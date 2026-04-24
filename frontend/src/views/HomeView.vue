<script setup>
import { ref, onMounted } from 'vue'
import ArticleCard from '../components/ArticleCard.vue'

const latestResults = ref([])
const latestNews = ref([])

onMounted(async () => {
  try {
    const [r1, r2] = await Promise.all([
      fetch('http://localhost:8000/api/articles?category=results&limit=3').then(r => r.json()),
      fetch('http://localhost:8000/api/articles?category=news&limit=3').then(r => r.json()),
    ])
    latestResults.value = r1
    latestNews.value = r2
  } catch {
    latestResults.value = [{ id: 1 }, { id: 2 }, { id: 3 }]
    latestNews.value = [{ id: 1 }, { id: 2 }, { id: 3 }]
  }
})
</script>

<template>
  <!-- Hero -->
  <section class="hero">
    <div class="hero-overlay">
      <div class="container">
        <span class="label hero-label">HASEGAWA LABORATORY</span>
        <h1 class="hero-title">ゼミのキャッチコピーが<br>ここに入ります</h1>
        <p class="hero-desc">サブタイトルや一言説明がここに入ります。ゼミメンバーが後から編集してください。</p>
        <RouterLink to="/about" class="btn-primary">LEARN MORE</RouterLink>
      </div>
    </div>
  </section>

  <!-- Latest Results -->
  <section class="section">
    <div class="container">
      <p class="section-title">Latest Results</p>
      <div class="grid-3">
        <ArticleCard
          v-for="article in latestResults"
          :key="article.id"
          :article="article"
          :to="`/results/${article.id}`"
        />
      </div>
      <div class="more-link">
        <RouterLink to="/results" class="btn-primary">SEE ALL RESULTS</RouterLink>
      </div>
    </div>
  </section>

  <!-- Latest News -->
  <section class="section section--gray">
    <div class="container">
      <p class="section-title">News</p>
      <div class="grid-3">
        <ArticleCard
          v-for="article in latestNews"
          :key="article.id"
          :article="article"
          :to="`/news/${article.id}`"
        />
      </div>
      <div class="more-link">
        <RouterLink to="/news" class="btn-primary">SEE ALL NEWS</RouterLink>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero {
  background: #111;
  min-height: 480px;
  display: flex;
  align-items: flex-end;
}

.hero-overlay {
  width: 100%;
  padding: 80px 0;
}

.hero-label {
  display: block;
  color: #757575;
  margin-bottom: 16px;
}

.hero-title {
  font-size: clamp(28px, 5vw, 56px);
  font-weight: 700;
  line-height: 1.3;
  color: #fff;
  margin-bottom: 16px;
}

.hero-desc {
  font-size: 16px;
  color: #999;
  max-width: 480px;
  margin-bottom: 32px;
  line-height: 1.75;
}

.grid-3 {
  display: grid;
  grid-template-columns: 1fr;
  gap: 40px;
}

.more-link {
  margin-top: 48px;
}

.section--gray {
  background: #f8f8f8;
}

@media (min-width: 640px) {
  .grid-3 { grid-template-columns: repeat(2, 1fr); }
}

@media (min-width: 960px) {
  .grid-3 { grid-template-columns: repeat(3, 1fr); }
}
</style>
