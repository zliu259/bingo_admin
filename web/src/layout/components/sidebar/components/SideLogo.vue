<template>
  <router-link h-60 f-c-c to="/">
    <img :src="logo" alt="Logo" class="logo" />
    <h2
      v-show="!appStore.collapsed"
      ml-2
      mr-8
      max-w-150
      flex-shrink-0
      text-16
      font-bold
      color-primary
    >
      {{ title }}
    </h2>
  </router-link>
</template>

<script setup>
import { useAppStore } from '@/store'
import logo from '@/assets/33fdb073c5f65d762bfb666444b2d58.png'

const title = import.meta.env.VITE_TITLE
const appStore = useAppStore()
</script>

<style scoped>
.logo {
  width: 80px; /* Adjust the width as needed */
  height: auto; /* Maintain aspect ratio */
}
</style>