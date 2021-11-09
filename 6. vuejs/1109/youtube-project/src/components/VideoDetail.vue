<template>
  <div v-if="video">
    <iframe :src="videoURL" frameborder="0"></iframe>
    <h2>title: {{ video.snippet.title | stringUnescape }}</h2>
    <p>description: {{ video.snippet.description | stringUnescape }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoDetail',
  props: {
    video: {
      type: [String, Object], //처음에 아무것도 안고른 경우, 골랐을 경우
    }
  },
  computed: {
    videoURL: function () {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  },
  filters: {
    stringUnescape: function (rawText) {
      return _.unescape(rawText)
    }
  }
}
</script>

<style>

</style>