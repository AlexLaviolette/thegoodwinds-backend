<template>
  <div>
    <!-- <current-weather></current-weather> -->
    <days-grid></days-grid>
  </div>
</template>

<script>
import daysGrid from '@/components/days-grid/days-grid.vue';

export default {
  components: {
    'days-grid': daysGrid,
  },
};
</script>

<style src="./home.styl" lang="stylus"></style>
