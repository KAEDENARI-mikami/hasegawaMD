<script setup>
import { ref, onMounted } from 'vue'
import ArticleCard from '../components/ArticleCard.vue'

const articles = ref([])
const loading = ref(true)

onMounted(async () => {
  try {
    const data = await fetch('http://localhost:8000/api/articles?category=results').then(r => r.json())
    articles.value = data
  } catch {
    articles.value = Array.from({ length: 6 }, (_, i) => ({ id: i + 1 }))
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div>
    <section class="page-header">
      <div class="container">
        <span class="label">RESULTS</span>
        <h1 class="page-title">成果発表</h1>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <p v-if="loading" class="loading label">Loading...</p>
        <div v-else class="grid-3">
          <ArticleCard
            v-for="article in articles"
            :key="article.id"
            :article="article"
            :to="`/results/${article.id}`"
          />
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.page-header {
  background: #000;
  padding: 64px 0 48px;
}
.page-header .label { color: #757575; display: block; margin-bottom: 12px; }
.page-title {
  font-size: clamp(32px, 5vw, 56px);
  font-weight: 700;
  color: #fff;
}
.grid-3 {
  display: grid;
  grid-template-columns: 1fr;
  gap: 40px;
}
.loading { color: #757575; }
@media (min-width: 640px) { .grid-3 { grid-template-columns: repeat(2, 1fr); } }
@media (min-width: 960px) { .grid-3 { grid-template-columns: repeat(3, 1fr); } }
</style>
