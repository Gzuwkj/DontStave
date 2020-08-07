import router from '../../router';
import {deepFilter} from "../../utils/utils";

const state = {
  routes: router.options.routes.filter(item => item && item.meta && !item.meta.hidden),
};

const mutations = {
  SET_ROUTES: (state, routes) => {
    state.routes = routes;
  }
};

const actions = {

};

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
