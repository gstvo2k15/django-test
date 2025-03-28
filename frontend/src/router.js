import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from './views/Dashboard.vue'

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
