<template>
  <div class="col">
    <article class="card">
      <img :src="thumbnailUrl" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">{{ movieCard.title }}</h5>
        <p class="card-text">{{ movieCard.overview }}</p>
      </div>
    </article>
   </div>
</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movieCard: Object
  },
  computed: {
    thumbnailUrl: function () {
      return `https://image.tmdb.org/t/p/original${this.movieCard.poster_path}`
    }
  }
}
</script>

<style>

</style>