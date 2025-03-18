<template>
      <div class="login-box">
        <h2 class="text-3xl font-bold text-center text-white">Вход</h2>
        <p class="text-gray-400 text-center mb-6">Введите свои данные для входа</p>
  
        <form @submit.prevent="handleLogin">
          <div class="input-group">
            <label for="email">Никнейм</label>
            <input type="nickname" id="nickname" v-model="nickname" placeholder="Введите никнейм" required />
          </div>
  
          <div class="input-group">
            <label for="password">Пароль</label>
            <input type="password" id="password" v-model="password" placeholder="Введите пароль" required />
          </div>
  
          <button type="submit" class="btn-login">Войти</button>
        </form>
  
        <p class="text-gray-400 text-sm text-center mt-4">
          Нет аккаунта?
          <router-link to="/register" class="text-yellow-400 hover:underline">Зарегистрируйтесь</router-link>
        </p>
    </div>
  </template>
  
  <script setup>
  import { loginUser } from '@/api/api';
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  
  const nickname = ref('');
  const password = ref('');
  const router = useRouter();
  
  const handleLogin = async() => {
    const params = {
        "password": password.value,
        "username": nickname.value
    }
    const login = await loginUser(params)
    if (login === 200) {
      alert('Успешный вход!');
      router.push('/profile');
    } else {
      alert('Неверные учетные данные!');
    }
  };
  </script>
  
  <style scoped>
  .login-box {
    background: #1a1a1a;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(255, 255, 255, 0.1);
    max-width: 400px;
    width: 100%;
    text-align: center;
  }
  
  /* Поля ввода */
  .input-group {
    margin-bottom: 1rem;
    text-align: left;
  }
  
  .input-group label {
    display: block;
    font-size: 14px;
    color: #ddd;
    margin-bottom: 4px;
  }
  
  .input-group input {
    width: 100%;
    padding: 12px;
    background: #2e2e2e;
    border: none;
    border-radius: 6px;
    color: white;
    font-size: 16px;
    outline: none;
    transition: all 0.3s ease;
  }
  
  .input-group input:focus {
    box-shadow: 0px 0px 10px rgba(255, 204, 0, 0.7);
  }
  
  /* Кнопка входа */
  .btn-login {
    width: 100%;
    background: linear-gradient(90deg, #FFC107, #FF9800);
    color: black;
    font-weight: bold;
    padding: 12px 24px;
    border-radius: 30px;
    font-size: 16px;
    margin-top: 10px;
    transition: all 0.3s ease-in-out;
    box-shadow: 0px 0px 15px rgba(255, 193, 7, 0.5);
    cursor: pointer;
  }
  
  .btn-login:hover {
    box-shadow: 0px 0px 25px rgba(255, 193, 7, 0.8);
  }
  </style>
  