<template>
  <div class="days-column">
    <div class="date-header">
      <p class="day">{{ date | moment("ddd")}}</p>
      <p class="date">{{ date | moment("D")}}</p>
    </div>
    <div class="days">
      <!-- <div class="hours">
        <div v-for="n in 24" v-bind:key="n" class="hour">
          <p>
            {{ today.setHours(n-1) | moment("hA") }}
          </p>
        </div>
      </div>
 -->      <slot></slot>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';

export default Vue.extend({
  name: 'days-column',
  data() {
    return {
      today: new Date()
    };
  },
  props: ['date']
});
</script>

<style src="./days-column.styl" lang="stylus"></style>
