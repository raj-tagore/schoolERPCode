import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import piniaPersistedState from 'pinia-plugin-persistedstate'

// Import Vuetify and its styles
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

// If you want to use mdi icons:
import '@mdi/font/css/materialdesignicons.css'

import { VDateInput } from 'vuetify/labs/VDateInput'

const vuetify = createVuetify({
  components: {...components, VDateInput },
  directives,
  theme: {
    defaultTheme: 'light', // Set 'light' as the default theme, or 'dark' if preferred
    themes: {
      light: {
        colors: {
          primary: '#6A1B9A',  // Deep Purple
          secondary: '#7B1FA2', // Purple
          accent: '#D500F9',    // Neon Purple
          background: '#F5F5F5', // Soft Grey
          surface: '#FFFFFF',    // White
          error: '#E53935',      // Red
          info: '#1E88E5',       // Blue
          success: '#43A047',    // Green
          warning: '#FB8C00',    // Orange
        },
      },
      dark: {
        colors: {
          primary: '#9C27B0',   // Lighter Purple
          secondary: '#512DA8', // Dark Indigo
          accent: '#FF4081',    // Neon Pink
          background: '#121212', // Deep Black
          surface: '#1E1E1E',    // Dark Grey
          error: '#CF6679',      // Soft Red
          info: '#64B5F6',       // Soft Blue
          success: '#66BB6A',    // Soft Green
          warning: '#FFB74D',    // Soft Orange
        },
      },
    },
  },
})

const pinia = createPinia()
pinia.use(piniaPersistedState)

createApp(App)
  .use(pinia)
  .use(router)
  .use(vuetify)
  .mount('#app')
