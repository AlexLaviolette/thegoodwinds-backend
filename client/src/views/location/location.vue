<template>
  <div>
    <places-search></places-search>
  </div>
</template>

<script>
import placesSearch from '@/components/places-search/places-search.vue';

export default {
  components: {
    'places-search': placesSearch,
  },
};
</script>

<style src="./location.styl" lang="stylus"></style>
