<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col">
        <h1>When Can I Play Disc Golf?</h1>
        <hr><br><br>
        <h2>Current Weather:</h2>
        <!-- <p> {{ weather.current.temp}} C, {{ weather.current.wind_kmh }} km/h</p> -->
        <br><br>
        <chunked-weather></chunked-weather>
        <br><br>
        <hourly-weather></hourly-weather>
      </div>
    </div>
  </div>
</template>

<script>
import chunkedWeather from './chunkedWeather.vue';
import hourlyWeather from './hourlyWeather.vue';

export default {
  components: {
    'chunked-weather': chunkedWeather,
    'hourly-weather': hourlyWeather,
  },
};
</script>

<style>

  .weather-rating-1 {
    background-color: #93d5f2;
  }
  .weather-rating-2 {
    background-color: #DCEAF1;
  }
  .weather-rating-3 {
    background-color: #DDECEA;
  }
  .weather-rating-4 {
    background-color: #FBF3DA;
  }
  .weather-rating-5 {
    background-color: #F9EADD;
  }
  .weather-rating-6 {
    background-color: #FAE4E3;
  }

  div.container-fluid {
    padding: 0 180px;
  }

  div.col.time {
    margin-top: 68px;
    max-width: fit-content;
    color: #70757a;
    font-size: 10px;
    text-align: right;
    padding: 0px;
  }

  div.cell {
    padding: 0px;
    /*border-top: #dadce0 1px solid;*/
  }

  p.inner-cell {
    margin: 0 5px;
    height: 24px;
  }

  div.col {
    padding: 0px;
  }
  div.today {
    color: #1a73e8;
  }
  div.date-header {
    text-align: center;
  }
</style>
