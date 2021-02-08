<template>
  <div class="row">
    <div class="col time">
      <div v-for="n in 24" v-bind:key="n" class="cell">
        <p class="inner-cell">
        {{ new Date().setHours(n-1) | moment("h A") }}
        </p>
      </div>
    </div>
    <div class="col day" v-for="(hourly, date, index) in weather.data" :key="index">
      <div class="date-header" :class="{ 'today' : index == 0 }">
        <h4>{{ date | moment("ddd")}}</h4>
        <h5>{{ date | moment("D")}}</h5>
      </div>
      <div v-for="(hourly_weather, index) in hourly" :key="index" class="cell">
        <p :class="'weather-rating-' + hourly_weather.weather_rating" class="inner-cell">
        {{ hourly_weather.temp }} C, {{ hourly_weather.wind_kmh }} km/h, {{ hourly_weather.pop * 100 }}%
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
import axios from 'axios';

export default Vue.extend({
  name: 'hourlyWeather',
  data() {
    return {
      weather: {},
    };
  },
  methods: {
    getHourly() {
      const path = 'http://localhost:5000/weather/hourly';
      axios.get(path)
        .then((res) => {
          this.weather = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getHourly();
  },
});
</script>
