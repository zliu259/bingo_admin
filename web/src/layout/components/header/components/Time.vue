<script setup>
import { ref, onMounted } from 'vue'

const currentTime = ref('')
const currentDate = ref('')
const timeZone = Intl.DateTimeFormat().resolvedOptions().timeZone

const updateTime = () => {
  const now = new Date()
  currentTime.value = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
  currentDate.value = now.toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' }).replace(/ /g, '-')
}

onMounted(() => {
  updateTime()
  setInterval(updateTime, 6000) // Update every minute
})
</script>

<template>
  <div>
    <p>{{ timeZone }} {{ currentDate }} {{ currentTime }}</p>
  </div>
</template>

<style scoped>
p {
  margin-right: 10px;
  font-size: 16px;
}
</style>