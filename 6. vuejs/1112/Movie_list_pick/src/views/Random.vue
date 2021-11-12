<template>
  <div>
    <button class="btn btn-success" @click="PickOneMovie">PICK</button>
    <br>   
    <img :src="thumbnailUrl" class="img-fluid" alt="">
    <h2>{{ selectedMovie.title }}</h2>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import MovieCard from '@/components/MovieCard'
import _ from 'lodash'

export default {
  name: 'Random',
  component: {
    MovieCard,
  },
  created: function () {
    this.$store.dispatch('LoadMovieCards')
  },
  computed: {
    ...mapState(['movieCards']),
    thumbnailUrl: function () {
      console.log(this.selectedMovie.poster_path)
      return `https://image.tmdb.org/t/p/original${this.selectedMovie.poster_path}`
    }
  },
  data: function () {
    return {
      selectedMovie: [],
    }
  },
  methods: {
    PickOneMovie: function () {
      const randomIndex = _.random(this.movieCards.length - 1)
      this.selectedMovie = this.movieCards[randomIndex]
    }
  }
}
</script>

<style>
 
</style>