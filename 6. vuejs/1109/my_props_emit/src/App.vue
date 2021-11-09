<template>
  <div id="app">
    <!-- 3. 사용한다 -->
    <h1>App</h1>
    <p>AppData: {{ appData }}</p>
    <input v-model="appData" type="text">
    <p>ParentData: {{ parentData }}</p>
    <p>ChildData: {{ childData }}</p>
    <Parent :appData="appData" 
    @child-input="inputChildData" @parent-input="inputParentData" />
  </div>
</template>

<script>
// 1. 불러온다
import Parent from './components/Parent.vue'

export default {
  name: 'App',
  // 2. 등록한다
  components: {
    Parent,
  },
  methods: {
    inputChildData: function (data) {
      this.childData = data
    },
    inputParentData: function (data) {
      this.parentData = data
    }
  },
  data: function () {
    return {
      appData: '',
      parentData: '',
      childData: '',
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
