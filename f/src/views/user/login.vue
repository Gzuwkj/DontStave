<template>
  <div class="w-100">
    <div class="text-center container" id="from_box">
      <form ref="loginFrom" method="post" class="form-signin" @click.prevent>
        <h1 class="h3 mb-3 font-weight-normal">请登录</h1>
        <label for="inputId" class="sr-only">用户名</label>
        <input type="text" id="inputId" v-model.lazy="loginForm.username" class="form-control" placeholder="用户名" name="username" required autofocus autocomplete>
        <div class="invalid-feedback mb-1 mt-0">
          {{ loginForm.tips.username }}
        </div>
        <label for="inputPassword" class="sr-only">密码</label>
        <input type="password" id="inputPassword" v-model.lazy="loginForm.password" class="form-control" placeholder="密码" name="password" aria-describedby="passwordHelpBlock" required>
        <div class="invalid-feedback mb-1 mt-0">
          {{ loginForm.tips.password }}
        </div>
        <button class="btn btn-lg btn-block" :class="loading.class" type="submit" @click="login" v-html="loading.content"/>
        <p class="mt-5 mb-3 text-muted">&copy; 2017-2019</p>
      </form>
      <router-link :to="{name: 'register'}">注册</router-link>
    </div>
  </div>
</template>

<script>
  import Vue from 'vue'
  export default {
    name: "login",
    data(){
      return {
        loginForm: {
          username: '',
          password: '',
          tips: {
            username: `用户名由数字字母下划线组成 只能以字母开头`,
            password: `密码长度为8-16位`,
          },
          submitAllow: false
        },
        loading: {
          class: 'btn-primary',
          content: `登录`
        },
        redirect: '',
      }
    },
    watch: {
      $route: {
        handler: function(route) {
          const query = route.query;
          if (query) {
            this.redirect = query.redirect || '';
          }
        },
        immediate: true
      },
      loginForm: {
        handler(value){
          const $loginFrom = $(this.$refs.loginFrom);
          const $username = $loginFrom.children(`input[name='username']`);
          const $password = $loginFrom.children(`input[name='password']`);

          let fu = /^[A-Za-z]\w{4,15}$/.test(value.username);
          $username.toggleClass(`is-invalid`, !fu);
          $username.toggleClass(`is-valid`, fu);

          let fp = /^.{8,16}$/.test(value.password);
          $password.toggleClass(`is-invalid`, !fp);
          $password.toggleClass(`is-valid`, fp);
          this.loginForm.submitAllow = fp && fu;
        },
        deep: true,
      }
    },
    methods: {
      login(){
        if(this.loginForm.submitAllow){
          this.loading.content = `<svg  xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="40px" height="40px" viewBox="0 0 40 40" enable-background="new 0 0 40 40" xml:space="preserve"><path opacity="0.2" fill="#fff" d="M20.201,5.169c-8.254,0-14.946,6.692-14.946,14.946c0,8.255,6.692,14.946,14.946,14.946 s14.946-6.691,14.946-14.946C35.146,11.861,28.455,5.169,20.201,5.169z M20.201,31.749c-6.425,0-11.634-5.208-11.634-11.634 c0-6.425,5.209-11.634,11.634-11.634c6.425,0,11.633,5.209,11.633,11.634C31.834,26.541,26.626,31.749,20.201,31.749z"/><path fill="white" d="M26.013,10.047l1.654-2.866c-2.198-1.272-4.743-2.012-7.466-2.012h0v3.312h0 C22.32,8.481,24.301,9.057,26.013,10.047z"><animateTransform attributeType="xml" attributeName="transform" type="rotate" from="0 20 20" to="360 20 20" dur="0.5s" repeatCount="indefinite"/></path></svg>`;
          this.$store.dispatch('user/login', this.loginForm).then(response => {
            this.loading.class = `btn-success`;
            this.loading.content = `马上跳转`;
            this.$router.replace({ path: this.redirect || '/' });
          }).catch(error => {
            this.loading.content = `登录`;
            alert(error);
            console.log(error)
          })
        }
        else alert(`请正确填写信息`);
      }
    }
  }
</script>

<style scoped>
  .form-signin {width: 100%;max-width: 330px;padding: 15px;margin: 5em auto auto;}
  .form-signin .checkbox {font-weight: 400;}
  .form-signin .form-control {position: relative;box-sizing: border-box;height: auto;padding: 10px;font-size: 16px;}
  .form-signin .form-control:focus {z-index: 2;}
  .form-signin h1 {margin-bottom: 1.5em!important;}
  .form-signin input[type="text"] {margin-bottom: 10px;border-bottom-right-radius: 0;border-bottom-left-radius:0;}
  .form-signin input[type="password"] {margin-bottom: 10px;border-top-left-radius: 0;border-top-right-radius:0;}
  .is-valid+.invalid-feedback{display: none;}
  .is-invalid+.invalid-feedback{display: block;}
</style>
