<style lang="scss">
@import "@/assets/scss/main.scss";
</style>

<template>
	<header>
		<div class="container">
			<spam>The App</spam>
	<nav>
      <ul>
        <li><a class="secondary" href="#">About</a></li>
          <li><a class="secondary" href="#">Services</a></li>
          <li><a class="secondary" href="#">Products</a></li>
			</ul>
		</nav></div>
</header>
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

header > .container {
	display: flex;
	justify-content: space-between;
	align-items: center;
	flex-direction: row;
}

@media (max-width: 1023px) {
  main {
    grid-template-columns: 10.5rem 1fr;
  }
}
</style>

<script>
export default {
  name: 'App',
}
</script>
