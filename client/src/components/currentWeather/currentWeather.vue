<template>
  <div>
    <h2>Current Weather:</h2>
    <p>
      <img class="weather-icon" :src="'http://openweathermap.org/img/wn/' + weather.icon + '@2x.png'">
      {{ weather.temp}} C, {{ weather.wind_kmh }} km/h
    </p>
  </div>
</template>

<script>
import Vue from 'vue';

export default Vue.extend({
  name: 'currentWeather',
  data() {
    return {
      weather: {},
    };
  },
  methods: {
    getCurrentWeather() {
      const path = 'http://localhost:5000/weather';
      this.$axios.get(path)
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
    this.getCurrentWeather();
  },
});
</script>
