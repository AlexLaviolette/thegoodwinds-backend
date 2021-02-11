import Vue from 'vue';
import axios from 'axios';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.css';

Vue.prototype.$axios = axios;
Vue.config.productionTip = false;

Vue.use(require('vue-moment'));

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
