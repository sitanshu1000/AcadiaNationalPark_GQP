<template>
  <div class="mb-5">
    <h3 class="mb-5">
      Please submit a .csv file containing date, humidity, etc. to predict the
      volume of cars on that day with Negative Binomial.
    </h3>
    <v-row>
      <v-file-input
        show-size
        label="File input"
        accept=".csv"
        @change="fileSelected"
      ></v-file-input>
    </v-row>
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
      <v-btn elevation="2" @click="uploadFile">Upload</v-btn>
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
        .post("http://" + location.hostname + ":5000/fileupload", fd, {
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
          if (tmp["msg"] == "Success") {
            console.log("Success");
            vm.$store.state.haveResult = true;
          }
          var volumeResult = JSON.parse(tmp["volume"]);
          var volParsed = [];
          for (var i = 0; i < volumeResult["index"].length; i++) {
            volParsed.push({
              text: vm.convertTimestamp(volumeResult["index"][i]),
              value: Math.round(volumeResult["data"][i]),
            });
          }
          vm.$store.state.volume = volParsed;
          var dwellResult = JSON.parse(tmp["dwell"]);
          var dwellParsed = [];
          for (i = 0; i < volumeResult["index"].length; i++) {
            dwellParsed.push({
              text: vm.convertTimestamp(volumeResult["index"][i]),
              value: Math.round(dwellResult[i]),
            });
          }
          vm.$store.state.dwell = dwellParsed;
        });
    },
  },
};
</script>
