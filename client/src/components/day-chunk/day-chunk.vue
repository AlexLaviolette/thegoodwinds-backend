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

        <p v-if="units == 'imperial'" class="temp">{{ Math.round((chunk.temp * 9/5) + 32) }}<sup>°F</sup></p>
        <p v-else class="temp">{{ chunk.temp }}<sup>°C</sup></p>

        <p v-if="units == 'imperial'" class="wind-pop">{{ Math.round(chunk.wind_kmh / 1.609) }} mph</p>
        <p v-else class="wind-pop">{{ chunk.wind_kmh }} km/h</p>
      </div>

      <div class="hour">
        <!-- Chunk spans am-pm -->
        <p v-if="(chunk.size > 1 && chunk.start < 12 && chunk.start + chunk.size > 12) || (chunk.size > 1 && chunk.start + chunk.size == 24)">
          {{ today.setHours(chunk.start) | moment("ha") }}
          –
          {{ today.setHours(chunk.start + chunk.size) | moment("ha") }}
        </p>
        <!-- Chunk only exists in am or pm -->
        <p v-else-if="chunk.size > 1">
          {{ today.setHours(chunk.start) | moment("h") }}
          –
          {{ today.setHours(chunk.start + chunk.size) | moment("ha") }}
        </p>
        <!-- Single hour chunk -->
        <p v-else>
          {{ today.setHours(chunk.start) | moment("ha") }}
        </p>
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
      today: new Date(),
      units: 'metric'
    };
  },
  mounted() {
    if (localStorage.units) {
      this.units = localStorage.units
    }
  },
  props: ['chunk']
});
</script>

<style src="./day-chunk.styl" lang="stylus"></style>
