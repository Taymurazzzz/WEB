<template>
    <div class="relative min-h-screen flex flex-col justify-center items-center text-white px-6">
      <!-- Контейнер, чтобы все элементы были по центру -->
      <div class="w-full max-w-6xl mx-auto px-6">
        
        <!-- Фиксированные кнопки в правом верхнем углу -->
        <div class="flex justify-end space-x-4 mt-6">
          <button 
            class="btn-primary"
            @click="$router.push('/login')">
            Войти
          </button>
          <button 
            class="btn-secondary"
            @click="$router.push('/profile')">
            Профиль
          </button>
        </div>
  
        <!-- Центрированный заголовок -->
        <div class="text-center mt-6">
          <h1 class="text-6xl font-extrabold tracking-wide bg-gradient-to-r from-yellow-400 to-orange-500 text-transparent bg-clip-text drop-shadow-lg">
            Выставки собак
          </h1>
          <p class="text-lg text-gray-300 mt-3 max-w-2xl mx-auto">
            Добро пожаловать на портал выставок собак! Найдите лучшее событие для вас и вашего питомца.
          </p>
        </div>
  
        <!-- Карточки с выставками -->
        <div v-if="events.length" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8 mt-12">
          <ExhibitionCard v-for="event in events" :key="event.id" :event="event" />
        </div>
        <div v-else class="text-lg text-gray-400 font-medium mt-12">Нет событий для отображения</div>
  
      </div>
    </div>
  </template>
  
  <script setup>
  import { getShows } from '@/api/api';
  import { ref, onMounted } from 'vue';
  import ExhibitionCard from '@/components/ExhibitionCard.vue';
  
  const events = ref([]);
  
  onMounted(async() => {
    events.value = await getShows();
  });
  </script>
  
