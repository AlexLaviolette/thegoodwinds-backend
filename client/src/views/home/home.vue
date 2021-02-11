<template>
  <div>
    <current-weather></current-weather>
    <days-grid></days-grid>
    <!--div class="container-fluid">
      <div class="row">
        <div class="col">
          <br><br>
          <chunked-weather></chunked-weather>
          <br><br>
          <hourly-weather></hourly-weather>
        </div>
      </div>
    </div-->
  </div>
</template>

<script>
// import currentWeather from '@/components/currentWeather/currentWeather.vue';
// import chunkedWeather from '@/components/chunkedWeather/chunkedWeather.vue';

import daysGrid from '@/components/days-grid/days-grid.vue';
// import hourlyWeather from '@/components/hourlyWeather/hourlyWeather.vue';

export default {
  components: {
    'days-grid': daysGrid,
    // 'current-weather': currentWeather,
    // 'chunked-weather': chunkedWeather,
    // 'hourly-weather': hourlyWeather,
  },
};
</script>

<style src="./home.styl" lang="stylus"></style>
