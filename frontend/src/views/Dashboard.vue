<template>
  <div class="space-y-4">
    <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
      <MiddlewareCard title="Apache" :count="3" />
      <MiddlewareCard title="Nginx" :count="2" />
      <MiddlewareCard title="Tomcat" :count="2" />
      <MiddlewareCard title="WAS" :count="4" />
    </div>

    <h2 class="text-xl font-bold mt-6">Pending Patches</h2>
    <PatchTable :patches="patches" @execute="runPatch" />
  </div>
</template>

<script>
import MiddlewareCard from '../components/MiddlewareCard.vue'
import PatchTable from '../components/PatchTable.vue'

export default {
  name: "Dashboard",
  components: { MiddlewareCard, PatchTable },
  data() {
    return {
      patches: [
        { host: 'host1.example.com', version: '2.4.54' },
        { host: 'host2.example.com', version: '2.4.51' },
        { host: 'host3.example.com', version: '2.4.46' }
      ]
    };
  },
  methods: {
    runPatch(patch) {
      alert(`Applying patchs for ${patch.host}`);
    }
  }
};
</script>
