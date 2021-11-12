<template>
  <div>
    <MyListItem
      v-for="mylist in mylists"
      :key="mylist.date"
      :mylist="mylist"
    />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import MyListItem from '@/components/MyListItem'

export default {
  name: 'MyList',
  components: {
    MyListItem,
  },
  // 1. 과거
  // computed: {
  //   mylists: function () {
  //     return this.$store.state.mylists
  //   },
  // }
  // 2.
  // computed: mapState([
  //   'mylists',
  // ]),
  // 3. 최종
  computed: {
    ...mapState([
      'mylists'
    ])
  }
}
</script>

<style>

</style>