<template>
  <div id="overlay" v-if="visible">
    <div class="shade" @click="goHome()"></div>
    <div class="content">
      <router-link :to="{name: 'home'}" class="close" @click="visible=false" aria-label="close map overlay">×</router-link>
      <slot></slot>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
export default Vue.extend({
  name: 'overlay',
  data() {
    return {
    };
  },
  computed: {
    visible: function () {
      return this.$route.name === 'location'
    }
  },
  methods: {
    goHome: function () {
      this.$router.push({name: 'home'})
    }
  },
  mounted() {
  },
  props: []
});
</script>

<style scoped src="./overlay.styl" lang="stylus"></style>
