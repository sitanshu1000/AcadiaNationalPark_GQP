<template>
  <apexchart
    type="line"
    height="350"
    :options="chartOptions"
    :series="series"
  ></apexchart>
</template>
<script>
import VueApexCharts from "vue-apexcharts";

export default {
  components: {
    apexchart: VueApexCharts,
  },
  data() {
    return {
      series: [],
      chartOptions: {
        chart: {
          height: 350,
          type: "line",
          zoom: {
            enabled: false,
          },
        },
        dataLabels: {
          enabled: false,
        },
        stroke: {
          curve: "straight",
        },
        title: {
          text: "Line Chart for Volume Predictions",
          align: "left",
        },
        grid: {
          row: {
            colors: ["#f3f3f3", "transparent"], // takes an array which will be repeated on columns
            opacity: 0.5,
          },
        },
        xaxis: {
          categories: [],
        },
      },
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    getData() {
      var dates = [];
      var volumes = [];
      var data = this.$store.state.results;
      data.forEach((element) => {
        dates.push(element.text);
        volumes.push(element.value);
      });
      this.series = [
        {
          name: "Volumes",
          data: volumes,
        },
      ];
      console.log(this.chartOptions.xaxis.categories);
      this.chartOptions = {
        chart: {
          height: 350,
          type: "line",
          zoom: {
            enabled: false,
          },
        },
        dataLabels: {
          enabled: false,
        },
        stroke: {
          curve: "straight",
        },
        title: {
          text: "Line Chart for Volume Predictions",
          align: "left",
        },
        grid: {
          row: {
            colors: ["#f3f3f3", "transparent"], // takes an array which will be repeated on columns
            opacity: 0.5,
          },
        },
        xaxis: {
          categories: dates,
        },
      };
    },
  },
};
</script>