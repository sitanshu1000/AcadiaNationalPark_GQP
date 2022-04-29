<template>
  <div>
    <h4>Box Plot for {{ $store.state.pType }} Predictions</h4>
    <v-img src="http://localhost:5000/dwellBoxp.jpg"></v-img>
  </div>
</template>
<script>
// import VueApexCharts from "vue-apexcharts";
import * as d3 from "d3";
export default {
  props: ["data"],
  components: {
    // apexchart: VueApexCharts,
  },
  data() {
    return {
      series: [],
      chartOptions: {
        chart: {
          type: "boxPlot",
          height: 350,
        },
        title: {
          text: "",
          align: "left",
        },
        plotOptions: {
          boxPlot: {
            colors: {
              upper: "#5C4742",
              lower: "#A5978B",
            },
          },
        },
      },
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    getData() {
      var volumes = [];
      var data = this.data;
      data.forEach((element) => {
        volumes.push(element.value);
      });
      var data_sorted = volumes.sort(d3.ascending);
      var q1 = d3.quantile(data_sorted, 0.25);
      var median = d3.quantile(data_sorted, 0.5);
      var q3 = d3.quantile(data_sorted, 0.75);
      var interQuantileRange = q3 - q1;
      var min = q1 - 1.5 * interQuantileRange;
      var max = q1 + 1.5 * interQuantileRange;
      var analysis = [min, q1, median, q3, max];
      this.series = [
        {
          type: "boxPlot",
          data: [
            {
              x: "Analysis",
              y: analysis,
            },
          ],
        },
      ];
    },
  },
};
</script>