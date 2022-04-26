<template>
  <div>
    <div v-if="haveResults">
      <v-col class="d-flex" cols="12" sm="6">
        <v-select
          :items="predictionType"
          label="Prediction Type"
          v-model="pType"
          @change="refresh"
          dense
        ></v-select>
      </v-col>
      <v-tabs
        v-model="tab"
        background-color="transparent"
        color="basil"
        grow
        class="mb-5"
      >
        <v-tab v-for="item in items" :key="item">
          {{ item }}
        </v-tab>
      </v-tabs>
      <v-data-table
        v-if="tab == 0"
        :headers="headers"
        :items="results"
        :items-per-page="5"
        class="elevation-1 mt-7"
      ></v-data-table>
      <Graphs v-else-if="tab == 1" :data="results" />
    </div>
    <div v-else class="text-center">
      <h1>The results will be here.</h1>
    </div>
  </div>
</template>

<script>
import Graphs from "./Graphs.vue";
export default {
  components: {
    Graphs,
  },
  data() {
    return {
      tab: null,
      items: ["Data Table", "Visualization"],
      pType: "Volume",
      predictionType: ["Volume", "Dwell Time"],
      headers: [
        { text: "Date", value: "text", sortable: false },
        { text: "Volume", value: "value", sortable: true },
      ],
    };
  },
  methods: {
    refresh() {
      this.tab = 0;
      this.$store.state.pType = this.pType;
      this.headers = [
        { text: "Date", value: "text", sortable: false },
        { text: this.pType, value: "value", sortable: true },
      ];
    },
  },
  computed: {
    results() {
      if (this.pType == "Volume") {
        return this.$store.state.volume;
      }
      return this.$store.state.dwell;
    },
    haveResults() {
      return this.$store.state.haveResult;
    },
  },
  mounted() {
    console.log(this.results);
  },
};
</script>