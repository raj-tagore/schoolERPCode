<template>
    <div>
      <!-- Tab Buttons -->
      <div class="tabs">
        <button
          v-for="(tab, index) in tabs"
          :key="index"
          :class="{ active: selectedTab === tab }"
          @click="selectedTab = tab"
        >
          {{ tab }} <!-- Display the name of the tab -->
        </button>
      </div>
  
      <!-- Tab Content -->
      <div class="tab-content">
        <slot :name="selectedTab"></slot> <!-- Render the content of the selected tab using a named slot -->
      </div>
    </div>
  </template>

<script>
export default {
  data() {
    return {
      selectedTab: "", // Holds the currently selected tab name
    };
  },
  props: {
    tabs: {
      type: Array, // Expects an array of tab names to be passed from the parent component
      required: true, // Makes the `tabs` prop mandatory
    },
  },
  mounted() {
    if (this.tabs.length > 0) {
      this.selectedTab = this.tabs[0]; // Sets the default selected tab to the first one in the array
    }
  },
};
</script>

<style>
.tabs button.active {
  font-weight: bold; /* Highlights the active tab button */
  border-bottom: 2px solid black; /* Adds an underline to the active tab */
}
</style>
  