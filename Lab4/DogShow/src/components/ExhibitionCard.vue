<template>
    <div class="card" @click="registerForEvent">
        <h2 class="text-2xl font-bold text-gray-900">{{ props.event?.name || "Название отсутствует" }}</h2>
        <p class="text-gray-600 mt-2">📅 Дата: {{ props.event?.date || "Дата неизвестна" }}</p>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
const props = defineProps({ event: Object });
const router = useRouter();

const registerForEvent = () => {
    router.push({ name: "RegisterEvent", params: { id: props.event.id }, state: { event: props.event } });
};
</script>