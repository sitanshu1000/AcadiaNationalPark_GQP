<template>
  <div class="mb-5">
    <v-row>
      <v-file-input
        show-size
        label="File input"
        accept=".csv"
        @change="fileSelected"
      ></v-file-input>
      <v-btn @click="detail = !detail" text>Submission Details</v-btn>
    </v-row>
    <h3 class="mb-5" v-show="detail">
      Please submit a .csv file containing date, humidity, etc. to predict the
      volume and dwell time of cars on that day with Negative Binomial and
      Random Forest.
      <a
        href="https://docs.google.com/spreadsheets/d/e/2PACX-1vT9EKaA2X-bTwi9x41rWyeBzkJrgJybiKOBOVaiVWb9HPmUQBfGM8nEuwhOqJmp3oy6i0IvQcfIi88o/pubhtml"
        >Data submission example is here:</a
      >
      https://docs.google.com/spreadsheets/d/e/2PACX-1vT9EKaA2X-bTwi9x41rWyeBzkJrgJybiKOBOVaiVWb9HPmUQBfGM8nEuwhOqJmp3oy6i0IvQcfIi88o/pubhtml
    </h3>
    <div v-if="selectedFile">
      <div>
        <v-progress-linear
          v-model="progress"
          color="primary"
          dark
          height="25"
          reactive
        >
          <span>{{ progress }} %</span>
        </v-progress-linear>
      </div>
    </div>
    <v-col class="text-right">
      <v-btn elevation="2" @click="downloadFile" class="mr-3" color="primary"
        >Download Result</v-btn
      >
      <v-btn elevation="2" @click="uploadFile" color="primary">Upload</v-btn>
    </v-col>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      progress: 0,
      selectedFile: null,
      detail: false,
    };
  },
  methods: {
    convertTimestamp(timestamp) {
      var d = new Date(timestamp), // Convert the passed timestamp to milliseconds
        yyyy = d.getFullYear(),
        mm = ("0" + (d.getMonth() + 1)).slice(-2), // Months are zero based. Add leading 0.
        dd = ("0" + d.getDate()).slice(-2), // Add leading 0.
        time;

      // ie: 2013-02-18
      time = yyyy + "-" + mm + "-" + dd;
      return time;
    },
    fileSelected(file) {
      console.log(file);
      this.progress = 0;
      this.selectedFile = file;
      this.$store.state.haveResult = false;
    },
    uploadFile() {
      if (!this.selectedFile) {
        alert("Please select a file!");
        return;
      }
      const fd = new FormData();
      var vm = this;
      fd.append("file", this.selectedFile);
      axios
        .post("https://" + location.hostname + ":5000/fileupload", fd, {
          onUploadProgress: (uploadEvent) => {
            vm.progress = Math.round(
              (100 * uploadEvent.loaded) / uploadEvent.total
            );
            console.log(
              "Upload Progress: " + uploadEvent.loaded / uploadEvent.total
            );
          },
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then(async (response) => {
          var tmp = await JSON.parse(JSON.stringify(response.data));
          if (tmp["msg"] != "Success") {
            console.log("Failed");
            return;
          }
          vm.$store.state.haveResult = true;
          console.log(tmp);
          var dates = tmp["date"];
          console.log(dates);
          var volumeResult = JSON.parse(tmp["volume"]);
          var volParsed = [];
          for (var i = 0; i < dates.length; i++) {
            volParsed.push({
              text: vm.convertTimestamp(dates[i]),
              value: Math.round(volumeResult[i]),
            });
          }
          vm.$store.state.volume = volParsed;
          var dwellResult = JSON.parse(tmp["dwell"]);
          var dwellParsed = [];
          for (i = 0; i < dates.length; i++) {
            dwellParsed.push({
              text: vm.convertTimestamp(dates[i]),
              value: Math.round(dwellResult[i]),
            });
          }
          vm.$store.state.dwell = dwellParsed;
        });
    },
    downloadFile() {
      if (!this.$store.state.haveResult) {
        alert("Please select and upload file");
        return;
      }
      alert("Downloading Result");
      axios
        .get("https://" + location.hostname + ":5000/downloadresult", {
          responseType: "blob",
        })
        .then(async function (response) {
          console.log("download result");
          // let contentType = response.headers["content-type"]
          const url = window.URL.createObjectURL(new Blob([response.data]));
          const link = document.createElement("a");
          link.href = url;
          link.setAttribute("download", "Result.csv");
          document.body.appendChild(link);
          link.click();
        });
    },
  },
};
</script>
