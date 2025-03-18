<template>
    <div class="dog-card">
      <div class="dog-info">
        <h3 class="dog-name">{{ dog.name }}</h3>
        <p><strong>Порода:</strong> {{ dog.breed }}</p>
        <p><strong>Возраст:</strong> {{ dog.age }} лет</p>
        <p><strong>Клуб:</strong> {{ dog.club }}</p>
        <p v-if="dog.mother_name"><strong>Мать:</strong> {{ dog.mother_name }}</p>
        <p v-if="dog.father_name"><strong>Отец:</strong> {{ dog.father_name }}</p>
        <p><strong>Рейтинг:</strong> {{ dog.classRanking }}</p>
        <p><strong>Документ:</strong> {{ dog.document }}</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { defineProps } from 'vue';
  
  const props = defineProps({
    dog: Object
  });
  
  // Фото по умолчанию
  const defaultDogImage = "https://via.placeholder.com/300x200?text=No+Image";
  </script>
  
  <style scoped>
  .dog-card {
    background: #222;
    padding: 12px;
    border-radius: 10px;
    text-align: center;
    width: 250px;
    box-shadow: 0 5px 15px rgba(255, 255, 255, 0.1);
    transition: transform 0.3s ease-in-out;
  }
  
  .dog-card:hover {
    transform: translateY(-5px);
  }
  
  /* Фото собаки */
  .dog-image {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 8px;
  }
  
  /* Имя собаки */
  .dog-name {
    margin-top: 8px;
    color: white;
    font-weight: bold;
    font-size: 18px;
  }
  
  /* Текстовое описание */
  p {
    color: #ccc;
    font-size: 14px;
    margin: 4px 0;
  }
  </style>
  