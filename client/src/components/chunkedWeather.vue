<template>
  <div class="row">
    <div class="col time">
      <div v-for="n in 24" v-bind:key="n" class="cell">
        <p class="inner-cell">
        {{ new Date().setHours(n-1) | moment("h A") }}
        </p>
      </div>
    </div>
    <div class="col day" v-for="(chunks, date, index) in chunked" :key="index">
      <div class="date-header" :class="{ 'today' : index == 0 }">
        <h4>{{ date | moment("ddd")}}</h4>
        <h5>{{ date | moment("D")}}</h5>
      </div>
      <span v-for="(chunk, index) in chunks" :key="index">
        <!-- Create the hourly cells. Only the first one of the chunk contains weather information. -->
        <div class="cell">
          <p :class="'weather-rating-' + chunk.weather_rating + ' icon-' + chunk.icon" class="inner-cell">
            <img class="weather-icon" :src="'http://openweathermap.org/img/wn/' + chunk.icon + '@2x.png'">
            {{ chunk.temp }} C, {{ chunk.wind_kmh }} km/h, {{ chunk.pop }}%
          </p>
        </div>
        <div v-for="n in chunk.size-1" :key="n" class="cell">
          <p :class="'weather-rating-' + chunk.weather_rating" class="inner-cell">
          </p>
        </div>
      </span>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
import axios from 'axios';

export default Vue.extend({
  name: 'chunkedWeather',
  data() {
    return {
      chunked: {},
    };
  },
  methods: {
    getChunks() {
      const path = 'http://localhost:5000/weather/chunked';
      axios.get(path)
        .then((res) => {
          this.chunked = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getChunks();
  },
});
</script>
