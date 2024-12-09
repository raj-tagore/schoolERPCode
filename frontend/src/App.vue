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
      </nav>
    </div>
  </header>
  <main class="container">
    <aside class="container" id="table-of-contents">
      <header>
          <h2>Table of Contents</h2>
          <a class="secondary" href="#">Close</a>
      </header>
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
  grid-template-columns: 10.5rem 1fr;
  display: grid;
}

header > .container {
	display: flex;
	justify-content: space-between;
	align-items: center;
	flex-direction: row;
}

#table-of-contents > header {
  display: none;
  justify-content: space-between;
  align-items: center;
}

@media (max-width: 1023px) {
  main {
    grid-template-columns: 1fr;
  }
  main > #table-of-contents {
    background-color: var(--pico-background-color);
    padding-top: 30px;
    position: fixed;
	top: 0%;
	left: 0%;
    width: 100%;
    height: 100%;
  }

  #table-of-contents > header > h2 {
    display: block;
  }
}

</style>

<script>
export default {
  name: 'App',
}
</script>
