<template>
  <div>
    <div>
      <GChart :type="typeOne" :data="data" :options="options" />
    </div>
  </div>
</template>

<script>
export default {
  name: 'GraphCard',
  props: ['typeOne', 'data', 'options'],
};
</script>

<style>
</style>