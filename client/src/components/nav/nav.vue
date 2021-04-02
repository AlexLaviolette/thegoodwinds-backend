<template>
  <div id="nav">
    <div class="title">
      <h1>GoodWinds</h1>
      <p>The Disc-Golf weather app.</p>
    </div>
    <router-link class="btn" :to="{name: 'location'}">Set Location</router-link>
  </div>
</template>

<script>

export default {
  name: 'nav-component',
  data() {
    return {
    };
  },
  mounted: function () {
  },
  methods: {
  },
};
</script>


<style scoped src="./nav.styl" lang="stylus"></style>