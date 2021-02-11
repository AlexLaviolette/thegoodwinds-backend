<template>
  <div class="days-column"> <!--:class="'weather-rating-' + chunk.weather_rating"-->
    <div class="date-header">
      <p class="day">{{ date | moment("ddd")}}</p>
      <p class="date">{{ date | moment("D")}}</p>
    </div>
    <div class="days">
      <slot></slot>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';

export default Vue.extend({
  name: 'days-column',
  data() {
    return {
    };
  },
  props: ['date']
});
</script>

<style src="./days-column.styl" lang="stylus"></style>
