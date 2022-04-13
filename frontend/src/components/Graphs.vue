<template>
  <v-row>
    <v-col cols="6">
      <linechart />
    </v-col>
    <v-col cols="6">
      <boxplot />
    </v-col>
  </v-row>
</template>

<script>
import linechart from "./Linechart.vue";
import boxplot from "./Boxplot.vue";

export default {
  components: {
    linechart,
    boxplot,
  },
};
</script>
