<template>
  <div class="flex h-screen">
    <Sidebar />
    <main class="flex-1 bg-gray-100 p-4 overflow-y-auto">
      <router-view />
    </main>
  </div>
</template>

<script>
import Sidebar from './components/Sidebar.vue'

export default {
  name: 'App',
  components: {
    Sidebar
  }
}
</script>
