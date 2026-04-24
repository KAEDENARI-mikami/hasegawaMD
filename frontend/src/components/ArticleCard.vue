<script setup>
defineProps({
  article: { type: Object, required: true },
  to: { type: String, required: true },
})
</script>

<template>
  <RouterLink :to="to" class="card">
    <div class="card-image-wrap">
      <div class="card-image-placeholder" />
    </div>
    <div class="card-body">
      <span class="label card-category">{{ article.category ?? 'CATEGORY' }}</span>
      <h3 class="card-title">{{ article.title ?? 'タイトルがここに入ります' }}</h3>
      <p class="card-summary">{{ article.summary ?? '概要文がここに入ります。ゼミメンバーが後から追記します。' }}</p>
      <span class="card-date label">{{ article.published_at ?? '----/--/--' }}</span>
    </div>
  </RouterLink>
</template>

<style scoped>
.card {
  display: flex;
  flex-direction: column;
  border-top: 2px solid #000;
  transition: opacity 0.2s;
}

.card:hover {
  opacity: 0.75;
}

.card-image-wrap {
  width: 100%;
  aspect-ratio: 16 / 9;
  overflow: hidden;
  background: #f2f2f2;
  margin-bottom: 16px;
}

.card-image-placeholder {
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #e5e5e5 25%, #d0d0d0 75%);
}

.card-body {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.card-category {
  display: block;
}

.card-title {
  font-size: 20px;
  font-weight: 700;
  line-height: 1.6;
  color: #000;
}

.card-summary {
  font-size: 14px;
  color: #333;
  line-height: 1.75;
}

.card-date {
  margin-top: 4px;
}
</style>
