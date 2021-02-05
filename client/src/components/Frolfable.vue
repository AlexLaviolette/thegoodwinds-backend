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
          <div class="col day" v-for="(hourly, date, index) in weather.data" :key="index">
            <div class="date-header" :class="{ 'today' : index == 0 }">
              <h4>{{ date | moment("ddd")}}</h4>
              <h5>{{ date | moment("D")}}</h5>
            </div>
            <div v-for="(hourly_weather, index) in hourly" :key="index" class="cell">
              <p :class="hourly_weather.colour" class="inner-cell">
              {{ hourly_weather.temp}} C, {{ hourly_weather.wind_kmh }} km/h, {{ hourly_weather.pop * 100 }}%
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
      const path = 'http://localhost:5000/weather';
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
    this.getWeather();
  },
};
</script>

<style scoped>

  .indigo {
    background-color: #93d5f2;
  }
  .blue {
    background-color: #DCEAF1;
  }
  .green {
    background-color: #DDECEA;
  }
  .yellow {
    background-color: #FBF3DA;
  }
  .orange {
    background-color: #F9EADD;
  }
  .red {
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
