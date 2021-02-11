<template>
  <div
    :class="['chunk', 'weather-rating-' + chunk.weather_rating, size > 2 ? 'large-content' : '']"
    :style="{height: height + '%'}"
    v-if="height > 0">
    <div class="content" :style="size > 2 ? {fontSize: size * 0.1 + 6 + 'em'} : {}">
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
      height: 0,
      size: this.chunk.size
    };
  },
  props: ['chunk'],
  created: function () {
    if (this.chunk.hour_end < 5) {
      this.height = 0
    } else {
      if (this.chunk.hour_start < 5) {
        this.size = this.chunk.size - (5 - this.chunk.hour_start)
      } else {
        this.size = this.chunk.size
      }
      this.height = this.size / 17 * 100
    }
  }
});
</script>

<style src="./day-chunk.styl" lang="stylus"></style>
