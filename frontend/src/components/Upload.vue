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
      selectedFile: null,
    };
  },
  methods: {
    fileSelected(file) {
      console.log(file);
      this.selectedFile = file;
    },
    uploadFile() {
      if (!this.selectedFile) {
        this.message = "Please select a file!";
        return;
      }
      const fd = new FormData();
      var vm = this;
      fd.append("file", this.selectedFile);
      axios
        .post("http://" + location.hostname + ":5000/fileupload", fd, {
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
