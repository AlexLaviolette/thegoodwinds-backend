import Vue from 'vue';
import VueRouter from 'vue-router';
import Frolfable from '../components/Frolfable.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Frolfable',
    component: Frolfable,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
