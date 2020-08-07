<template>
  <div class="w-100">
    <div class="text-center container" id="from_box">
      <form class="form-signin" method="post" @click.prevent >
        <h1 class="h3 mb-3 font-weight-normal">请登录</h1>
        <label for="inputId" class="sr-only">用户名</label>
        <input type="text" id="inputId" v-model="username" class="form-control" placeholder="用户名" name="username" required autofocus autocomplete>
        <label for="inputPassword" class="sr-only">密码</label>
        <input type="password" id="inputPassword" v-model="password" class="form-control" placeholder="密码" name="password" required>
        <button class="btn btn-lg btn-block" :class="btn_class" v-html="button" type="submit" @click="login"></button>
        <p class="mt-5 mb-3 text-muted">&copy; 2017-2019</p>
      </form>
      <router-link :to="{name: 'register'}">注册</router-link>
    </div>
  </div>
</template>

<script>
  import {login_state_mapMutations} from "../../store/login_state";
  import axios from "axios";
  export default {
    name: "login",
    data(){
      return {
        username: '',
        password: '',
        button: '登录',
        btn_class: 'btn-primary',
      }
    },
    methods: {
      ...login_state_mapMutations,
      login(){
        let params = new URLSearchParams();
        params.append('username', this.username);
        params.append('password', this.password);
        let _this = this;
        this.button = ``;
        this.axios({
          url: this.$route.meta.path,
          method: 'post',
          data: params,
          transformRequest: [
            (data, headers) => {
              delete headers.common.Authorization;
              return data;
            }
          ]
        }).then(res=>{
          if(res.data.status === 200){
            sessionStorage.token = res.data.token;
            localStorage.token = res.data.token;
            this.setToken(res.data.token);
            this.setLoginState(true);
            this.setUser(res.data.user);
            axios.defaults.headers.common['Authorization'] = 'JWT ' + res.data.token;
            this.btn_class = 'btn-success';
            this.button =  `<svg viewBox="0 0 1024 1024" version="1.1" width="40" height="40"><path d="M857.6 188.928c-168.448 104.448-320 234.496-448.512 385.024L234.496 438.272l-77.312 61.44 301.568 304.64c100.352-216.064 242.176-411.136 417.28-572.928l-18.432-42.496z m0 0" fill="#e6e6e6" p-id="4642"></path></svg>`;
            setTimeout(
              () => this.$router.replace({name: 'contest'}),
              1000
            );
          }
          else{
            this.button = '登录';
            this.alert_msg = {
              stats: res.data.success ? 'success' : 'warning',
              msg: res.data.msg
            };
          }
        });
      }
    },
    computed: {
      alert_msg: {
        // eslint-disable-next-line vue/return-in-computed-property
        get(){
          return '';
        },
        set(value) {
          if (value) {
            $('.alert').alert('close');
            $('#from_box').prepend(`<div class="alert alert-${value.stats} alert-dismissible fade show" role="alert">
                             ${value.msg}
                            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                              <span aria-hidden="true">&times;</span>
                            </button>
                          </div>`);
          }
        }
      }
    }
  }
</script>

<style scoped>
  .form-signin {width: 100%;max-width: 330px;padding: 15px;margin: auto;margin-top: 5em;}
  .form-signin .checkbox {font-weight: 400;}
  .form-signin .form-control {position: relative;box-sizing: border-box;height: auto;padding: 10px;font-size: 16px;}
  .form-signin .form-control:focus {z-index: 2;}
  .form-signin h1 {margin-bottom: 1.5em!important;}
  .form-signin input[type="text"] {margin-bottom: 10px;border-bottom-right-radius: 0;border-bottom-left-radius: 0;}
  .form-signin input[type="password"] {margin-bottom: 10px;border-top-left-radius: 0;border-top-right-radius: 0;}
</style>
