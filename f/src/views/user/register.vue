<template>
  <div class="w-100">
    <div class="text-center container" id="from_box">
      <form ref="registerFrom" class="form-signin" method="post" @click.prevent>
        <h1 class="h3 mb-3 font-weight-normal">请填写注册信息</h1>
        <label for="inputId" class="sr-only">用户名</label>
        <input type="text" id="inputId" v-model.lazy="registerFrom.username" class="form-control" placeholder="用户名" name="username" required autofocus autocomplete>
        <div class="invalid-feedback mb-1 mt-0">
          {{ registerFrom.tips.username }}
        </div>
        <label for="inputPassword1" class="sr-only">密码</label>
        <input type="password" id="inputPassword1" v-model.lazy="registerFrom.password" class="form-control" placeholder="密码"  name="password" required>
        <div class="invalid-feedback mb-1 mt-0">
          {{ registerFrom.tips.password }}
        </div>
        <label for="inputPassword2" class="sr-only">确认密码</label>
        <input type="password" id="inputPassword2" v-model.lazy="registerFrom.repassword" class="form-control" placeholder="确认密码" name="repassword" required>
        <div class="invalid-feedback mb-1 mt-0">
          {{ registerFrom.tips.repassword }}
        </div>
        <button class="btn btn-lg btn-block" :class="loading.class" type="submit" @click="register" v-html="loading.content"/>
      </form>
    </div>
  </div>
</template>

<script>
  export default {
    name: "register",
    data(){
      return {
        registerFrom: {
          username: '',
          password: '',
          repassword: '',
          tips: {
            username: `用户名由数字字母下划线组成 只能以字母开头`,
            password: `密码长度为8-16位`,
            repassword: `两次密码不一致`,
          },
          submitAllow: false,
        },
        loading: {
          class: 'btn-primary',
          content: `注册`
        },
      }
    },
    watch: {
      registerFrom: {
        handler(value){
          const $registerFrom = $(this.$refs.registerFrom);
          const $username = $registerFrom.children(`input[name='username']`);
          const $password = $registerFrom.children(`input[name='password']`);
          const $repassword = $registerFrom.children(`input[name='repassword']`);

          let fu = /^[A-Za-z]\w{4,15}$/.test(value.username);
          $username.toggleClass(`is-invalid`, !fu);
          $username.toggleClass(`is-valid`, fu);

          let fp = /^.{8,16}$/.test(value.password);
          $password.toggleClass(`is-invalid`, !fp);
          $password.toggleClass(`is-valid`, fp);

          let fp2 = value.repassword !== '' && value.password === value.repassword;
          $repassword.toggleClass(`is-invalid`, !fp2);
          $repassword.toggleClass(`is-valid`, fp2);

          this.registerFrom.submitAllow = fp && fu && fp2;
        },
        deep: true,
      }
    },
    methods: {
      register(){
        if(this.registerFrom.submitAllow){
          this.loading.content = `<svg  xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="40px" height="40px" viewBox="0 0 40 40" enable-background="new 0 0 40 40" xml:space="preserve"><path opacity="0.2" fill="#fff" d="M20.201,5.169c-8.254,0-14.946,6.692-14.946,14.946c0,8.255,6.692,14.946,14.946,14.946 s14.946-6.691,14.946-14.946C35.146,11.861,28.455,5.169,20.201,5.169z M20.201,31.749c-6.425,0-11.634-5.208-11.634-11.634 c0-6.425,5.209-11.634,11.634-11.634c6.425,0,11.633,5.209,11.633,11.634C31.834,26.541,26.626,31.749,20.201,31.749z"/><path fill="white" d="M26.013,10.047l1.654-2.866c-2.198-1.272-4.743-2.012-7.466-2.012h0v3.312h0 C22.32,8.481,24.301,9.057,26.013,10.047z"><animateTransform attributeType="xml" attributeName="transform" type="rotate" from="0 20 20" to="360 20 20" dur="0.5s" repeatCount="indefinite"/></path></svg>`;
          this.$store.dispatch('user/register', this.registerFrom).then(response => {
            this.loading.class = `btn-success`;
            this.loading.content = `马上跳转`;
            this.$router.replace({ name: 'login' })
          }).catch(error => {
            this.loading.content = `注册`;
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
  .form-signin {width: 100%;max-width: 330px;padding: 15px;margin: 5em auto auto;background: #ffffff;}
  .form-signin .checkbox {font-weight: 400;}
  .form-signin .form-control {position: relative;box-sizing: border-box;height: auto;padding: 10px;font-size: 16px;}
  .form-signin .form-control:focus {z-index: 2;}
  .form-signin h1 {margin-bottom: 1.5em!important;}
  .form-signin input{margin-bottom: 10px;}
  .form-signin input[type="text"] {border-bottom-right-radius: 0;border-bottom-left-radius: 0;}
  .form-signin input[name="password2"] {border-top-left-radius: 0;border-top-right-radius: 0;}
  .is-valid+.invalid-feedback{display: none;}
  .is-invalid+.invalid-feedback{display: block;}
</style>
