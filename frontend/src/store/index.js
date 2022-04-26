import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    pType:"Volume",
    haveResult: false,
    volume: [
      {
        text: "2022-05-01",
        value: 200,
      },
      {
        text: "2022-05-02",
        value: 500,
      },
      {
        text: "2022-05-03",
        value: 300,
      },
      {
        text: "2022-05-04",
        value: 400,
      },
      {
        text: "2022-05-05",
        value: 550,
      },
      {
        text: "2022-05-06",
        value: 100,
      },
      {
        text: "2022-05-07",
        value: 300,
      },
      {
        text: "2022-05-08",
        value: 400,
      },
      {
        text: "2022-05-09",
        value: 500,
      },
      {
        text: "2022-05-10",
        value: 580,
      },
      {
        text: "2022-05-11",
        value: 340,
      },
      {
        text: "2022-05-12",
        value: 550,
      },
      {
        text: "2022-05-13",
        value: 480,
      },
      {
        text: "2022-05-14",
        value: 460,
      },
      {
        text: "2022-05-15",
        value: 500,
      },
    ],
    dwell: [
      {
        text: "2022-05-01",
        value: 300,
      },
      {
        text: "2022-05-02",
        value: 500,
      },
      {
        text: "2022-05-03",
        value: 300,
      },
      {
        text: "2022-05-04",
        value: 400,
      },
      {
        text: "2022-05-05",
        value: 550,
      },
      {
        text: "2022-05-06",
        value: 100,
      },
      {
        text: "2022-05-07",
        value: 300,
      },
      {
        text: "2022-05-08",
        value: 400,
      },
      {
        text: "2022-05-09",
        value: 500,
      },
      {
        text: "2022-05-10",
        value: 580,
      },
      {
        text: "2022-05-11",
        value: 340,
      },
      {
        text: "2022-05-12",
        value: 550,
      },
      {
        text: "2022-05-13",
        value: 480,
      },
      {
        text: "2022-05-14",
        value: 460,
      },
      {
        text: "2022-05-15",
        value: 500,
      },
    ],
  },
  getters: {
    resultsData(state) {
      return state.results
    }
  },
  mutations: {
    uptextLoc: (state, newLoc) => {
      state.location = newLoc
    },
    uptextStatus: (state, newStatus) => {
      state.status = newStatus
    },
    uptextTable: (state, newTable) => {
      state.table = newTable
    }
  },
  actions: {
    uptextLoc: (context, newLoc) => {
      context.commit("uptextLoc", newLoc)
    }
  },
  modules: {
  }
})