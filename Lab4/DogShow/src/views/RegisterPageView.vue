<template>
    <div class="h-screen flex justify-center items-center bg-gradient-to-br from-gray-900 to-black px-6">
      <div class="register-box">
        <h2 class="text-3xl font-bold text-center text-white">Регистрация</h2>
        <p class="text-gray-400 text-center mb-6">Создайте новый аккаунт</p>
  
        <form @submit.prevent="handleRegister">
          <div class="input-group">
            <label for="firstName">Имя</label>
            <input type="text" id="firstName" v-model="user.first_name" placeholder="Введите имя" required />
          </div>
  
          <div class="input-group">
            <label for="lastName">Фамилия</label>
            <input type="text" id="lastName" v-model="user.last_name" placeholder="Введите фамилию" required />
          </div>
  
          <div class="input-group">
            <label for="nickname">Никнейм</label>
            <input type="text" id="nickname" v-model="user.username" placeholder="Введите никнейм" required />
          </div>
  
          <div class="input-group">
            <label for="email">Email</label>
            <input type="email" id="email" v-model="user.email" placeholder="Введите email" required />
          </div>
  
          <div class="input-group">
            <label for="password">Пароль</label>
            <input type="password" id="password" v-model="user.password" placeholder="Введите пароль" required />
          </div>
  
          <button type="submit" class="btn-register">Зарегистрироваться</button>
        </form>
  
        <p class="text-gray-400 text-sm text-center mt-4">
          Уже есть аккаунт?
          <router-link to="/login" class="text-yellow-400 hover:underline">Войти</router-link>
        </p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  import { regUser } from '@/api/api';
  
  const router = useRouter();
  
  const user = ref({
    password: "",
    username: "",
    first_name: "",
    last_name: "",
    email: "",
  });
  
  const handleRegister = async () => {
    try {
      const response = await regUser(user.value)
    
      alert("Регистрация успешна!");
      router.push("/login");
    } catch (error) {
      console.error("Ошибка регистрации:", error);
      alert("Ошибка регистрации. Попробуйте снова.");
    }
  };
  </script>
  
  <style scoped>
  /* Центрированная форма */
  .register-box {
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
  
  /* Кнопка регистрации */
  .btn-register {
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
  
  .btn-register:hover {
    box-shadow: 0px 0px 25px rgba(255, 193, 7, 0.8);
  }
  </style>
  