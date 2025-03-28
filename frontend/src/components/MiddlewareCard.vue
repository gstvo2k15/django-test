<template>
  <div class="bg-white rounded-lg shadow p-4">
    <h2 class="text-lg font-bold">{{ title }}</h2>
    <p class="text-3xl">{{ count }}</p>
    <p class="text-sm text-gray-600">Pending Updates</p>
  </div>
</template>

<script>
export default {
  name: "MiddlewareCard",
  props: {
    title: String,
    count: Number
  }
};
</script>
