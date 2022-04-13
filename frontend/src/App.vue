<template>
  <v-app>
    <topbar />
    <v-main>
      <v-row class="mt-5">
        <v-col cols="2"></v-col>
        <v-col cols="8">
          <upload />
          <results />
        </v-col>
        <v-col></v-col>
      </v-row>
    </v-main>
  </v-app>
</template>

<script>
import topbar from "./components/Topbar.vue";
import upload from "./components/Upload.vue";
import results from "./components/Results.vue";

export default {
  name: "App",

  components: {
    topbar,
    upload,
    results,
  },

  data: () => ({
    //
  }),
};
</script>
