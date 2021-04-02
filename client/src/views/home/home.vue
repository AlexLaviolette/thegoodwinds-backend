<template>
  <div>
    <days-grid ref="days"></days-grid>
    <overlay>
      <map-component @setLocation="$refs.days.getLocation()"></map-component>
    </overlay>
  </div>
</template>

<script>
import daysGrid from '@/components/days-grid/days-grid.vue';
import overlay from '@/components/overlay/overlay.vue';
import map from '@/components/map/map.vue';

export default {
  components: {
    'days-grid': daysGrid,
    'overlay': overlay,
    'map-component': map,
  },
};
</script>

<style src="./home.styl" lang="stylus"></style>
