<template>
  <n-alert :show-icon="false" type="info" class="progress">
    <Progress :status="step"/>
  </n-alert>
  <n-scrollbar>
    <Form />
  </n-scrollbar>
</template>

<script setup>
import Progress from './progress.vue'
import Form from './form.vue'
import api from '@/api'
const step = 1
const user = api.getUserInfo()
console.log(user)


</script>

<style scoped>
.progress {
  margin: 20px;
}
</style>