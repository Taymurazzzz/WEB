<template>
  <router-view />
</template>

<script>
export default {
  name: "App",
};
</script>

<style>
/* Глобальный фон */
body {
  background: linear-gradient(135deg, #0D0D0D, #1A1A1A);
  color: #EDEDED;
  font-family: "Inter", Arial, sans-serif;
  font-size: 16px;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
}

/* Улучшенный скролл */
::-webkit-scrollbar {
  width: 8px;
}
::-webkit-scrollbar-track {
  background: #111;
}
::-webkit-scrollbar-thumb {
  background: #444;
  border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
  background: #666;
}

/* Улучшенные заголовки */
h1, h2, h3, h4, h5, h6 {
  font-weight: 700;
  color: white;
  text-shadow: 2px 2px 10px rgba(255, 255, 255, 0.2);
}

/* Карточки */
.card {
  background: linear-gradient(135deg, #1A1A1A, #2E2E2E);
  border: 1px solid #333366;
  border-radius: 12px;
  padding: 20px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(255, 255, 255, 0.1);
}

/* Кнопки */
.btn-primary {
  background: linear-gradient(90deg, #FFC107, #FF9800);
  color: black;
  font-weight: bold;
  padding: 12px 24px;
  border-radius: 30px;
  font-size: 16px;
  transition: all 0.3s ease-in-out;
  box-shadow: 0px 0px 15px rgba(255, 193, 7, 0.5);
}

.btn-primary:hover {
  box-shadow: 0px 0px 25px rgba(255, 193, 7, 0.8);
}

.btn-secondary {
  background: linear-gradient(90deg, #00E676, #009688);
  color: black;
  font-weight: bold;
  padding: 12px 24px;
  border-radius: 30px;
  font-size: 16px;
  transition: all 0.3s ease-in-out;
  box-shadow: 0px 0px 15px rgba(0, 230, 118, 0.5);
}

.btn-secondary:hover {
  box-shadow: 0px 0px 25px rgba(0, 230, 118, 0.8);
}

/* Подвал */
footer {
  background: #222222;
  color: #A0A0A0;
  text-align: center;
  padding: 20px 0;
  border-top: 1px solid #333;
}
</style>
