/**
 * 权限判定
 */

import router from './router'
import store from "./store";
import {getToken, checkToken} from "./utils/auth";
import {deepSearch} from "./utils/utils";
import getPageTitle from "./utils/getPageTitle";

const login = deepSearch(router.options.routes, i => i.name === 'login');
const register = deepSearch(router.options.routes, i => i.name === 'register')

const deepFilter = function(arr, pre){
  let ret = [];
  for(let i of arr.values()){
    if(i)
      if(!i.hasOwnProperty('meta') || !i.meta.hasOwnProperty('allowAnonymous') || i.meta.allowAnonymous){
        ret.push(pre+i.path);
      }
    if(i && i.hasOwnProperty('children')){
      ret = ret.concat(deepFilter(i.children, pre + i.path))
    }

  }
  return ret;
};
const whitelist = deepFilter(router.options.routes, ''); // 白名单

router.beforeEach(async(to, from, next) => {
  document.title = getPageTitle(to.meta.title);
  const token = getToken();
  if (token && await checkToken()) {
    const path = to.fullPath.replace(/\?.*/, '');
    if (path === login || path === register) {
      next({ path: '/' })
    }
    else {
      const hasRoles = store.getters.roles && store.getters.roles.length > 0;
      if (true) {
        next()
      }
      else {
        try {
          next({ path:  login, replace: true })
        } catch (error) {
          await store.dispatch('user/resetToken');
          next(`${ login }?redirect=${path}`);
        }
      }
    }
  }
  else {
    if (whitelist.indexOf(to.fullPath.replace(/\?.*/, '')) !== -1) {
      next()
    }
    else {
      next(`${login}?redirect=${to.fullPath.replace(/\?.*/, '')}`)
    }
  }
});
