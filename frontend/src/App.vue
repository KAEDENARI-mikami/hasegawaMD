<script setup>
import TheHeader from './components/TheHeader.vue'
import TheFooter from './components/TheFooter.vue'
</script>

<template>
  <TheHeader />
  <main style="flex: 1;">
    <RouterView />
  </main>
  <TheFooter />
</template>
