<template>
  <div>
    <span 
      @click="updateMylistStatus(mylist)"
      :class="{ 'is-completed': mylist.isCompleted }"
    >
    {{ mylist.title }}
    </span>
    <button @click="deleteMylist(mylist)">Delete</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'MyListItem',
  props: {
    mylist: {
      type: Object,
    }
  },
  methods: {
    // deleteMylist: function () {
    //   this.$store.dispatch('deleteMylist', this.mylist)
    // },
    // updateMylistStatus: function () {
    //   this.$store.dispatch('updateMylistStatus', this.mylist)
    // },
    ...mapActions([
      'deleteMylist',
      'updateMylistStatus',
    ])
  }
}
</script>

<style>
  .is-completed {
    text-decoration: line-through;
  }
</style>