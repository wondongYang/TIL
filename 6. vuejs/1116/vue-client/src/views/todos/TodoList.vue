<template>
  <div>
    <ul>
      <li v-for="(todo, idx) in todos" :key="idx">
        <span @click="updateTodoStatus(todo)" :class="{ completed: todo.completed }">{{ todo.title }}</span>
        <button @click="deleteTodo(todo)" class="todo-btn">X</button>
      </li>
    </ul>
    <!-- <button @click="getTodos">Get Todos</button> -->
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'TodoList',
  data: function () {
    return {
      todos: [],
    }
  },
  methods: {
    getTodos: function () {
      axios.get(`${SERVER_URL}/todos/`)
        .then((res) => {
          console.log(res)
          this.todos = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteTodo: function (todo) {
      axios.delete(`${SERVER_URL}/todos/${todo.id}/`)
        .then((res) => {
          console.log(res)
          const targetTodoIdx = this.todos.findIndex((todo) => {
            return todo.id === res.data.id
          })
          this.todos.splice(targetTodoIdx, 1)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    updateTodoStatus: function (todo) {
      const todoItem = {
        // { todo.title = this.title, ...}
        ...todo, // 20개가 있다면 전부 다 바꿔야함(번거롭다!)
        // ...todo 이렇게하면 나머지는 그대로 두고 라는 의미.
        completed: !todo.completed
      }

      axios.put(`${SERVER_URL}/todos/${todo.id}/`, todoItem)
        .then((res) => {
          console.log(res)
          todo.completed = !todo.completed
        })
      },
    },
  created: function () {
    this.getTodos()
    // vuex에서는 actions을 호출(store안에 actions을 호출)
  }
}
</script>

<style scoped>
  .todo-btn {
    margin-left: 10px;
  }

  .completed {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }
</style>