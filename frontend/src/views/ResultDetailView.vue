<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const article = ref(null)

onMounted(async () => {
  try {
    article.value = await fetch(`http://localhost:8000/api/articles/${route.params.id}`).then(r => r.json())
  } catch {
    article.value = {
      title: '成果タイトルがここに入ります',
      category: 'CATEGORY',
      published_at: '----/--/--',
      content: '本文がここに入ります。ゼミメンバーが後から内容を追記してください。',
    }
  }
})
</script>

<template>
  <div v-if="article">
    <section class="page-header">
      <div class="container">
        <span class="label">{{ article.category ?? 'CATEGORY' }}</span>
        <h1 class="page-title">{{ article.title }}</h1>
        <span class="label article-date">{{ article.published_at ?? '----/--/--' }}</span>
      </div>
    </section>

    <article class="section">
      <div class="container article-body">
        <p class="article-content">{{ article.content }}</p>
      </div>
    </article>
  </div>
</template>

<style scoped>
.page-header {
  background: #000;
  padding: 64px 0 48px;
}
.page-header .label { color: #757575; display: block; margin-bottom: 12px; }
.article-date { display: block; margin-top: 16px; }
.page-title {
  font-size: clamp(24px, 4vw, 40px);
  font-weight: 700;
  color: #fff;
  line-height: 1.4;
  margin-top: 8px;
}
.article-body { max-width: 720px; }
.article-content {
  font-size: 16px;
  line-height: 1.75;
  color: #1a1a1a;
}
</style>
