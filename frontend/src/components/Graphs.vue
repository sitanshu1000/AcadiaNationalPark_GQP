<template>
  <v-row>
    <v-col cols="12">
      <linechart :data="data"/>
    </v-col>
    <!-- <v-col cols="6">
      <boxplot :data="data"/>
    </v-col> -->
  </v-row>
</template>

<script>
import linechart from "./Linechart.vue";
// import boxplot from "./Boxplot.vue";

export default {
  props:["data"],
  components: {
    linechart,
    // boxplot,
  },
};
</script>
