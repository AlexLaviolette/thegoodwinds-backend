<template>
  <div :class="['chunk', 'weather-rating-' + chunk.weather_rating]"  :style="{height: (chunk.size / 24 * 100) + '%'}">
    <div class="content">
      <div class="text">
        <p class="temp">{{ chunk.temp }}<sups>°C</sups></p>
        <p class="wind-pop">({{ chunk.wind_kmh }} km/h, {{ chunk.pop }}%)</p>
      </div>
      <img class="weather-icon" :src="'http://openweathermap.org/img/wn/' + chunk.icon + '@2x.png'">
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
