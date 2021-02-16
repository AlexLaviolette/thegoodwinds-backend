import Vue from 'vue';
import VueRouter from 'vue-router';
import home from '../views/home/home.vue';
import location from '../views/location/location.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: home,
  },
  {
    path: '/location',
    name: 'location',
    component: location,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior() {
    return { x: 0, y: 0 };
  },
});

export default router;
