<template>
  <aside class="w-64 h-screen bg-gray-800 text-white flex flex-col">
    <div class="text-2xl font-bold p-4 border-b border-gray-700">Middleware</div>
    <nav class="flex-1">
      <ul>
        <li v-for="item in menu" :key="item.name" class="hover:bg-gray-700">
          <router-link :to="item.route" class="block px-4 py-2">{{ item.name }}</router-link>
        </li>
      </ul>
    </nav>
  </aside>
</template>

<script>
export default {
  name: "Sidebar",
  data() {
    return {
      menu: [
        { name: "Dashboard", route: "/" },
        { name: "Apache", route: "/apache" },
        { name: "Nginx", route: "/nginx" },
        { name: "Tomcat", route: "/tomcat" },
        { name: "JBoss", route: "/jboss" },
        { name: "WebLogic", route: "/weblogic" },
        { name: "WAS", route: "/was" }
      ]
    };
  }
};
</script>
