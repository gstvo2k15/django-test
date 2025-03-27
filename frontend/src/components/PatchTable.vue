<template>
  <div class="overflow-x-auto">
    <table class="min-w-full bg-white rounded-lg">
      <thead>
        <tr>
          <th class="px-4 py-2 text-left">Host</th>
          <th class="px-4 py-2 text-left">Version</th>
          <th class="px-4 py-2 text-left">Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="patch in patches" :key="patch.host" class="border-t">
          <td class="px-4 py-2">{{ patch.host }}</td>
          <td class="px-4 py-2">{{ patch.version }}</td>
          <td class="px-4 py-2">
            <button @click="$emit('execute', patch)" class="bg-blue-600 text-white px-3 py-1 rounded">Ejecutar parches</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "PatchTable",
  props: {
    patches: Array
  }
};
</script>
