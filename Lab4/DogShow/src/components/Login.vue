<template>
  <div>
    <input type="username" v-model="username" placeholder="Uername">
    <input type="password" v-model="password" placeholder="Password">
    <button @click="login">Login</button>
  </div>
</template>

<script>
import axios from 'axios'
defineExpose({
  name: 'Login',
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    login() {
      axios.post('http://localhost:8000/auth/token/login', {
        password: this.data.password,
        username: this.data.username
      })


    }
  }
})
</script>
