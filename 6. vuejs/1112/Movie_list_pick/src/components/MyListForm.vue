<template>
  <div>
    <input 
      type="text"
      v-model.trim="mylistTitle"
      @keyup.enter="createMylist"
    >
    <button @click="createMylist">+</button>
  </div>
</template>

<script>
export default {
  name: 'MyListForm',
  data: function () {
    return {
      mylistTitle: null,
    }
  },
  methods: {
    createMylist: function () {
      const mylistItem = {
        title: this.mylistTitle,
        isCompleted: false,
        date: new Date().getTime(),
      }
      // console.log('Mylist create!!!')
      // this.$store.commit('CREATE_MYLIST', mylistItem)
      if (mylistItem.title) {
        this.$store.dispatch('createMylist', mylistItem) // actions 호출
      }
      this.mylistTitle = null
    }
  }
}
</script>

<style>

</style>