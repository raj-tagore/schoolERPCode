<style lang="scss">
@import "@/assets/scss/main.scss";
</style>

<template>
  <main class="container">
    <aside>
      <nav>
        <ul>
          <li><a class="secondary" href="#">About</a></li>
          <li><a class="secondary" href="#">Services</a></li>
          <li><a class="secondary" href="#">Products</a></li>
        </ul>
      </nav>
    </aside>
	<div id="content" role="document">
      <router-view></router-view>
    </div>
  </main>
</template>

<style>
main {
  grid-template-rows: auto 1fr;
  grid-template-columns: 10.5rem 1fr 10.5rem;
  display: grid;
  grid-template-areas:
    "menu header table-of-content" 
    "menu body   table-of-content";
}
</style>

<script>
export default {
  name: 'App',
}
</script>
