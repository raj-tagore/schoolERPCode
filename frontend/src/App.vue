<template>
  <header>
    <div class="container">
      <span>The App</span>
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
	<a class="secondary" id="sidebarOpener" :class="{shown: !isSidebarOpen}" @click="isSidebarOpen = true" href="#">Table of Contents</a>
	<aside class="container" id="table-of-contents" :class="{open: isSidebarOpen}">
      <header>
          <h2>Table of Contents</h2>
          <a class="secondary" @click="isSidebarOpen = false" href="#">Close</a>
      </header>
      <nav>
        <ul>
          <li v-for="item in tableOfContents" :key="item.id">
			<a class="secondary" :href="'#' + item.id">{{ item.text }}</a>
          </li>
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

.container:has(#table-of-contents) > a {
  display: none;
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
	left: -100%;
    width: 100%;
    height: 100%;
    padding: 20px;
    transition: left 0.5s ease-in-out;
    box-shadow: rgba(0, 0, 0, 0.1) 15px 0px 40px -3px
  }

  main > #table-of-contents.open {
    left: 0;
  }

  #table-of-contents > header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  #table-of-contents > header > h2 {
    display: block;
  }

  .container:has(#table-of-contents) > a {
    display: block;
  }
}


</style>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
}
</script>
<script setup>
import {ref, onMounted} from "vue";

const isSidebarOpen = ref(false)

const tableOfContents = ref([]);

onMounted(() => {
  generateTableOfContents();
	console.log("Mounted")
});

function generateTableOfContents() {
	console.log("Generating Table of Contents")
  const headings = document.getElementById("content").querySelectorAll('h1, h2, h3, h4, h5, h6');
	console.log(headings);
  
  // Map headings into a structured array
	tableOfContents.value = Array.from(headings).map((heading) => {
		let textContent = heading.textContent;
		if (textContent.length > 15) {
			textContent = textContent.substring(0, 15) + "...";
		}
		return {
		id: heading.id || generateId(heading.textContent), // Use existing ID or generate one
		text: textContent,
		level: heading.tagName.toLowerCase(), // h1, h2, etc.
	}
	});

  headings.forEach((heading) => {
    if (!heading.id) heading.id = generateId(heading.textContent);
  });
}

function generateId(text) {
  return text.toLowerCase().replace(/\s+/g, '-').replace(/[^\w-]/g, '');
}


</script>
