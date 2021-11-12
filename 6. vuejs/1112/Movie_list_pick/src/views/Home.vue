<template>
  <div class="row row-cols-1 row-cols-md-3 g-4">
    <MovieCard 
      v-for="movieCard in movieCards"
      :key="movieCard.id"
      :movieCard="movieCard"
    />
  </div>
</template>

<script>
// @ is an alias to /src
import MovieCard from '@/components/MovieCard'
import { mapState } from 'vuex'

export default {
  name: 'Home',
  components: {
    MovieCard,
  },
  created: function () {
    this.$store.dispatch('LoadMovieCards')
  },
  computed: {
    ...mapState(['movieCards'])
  }
}
</script>
