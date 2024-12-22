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

const vuetify = createVuetify({
  components,
  directives,
})

const pinia = createPinia()
pinia.use(piniaPersistedState)

createApp(App)
  .use(pinia)
  .use(router)
  .use(vuetify)
  .mount('#app')
