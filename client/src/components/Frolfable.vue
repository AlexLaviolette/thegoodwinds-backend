<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col">
        <h1>When Can I Play Disc Golf?</h1>
        <hr><br><br>
        <h2>Current Status:</h2>
        <p> {{ weather.current.temp}} C, {{ weather.current.wind_kmh }} km/h</p>
        <br><br>
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
                <p :class="'weather-rating-' + chunk.weather_rating" class="inner-cell">
                  {{ chunk.temp }} C, {{ chunk.wind_kmh }} km/h, {{ chunk.pop * 100 }}%
                </p>
              </div>
              <div v-for="n in chunk.size-1" :key="n" class="cell">
                <p :class="'weather-rating-' + chunk.weather_rating" class="inner-cell">
                </p>
              </div>
            </span>
          </div>
        </div>
        <br><br>
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
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      weather: {},
    };
  },
  methods: {
    getWeather() {
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
    this.getWeather();
  },
};
</script>

<style scoped>

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
