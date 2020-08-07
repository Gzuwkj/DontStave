import request from '../utils/request'
import router from'../router'
import { deepSearch } from "../utils/utils";

let t;

export function login(data) {
  return request({
    url: (t = deepSearch(router.options.routes, item => item.name === 'login')) ? t : '/user/login',
    method: 'post',
    data
  })
}

export function getInfo(token) {
  return request({
    url: '/vue-element-admin/user/info',
    method: 'get',
    params: { token }
  })
}

export function logout() {
  return request({
    url: '/vue-element-admin/user/logout',
    method: 'post'
  })
}

export function register(data) {
  return request({
    url: (t = deepSearch(router.options.routes, item => item.name === 'register')) ? t : '/user/register',
    method: 'post',
    data
  })
}

export function authenticate() {
  return request({
    url: '/user/authenticate',
    method: 'get',
  })
}
