import axios from 'axios'
import store from '@/store'
import { getToken } from './auth'
const config = require('@/settings');


// create an axios instance
const service = axios.create({
  baseURL: config.baseURL, // url = base url + request url
  // withCredentials: true, // send cookies when cross-domain requests
  timeout: 5000 // request timeout
});

// request interceptor
service.interceptors.request.use(
  config => {
    if (store.getters.token) {
      config.headers['Authorization'] = 'JWT ' + getToken()
    }
    return config;
  },
  error => {
    console.log(error);
    return Promise.reject(error);
  }
);

// response interceptor
service.interceptors.response.use(
  response => {
    const { status, data } = response;
    // if the custom code is not 20000, it is judged as an error.
    if(status !== 200){
      if(status === 401){
        //....
      }
      return Promise.reject(data.msg || 'Error')
    }
    return data;
  },
  error => {
    console.log('err' + error);// for debug
    return Promise.reject(error);
  }
);

export default service
