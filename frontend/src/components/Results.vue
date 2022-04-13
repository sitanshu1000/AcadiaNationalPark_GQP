<template>
  <div v-show="haveResults">
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
    <Graphs v-else-if="tab == 1" />
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
      headers: [
        { text: "Date", value: "text", sortable: false },
        { text: "Volume", value: "value", sortable: true },
      ],
    };
  },
  computed: {
    results() {
      return this.$store.state.results;
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