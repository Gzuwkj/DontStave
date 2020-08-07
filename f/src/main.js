// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from "./store";
import './icons'
import * as filters from './filters'
import './permissions'
import vueAxios from "vue-axios";
import axios from "axios";


Vue.config.productionTip = false;
Vue.use(vueAxios, axios);
/*router.beforeEach((to, from, next) => {
  let params = to.params;
  to.meta.path = to.meta.reg_path;
  for(let key in params){
    to.meta.path = to.meta.path.replace(':'+key, params[key]);
  }
  next();
});*/
Object.keys(filters).forEach(key => Vue.filter(key, filters[key]));

new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',
});

import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min'
import 'animate.css'
