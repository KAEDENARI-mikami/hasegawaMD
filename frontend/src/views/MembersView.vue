<script setup>
import { ref, computed, onMounted } from 'vue'
import MemberCard from '../components/MemberCard.vue'

const members = ref([])

onMounted(async () => {
  try {
    members.value = await fetch('http://localhost:8000/api/members').then(r => r.json())
  } catch {
    members.value = [
      { id: 1, role: 'PROFESSOR', name: '長谷川 〇〇', research: '研究テーマがここに入ります。' },
      ...Array.from({ length: 5 }, (_, i) => ({
        id: i + 2, role: 'STUDENT', name: 'メンバー名', research: '研究テーマがここに入ります。',
      })),
    ]
  }
})

const professor = computed(() => members.value.filter(m => m.role === 'PROFESSOR'))
const students = computed(() => members.value.filter(m => m.role !== 'PROFESSOR'))
</script>

<template>
  <div>
    <section class="page-header">
      <div class="container">
        <span class="label">MEMBERS</span>
        <h1 class="page-title">メンバー</h1>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <p class="section-title">Faculty</p>
        <MemberCard v-for="m in professor" :key="m.id" :member="m" />
      </div>
    </section>

    <section class="section section--gray">
      <div class="container">
        <p class="section-title">Students</p>
        <MemberCard v-for="m in students" :key="m.id" :member="m" />
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
.section--gray { background: #f8f8f8; }
</style>
