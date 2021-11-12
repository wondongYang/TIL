<template>
  <div>
    <h2>My Movie List</h2>
    <MyListForm />
    <br>
    <MyList />
  </div>
</template>

<script>
import MyListForm from '@/components/MyListForm'
import MyList from '@/components/MyList'

export default {
  name: 'MyMoiveList',
  components: {
    MyListForm,
    MyList,
  },
}
</script>

<style>

</style>