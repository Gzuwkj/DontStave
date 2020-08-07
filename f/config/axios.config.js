'use strict';



import axios from 'axios';
import Vue from "vue";
import vueAxios from "vue-axios";

axios.defaults.baseURL='http://192.168.0.105:8000/api/';
if(window.localStorage.token || window.sessionStorage.token)
  axios.defaults.headers.common['Authorization'] = 'JWT ' + window.localStorage.token || window.sessionStorage.token;
Vue.use(vueAxios, axios);
