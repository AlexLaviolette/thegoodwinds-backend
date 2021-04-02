<template>
  <div v-cloak id="app">
    <nav-component></nav-component>
    <router-view/>
  </div>
</template>

<script>
import nav from '@/components/nav/nav.vue';

export default {
  components: {
    'nav-component': nav
  },
};
</script>

<style src="@/styles/main.styl" lang="stylus"></style>
