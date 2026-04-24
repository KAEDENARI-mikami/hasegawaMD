<template>
  <div>
    <!-- Page Header -->
    <section class="page-header">
      <div class="container">
        <span class="label">ABOUT</span>
        <h1 class="page-title">ゼミ紹介</h1>
      </div>
    </section>

    <!-- Philosophy -->
    <section class="section">
      <div class="container content-narrow">
        <p class="section-title">Philosophy</p>
        <h2 class="content-heading">ゼミの理念・テーマ</h2>
        <p class="content-body placeholder-text">
          ここにゼミの理念や研究テーマの説明が入ります。ゼミメンバーが後から内容を追記してください。
        </p>
      </div>
    </section>

    <!-- Research Fields -->
    <section class="section section--gray">
      <div class="container">
        <p class="section-title">Research Fields</p>
        <div class="fields-grid">
          <div v-for="n in 4" :key="n" class="field-item">
            <span class="label field-num">0{{ n }}</span>
            <h3 class="field-title">研究分野タイトル</h3>
            <p class="field-desc placeholder-text">この研究分野の説明がここに入ります。</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Activities -->
    <section class="section">
      <div class="container content-narrow">
        <p class="section-title">Activities</p>
        <h2 class="content-heading">活動内容</h2>
        <ul class="activity-list">
          <li v-for="n in 4" :key="n" class="activity-item placeholder-text">
            活動内容 {{ n }} がここに入ります。
          </li>
        </ul>
      </div>
    </section>
  </div>
</template>

<style scoped>
.page-header {
  background: #000;
  padding: 64px 0 48px;
}

.page-header .label {
  color: #757575;
  display: block;
  margin-bottom: 12px;
}

.page-title {
  font-size: clamp(32px, 5vw, 56px);
  font-weight: 700;
  color: #fff;
  line-height: 1.3;
}

.section--gray {
  background: #f8f8f8;
}

.content-narrow {
  max-width: 720px;
}

.content-heading {
  font-size: 24px;
  font-weight: 700;
  color: #000;
  margin-bottom: 20px;
  line-height: 1.5;
}

.content-body {
  font-size: 16px;
  color: #1a1a1a;
  line-height: 1.75;
}

.placeholder-text {
  color: #999;
}

.fields-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 40px;
}

.field-item {
  border-top: 2px solid #000;
  padding-top: 20px;
}

.field-num {
  display: block;
  margin-bottom: 8px;
}

.field-title {
  font-size: 20px;
  font-weight: 700;
  color: #000;
  margin-bottom: 12px;
}

.field-desc {
  font-size: 14px;
  line-height: 1.75;
}

.activity-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0;
}

.activity-item {
  font-size: 16px;
  line-height: 1.75;
  padding: 16px 0;
  border-bottom: 1px solid #e5e5e5;
}

@media (min-width: 640px) {
  .fields-grid { grid-template-columns: repeat(2, 1fr); }
}
</style>
