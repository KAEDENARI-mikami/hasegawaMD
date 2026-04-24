<template>
  <footer class="footer">
    <div class="container footer-inner">
      <span class="footer-name">HASEGAWA LAB</span>
      <span class="footer-copy">© {{ new Date().getFullYear() }} Hasegawa Laboratory. All rights reserved.</span>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  border-top: 1px solid #e5e5e5;
  padding: 32px 0;
  margin-top: auto;
}

.footer-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 8px;
}

.footer-name {
  font-family: "Courier New", Courier, monospace;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.15em;
  color: #000;
}

.footer-copy {
  font-size: 11px;
  color: #757575;
}
</style>
