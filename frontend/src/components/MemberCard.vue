<script setup>
defineProps({
  member: { type: Object, required: true },
})
</script>

<template>
  <div class="member-card">
    <div class="member-avatar" />
    <div class="member-info">
      <span class="label member-role">{{ member.role ?? 'ROLE' }}</span>
      <h3 class="member-name">{{ member.name ?? '氏名' }}</h3>
      <p class="member-research">{{ member.research ?? '研究テーマがここに入ります。' }}</p>
    </div>
  </div>
</template>

<style scoped>
.member-card {
  display: flex;
  gap: 24px;
  padding: 24px 0;
  border-top: 1px solid #e5e5e5;
}

.member-avatar {
  width: 80px;
  height: 80px;
  flex-shrink: 0;
  background: #e5e5e5;
  border-radius: 50%;
}

.member-info {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.member-role {
  display: block;
}

.member-name {
  font-size: 18px;
  font-weight: 700;
  color: #000;
  line-height: 1.4;
}

.member-research {
  font-size: 14px;
  color: #333;
  line-height: 1.75;
}
</style>
