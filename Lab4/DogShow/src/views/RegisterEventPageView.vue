<template>
    <div class="register-page">
      <div class="register-card">
        <h2 class="text-3xl font-bold text-white text-center">Запись на выставку</h2>
        <p class="event-name">{{ event?.name }}</p>
        <p class="event-date">📅 Дата: {{ event?.date }}</p>
  
        <div class="input-group">
          <label for="dogSelect">Выберите собаку:</label>
          <select id="dogSelect" v-model="selectedDog" class="select-dog">
            <option v-for="dog in userDogs" :key="dog.id" :value="dog.id">
              {{ dog.name }} ({{ dog.breed }})
            </option>
          </select>
        </div>
  
        <button class="btn-register" @click="registerForEvent" :disabled="!selectedDog">Записаться</button>
        <button class="btn-back" @click="$router.push('/')">Назад</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  import { getShowsById, getDog, userInfo, regDog } from '@/api/api';
  
  const route = useRoute();
  const router = useRouter();
  
  const userDogs = ref([]);
  const event = ref()
  const eventId = ref(route.params.id);
  const selectedDog = ref(null);
  
  onMounted(async () => {
    event.value = await getShowsById(eventId.value);
    const userData = await userInfo();
    userDogs.value = await getDog(userData["id"]);
  });
  const registerForEvent = async () => {
    try {
        const params = {
            dog: selectedDog.value,
            show: eventId.value
        }
        await regDog(params);
        alert("Собака успешно записана на выставку!");
        router.push('/');
    } catch (error) {
        console.error("Ошибка записи:", error);
        alert("Не удалось записать собаку, попробуйте позже.");
    }
  };
  </script>
  
  <style scoped>
  .register-page {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background: #1a1a1a;
  }
  
  .register-card {
    background: #222;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    width: 350px;
    box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.1);
  }
  
  .event-name {
    color: white;
    font-size: 20px;
    font-weight: bold;
  }
  
  .event-date {
    color: #bbb;
    font-size: 16px;
    margin-bottom: 12px;
  }
  
  /* Выпадающий список */
  .input-group {
    margin: 15px 0;
  }
  
  .input-group label {
    color: white;
    font-size: 16px;
  }
  
  .select-dog {
    width: 100%;
    padding: 10px;
    background: #2e2e2e;
    color: white;
    border-radius: 6px;
    border: none;
  }
  
  /* Кнопки */
  .btn-register {
    background: linear-gradient(90deg, #00E676, #00C853);
    color: black;
    font-weight: bold;
    padding: 12px 24px;
    border-radius: 8px;
    font-size: 16px;
    cursor: pointer;
    margin: 10px 0;
  }
  
  .btn-register:disabled {
    background: #555;
    cursor: not-allowed;
  }
  
  .btn-back {
    background: #FF1744;
    color: white;
    padding: 10px 20px;
    border-radius: 8px;
    font-weight: bold;
    cursor: pointer;
    width: 100%;
    margin-top: 8px;
  }
  </style>
  