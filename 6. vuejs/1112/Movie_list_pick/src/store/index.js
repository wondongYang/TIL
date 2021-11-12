import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    movieCards: [],
    mylists: [],
  },
  mutations: {
    LOAD_MOVIE_CARDS: function (state, results) {
      state.movieCards = results
    },
    CREATE_MYLIST: function (state, mylistItem) {
      // console.log(state)
      // console.log(mylistItem)
      state.mylists.push(mylistItem) // state 변경
    },
    DELETE_MYLIST: function (state, mylistItem) {
      const index = state.mylists.indexOf(mylistItem)
      state.mylists.splice(index, 1)
    },
    UPDATE_MYLIST_STATUS: function (state, mylistItem) {
      state.mylists = state.mylists.map(mylist => {
        if (mylist === mylistItem) {
          return {
            ...mylist, // JS spread syntax
            isCompleted: !mylist.isCompleted
          }
        } else {
          return mylist
        }
      })
    },
  },
  actions: {
    LoadMovieCards: function ({commit}) {
      axios({
        method: 'get',
        url: 'https://api.themoviedb.org/3/movie/top_rated',
        params: {
          api_key: '2176e678f7fd85bcdcc3c92afb413dbe',
          language: 'ko-KR',
        }
      })
        .then((res) => {
          console.log(res)
          commit('LOAD_MOVIE_CARDS', res.data.results)
        })
    },
    createMylist: function ({ commit }, mylistItem) {
      // console.log(context)
      // console.log(mylistItem)
      commit('CREATE_MYLIST', mylistItem)
    },
    deleteMylist: function ({ commit }, mylistItem) {
      commit('DELETE_MYLIST', mylistItem)
    },
    updateMylistStatus: function ({ commit }, mylistItem) {
      commit('UPDATE_MYLIST_STATUS', mylistItem)
    },
  },
  modules: {
  }
})