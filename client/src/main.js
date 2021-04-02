import Vue from 'vue';
import axios from 'axios';
import App from './App.vue';
import router from './router';
import store from './store';
// import VueGtm from "vue-gtm";

Vue.prototype.$axios = axios;
Vue.config.productionTip = false;

Vue.use(require('vue-moment'));

// Vue.use(VueGtm, {
//   id: "GTM-xxxxxx", // Your GTM single container ID or array of container ids ['GTM-xxxxxx', 'GTM-yyyyyy'] or array of objects [{id: 'GTM-xxxxxx', queryPararms: { gtm_auth: 'abc123', gtm_preview: 'env-4', gtm_cookies_win: 'x'}}, {id: 'GTM-yyyyyy', queryParams: {gtm_auth: 'abc234', gtm_preview: 'env-5', gtm_cookies_win: 'x'}}]
//   defer: true, // defaults to false. Script can be set to `defer` to increase page-load-time at the cost of less accurate results (in case visitor leaves before script is loaded, which is unlikely but possible)
//   enabled: !location.host.includes('localhost'), // defaults to true. Plugin can be disabled by setting this to false for Ex: enabled: !!GDPR_Cookie (optional)
//   debug: true, // Whether or not display console logs debugs (optional)
//   loadScript: true, // Whether or not to load the GTM Script (Helpful if you are including GTM manually, but need the dataLayer functionality in your components) (optional)
//   vueRouter: router, // Pass the router instance to automatically sync with router (optional)
//   // ignoredViews: ["homepage"], // Don't trigger events for specified router names (case insensitive) (optional)
//   trackOnNextTick: false, // Whether or not call trackView in Vue.nextTick
// });

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
