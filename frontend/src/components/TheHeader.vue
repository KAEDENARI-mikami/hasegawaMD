<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'

const menuOpen = ref(false)

const navLinks = [
  { name: 'Home', to: '/' },
  { name: 'About', to: '/about' },
  { name: 'Results', to: '/results' },
  { name: 'Members', to: '/members' },
  { name: 'News', to: '/news' },
]
</script>

<template>
  <header class="header">
    <div class="header-inner container">
      <RouterLink to="/" class="site-title">HASEGAWA LAB</RouterLink>

      <nav class="nav-desktop">
        <RouterLink
          v-for="link in navLinks"
          :key="link.to"
          :to="link.to"
          class="nav-link"
        >{{ link.name }}</RouterLink>
      </nav>

      <button class="menu-btn" @click="menuOpen = !menuOpen" aria-label="メニュー">
        <span class="menu-btn-label">{{ menuOpen ? 'CLOSE' : 'MENU' }}</span>
      </button>
    </div>

    <nav v-if="menuOpen" class="nav-mobile">
      <RouterLink
        v-for="link in navLinks"
        :key="link.to"
        :to="link.to"
        class="nav-mobile-link"
        @click="menuOpen = false"
      >{{ link.name }}</RouterLink>
    </nav>
  </header>
</template>

<style scoped>
.header {
  background: #000;
  position: sticky;
  top: 0;
  z-index: 100;
}

.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 56px;
}

.site-title {
  font-family: "Courier New", Courier, monospace;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.15em;
  color: #fff;
}

.nav-desktop {
  display: none;
  gap: 32px;
}

.nav-link {
  font-family: "Courier New", Courier, monospace;
  font-size: 11px;
  letter-spacing: 0.083em;
  color: #e5e5e5;
  text-transform: uppercase;
  transition: color 0.2s;
}

.nav-link:hover,
.nav-link.router-link-active {
  color: #fff;
}

.menu-btn {
  background: transparent;
  border: none;
  cursor: pointer;
}

.menu-btn-label {
  font-family: "Courier New", Courier, monospace;
  font-size: 12px;
  font-weight: 700;
  color: #fff;
  letter-spacing: 0.05em;
}

.nav-mobile {
  background: #000;
  display: flex;
  flex-direction: column;
  border-top: 1px solid #333;
}

.nav-mobile-link {
  font-family: "Courier New", Courier, monospace;
  font-size: 12px;
  letter-spacing: 0.083em;
  color: #e5e5e5;
  text-transform: uppercase;
  padding: 16px 24px;
  border-bottom: 1px solid #222;
  transition: color 0.2s;
}

.nav-mobile-link:hover {
  color: #fff;
}

@media (min-width: 768px) {
  .nav-desktop { display: flex; }
  .menu-btn { display: none; }
  .nav-mobile { display: none !important; }
}
</style>
