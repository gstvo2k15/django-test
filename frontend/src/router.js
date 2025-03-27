import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from './views/Dashboard.vue'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/tailwind.css'

createApp(App).use(router).mount('#app')

const routes = [
  { path: '/', component: Dashboard },
  { path: '/apache', component: Dashboard },
  { path: '/nginx', component: Dashboard },
  { path: '/tomcat', component: Dashboard },
  { path: '/jboss', component: Dashboard },
  { path: '/weblogic', component: Dashboard },
  { path: '/was', component: Dashboard }
]

export default createRouter({
  history: createWebHistory(),
  routes,
})
