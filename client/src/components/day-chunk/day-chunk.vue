<template>
  <div
    :class="[
      'chunk',
      'weather-rating-' + chunk.weather_rating, chunk.size > 2 ? 'large-content' : '',
      chunk.size > 3 && chunk.weather_rating === 1 ? 'extra-special': ''
    ]"
    :style="{height: (chunk.size / 24 * 100) + '%'}">
    <div class="content">
      <!-- <img class="weather-icon" :src="'http://openweathermap.org/img/wn/' + chunk.icon + '@2x.png'"> -->
      <img class="weather-icon" :src="require('./weather/' + chunk.icon + '.svg')">
      <div class="text">
        <p class="temp">{{ chunk.temp }}<sup>°C</sup></p>
        <p class="wind-pop">{{ chunk.wind_kmh }}km/h, {{ chunk.pop }}%</p>
      </div>
    </div>
    <!-- <div :style="{height: ((chunk.size-1) * 35) + 'px'}" class="cell"></div> -->
  </div>
</template>

<script>
import Vue from 'vue';
export default Vue.extend({
  name: 'day-chunk',
  data() {
    return {
    };
  },
  props: ['chunk']
});
</script>

<style src="./day-chunk.styl" lang="stylus"></style>
