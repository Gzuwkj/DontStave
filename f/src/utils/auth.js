import { authenticate } from "@/api/user";
import store from "@/store";

const TOKEN = 'JWT token';
export function getToken() {
  return sessionStorage.getItem(TOKEN) || localStorage.getItem(TOKEN)
}

export function setToken(token) {
  sessionStorage.setItem(TOKEN, token);
  localStorage.setItem(TOKEN, token);
}

export function removeToken() {
  sessionStorage.removeItem(TOKEN);
  localStorage.removeItem(TOKEN);
}

export function checkToken() {
  return authenticate().then(response => {
    const { user, status } = response;
    if (status === 200) {
      // if (!roles || roles.length <= 0) {
      //   return false;
      // }
      store.commit('user/SET_USER', user);
      // store.commit('SET_ROLES', roles);
    }
    else if(status === 401) {
      // refresh token
    }
    return true;
  }).catch(error => {
    store.dispatch('user/resetToken');
    console.log(error);
    return false;
  })
}
