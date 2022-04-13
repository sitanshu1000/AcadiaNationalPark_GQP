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
    fileSelected(file) {
      console.log(file);
      this.progress = 0;
      this.selectedFile = file;
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
        .then((res) => {
          vm.$store.state.haveResult = true;
          console.log(res);
        });
    },
  },
};
</script>
