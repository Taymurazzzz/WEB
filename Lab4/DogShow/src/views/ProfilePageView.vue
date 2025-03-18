<template>
    <div class="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-gray-900 to-black px-6 py-10">
      
      <!-- Кнопка возврата на главную -->
      <button class="btn-back" @click="$router.push('/')">На главную</button>
  
      <div class="profile-card">
        <h2 class="text-3xl font-bold text-white text-center">Профиль</h2>
  
        <div class="profile-info">
          <p><strong>Имя:</strong> {{ user.firstName }}</p>
          <p><strong>Фамилия:</strong> {{ user.lastName }}</p>
          <p><strong>Никнейм:</strong> @{{ user.username }}</p>
        </div>
  
        <button class="btn-add-dog" @click="showModal = true">Добавить собаку</button>
      </div>
  
      <div v-if="user.dogs != undefined" class="dogs-container">
        <h3 class="text-2xl font-semibold text-white mt-6 mb-4 text-center">Ваши собаки</h3>
        <div class="dogs-list">
          <DogCard v-for="dog in user.dogs" :key="dog.id" :dog="dog" />
        </div>
      </div>
  
      <div v-else class="text-gray-400 text-lg mt-6">У вас пока нет собак.</div>
  
      <div v-if="showModal" class="modal">
        <div class="modal-content">
          <h3 class="text-xl font-bold text-white mb-4">Добавить собаку</h3>
          <form @submit.prevent="addDog">
            <div class="input-group">
              <label>Имя собаки</label>
              <input type="text" v-model="newDog.name" required />
            </div>
            <div class="input-group">
              <label>Порода</label>
              <input type="text" v-model="newDog.breed" required />
            </div>
            <div class="input-group">
              <label>Возраст</label>
              <input type="number" v-model="newDog.age" min="0" required />
            </div>
            <div class="input-group">
              <label>Клуб</label>
              <input type="text" v-model="newDog.club" required />
            </div>
            <div class="input-group">
              <label>Мать</label>
              <input type="text" v-model="newDog.mother_name" required />
            </div>
            <div class="input-group">
              <label>Отец</label>
              <input type="text" v-model="newDog.father_name" required />
            </div>
            <div class="input-group">
              <label>Документ</label>
              <input type="text" v-model="newDog.document" required />
            </div>
            <div class="input-group">
              <label>Классность</label>
              <input type="text" v-model="newDog.classRanking" required />
            </div>
            <button type="submit" class="btn-save">Сохранить</button>
            <button type="button" class="btn-close" @click="showModal = false">Отмена</button>
          </form>
        </div>
      </div>
  
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import { userInfo, getDog, createDog } from '@/api/api';
  import DogCard from '@/components/DogCard.vue';
  
  const router = useRouter();
  const user = ref({});
  onMounted(async () => {
      const userData = await userInfo();
      const dogs = await getDog(userData["id"]);
      user.value = {
          firstName: userData["first_name"],
          lastName: userData["last_name"],
          username: userData["username"],
          dogs: dogs
      };
  });
  
  const showModal = ref(false);
  
  const newDog = ref({
      name: "",
      club: "",
      breed: "",
      age: 0,
      classRanking: "",
      document: "",
      mother_name: "",
      father_name: "",
      owner: null
  });
  
  const addDog = async () => {
      const userData = await userInfo();
      newDog.value["owner"] = userData["id"];
      console.log(newDog.value);
      await createDog(newDog.value);
      showModal.value = false;
      newDog.value = {
          name: "",
          club: "",
          breed: "",
          age: 0,
          classRanking: "",
          document: "",
          mother_name: "",
          father_name: "",
          owner: null
      };
  };
  </script>
  
  <style scoped>
  /* Кнопка "На главную" */
  .btn-back {
    position: absolute;
    top: 20px;
    left: 20px;
    background: linear-gradient(90deg, #2196F3, #1E88E5);
    color: white;
    font-weight: bold;
    padding: 12px 20px;
    border-radius: 30px;
    font-size: 16px;
    transition: all 0.3s ease-in-out;
    box-shadow: 0px 0px 15px rgba(33, 150, 243, 0.5);
    cursor: pointer;
    border: none;
  }
  
  .btn-back:hover {
    box-shadow: 0px 0px 25px rgba(33, 150, 243, 0.8);
  }
  
  /* Карточка профиля */
  .profile-card {
    background: #1a1a1a;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(255, 255, 255, 0.1);
    max-width: 400px;
    width: 100%;
    text-align: center;
  }
  
  /* Информация о пользователе */
  .profile-info {
    margin-top: 1rem;
    color: #ddd;
    font-size: 18px;
    text-align: left;
    line-height: 1.6;
  }
  
  /* Кнопка добавления собаки */
  .btn-add-dog {
    background: linear-gradient(90deg, #FFC107, #FF9800);
    color: black;
    font-weight: bold;
    padding: 12px 24px;
    border-radius: 30px;
    font-size: 16px;
    transition: all 0.3s ease-in-out;
    box-shadow: 0px 0px 15px rgba(255, 193, 7, 0.5);
    cursor: pointer;
    margin-top: 12px;
  }
  
  .btn-add-dog:hover {
    box-shadow: 0px 0px 25px rgba(255, 193, 7, 0.8);
  }
  
  /* Контейнер для собак */
  .dogs-container {
    width: 100%;
    max-width: 800px;
    margin-top: 2rem;
  }
  
  /* Список собак */
  .dogs-list {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: center;
  }

  .modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: #1a1a1a;
  padding: 2rem;
  border-radius: 10px;
  width: 350px;
  text-align: center;
  box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.1);
}

/* Поля ввода */
.input-group {
  margin-bottom: 12px;
  text-align: left;
}

.input-group label {
  color: white;
  font-size: 14px;
}

.input-group input {
  width: 100%;
  padding: 8px;
  background: #2e2e2e;
  border: none;
  border-radius: 6px;
  color: white;
}

/* Кнопки */
.btn-save {
  background: #00E676;
  color: black;
  padding: 10px 20px;
  border-radius: 8px;
  font-weight: bold;
  cursor: pointer;
  width: 100%;
}

.btn-close {
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
  