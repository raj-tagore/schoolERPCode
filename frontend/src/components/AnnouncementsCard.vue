<template>
  <DataCard title="Announcements">
    <template #content>
      <div v-if="announcements && announcements.length">
        <ul>
          <li v-for="announcement in announcements" :key="announcement.id" class="mb-2">
            <strong>{{ announcement.title }}</strong>
            <br />
            {{ announcement.description }}
            <br />
            <small>Priority: {{ announcement.priority }}</small>
            <br />
            <small>Release At: {{ formatDate(announcement.release_at) }}</small>
          </li>
        </ul>
      </div>
      <div v-else>
        No announcements available.
      </div>
    </template>
  </DataCard>
</template>
  
<script>
import DataCard from './DataCard.vue'

export default {
  components: {
    DataCard
  },
  props: {
    announcements: {
      type: Array,
      default: () => []
    }
  },
  methods: {
    formatDate(dateString) {
      if (!dateString) return ''
      const date = new Date(dateString)
      return date.toLocaleString()
    }
  }
}
</script>
  