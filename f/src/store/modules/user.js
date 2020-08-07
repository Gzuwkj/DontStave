import { getToken, setToken, removeToken } from '../../utils/auth'
import { login ,  register} from "../../api/user";

const Anonymous = {
  id: -1,
  username: 'Anonymous',
};

const state = {
  token: getToken(),
  user: Anonymous,
  roles: [],
};

const mutations = {
  SET_TOKEN: (state, token) => state.token = token,
  SET_USER: (state, user) => state.user = user,
  SET_ROLES: (state, roles) => state.roles = roles
};


const actions = {
  login({ commit }, userInfo){
    const { username, password } = userInfo;
    return new Promise((resolve, reject) => {
      login({ username: username.trim(), password: password }).then(response => {
        if (!response) {
          reject('Verification failed, please Login again.')
        }
        const { token, roles, user } = response;
        // if (!roles || roles.length <= 0) {
        //   reject('getInfo: roles must be a non-null array!')
        // }
        commit('SET_ROLES', roles);
        commit('SET_USER', user);
        commit('SET_TOKEN', token);
        setToken(token);
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  /*getInfo({ commit, state }) {
    return new Promise((resolve, reject) => {
      getInfo(state.token).then(response => {
        const { data } = response;
        if (!data) {
          reject('Verification failed, please Login again.')
        }
        const { roles, user } = data;
        // roles must be a non-empty array
        if (!roles || roles.length <= 0) {
          reject('getInfo: roles must be a non-null array!')
        }
        commit('SET_ROLES', roles);
        commit('SET_USER', user);
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },*/

  // user logout
  logout({ commit }) {
    commit('SET_TOKEN', '');
    commit('SET_USER', Anonymous);
    commit('SET_ROLES', []);
    removeToken();
  },
  register({ commit }, userInfo){
    const { username, password, repassword } = userInfo;
    return new Promise((resolve, reject) => {
      register({ username: username.trim(), password , repassword}).then(response => {
        const { data } = response;
        if (!data) {
          reject('Verification failed, please Register again.')
        }
        // const { token, roles, user } = data;
        // if (!roles || roles.length <= 0) {
        //   reject('getInfo: roles must be a non-null array!')
        // }
        // commit('SET_ROLES', roles);
        // commit('SET_USER', user);
        // commit('SET_TOKEN', token);
        // setToken(token);
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },
  resetToken({ commit }) {
    return new Promise(resolve => {
      commit('SET_TOKEN', '');
      commit('SET_ROLES', []);
      commit('SET_USER', Anonymous);
      removeToken();
      resolve();
    })
  },
};

export default {
  namespaced: true,
  state,
  mutations,
  actions
};

