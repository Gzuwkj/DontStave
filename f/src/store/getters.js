
const getters = {
  token: state => state.user.token,
  user: state => state.user.user,
  roles: state => state.user.roles,
  routes: state => state.permission.routes,
  is_login: state => state.user.user.id !== -1
};

export default getters;
