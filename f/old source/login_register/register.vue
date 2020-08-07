<template>
  <div class="w-100">
    <div class="text-center container" id="from_box">
      <form class="form-signin" method="post" @click.prevent>
        <h1 class="h3 mb-3 font-weight-normal">请填写注册信息</h1>
        <label for="inputId" class="sr-only">用户名</label>
        <input type="text" id="inputId" class="form-control" placeholder="用户名" name="username" v-model="username" required autofocus autocomplete>
        <label for="inputPassword1" class="sr-only">密码</label>
        <input type="password" id="inputPassword1" class="form-control" placeholder="密码" v-model="password" name="password1" required>
        <label for="inputPassword2" class="sr-only">确认密码</label>
        <input type="password" id="inputPassword2" class="form-control" placeholder="确认密码" v-model="password2" name="password2" required>
        <button class="btn btn-lg btn-block" :class="btn_class" type="submit" @click="register" v-html="button"></button>
      </form>
    </div>
  </div>
</template>

<script>
  import {login_state_mapGetters, login_state_mapMutations} from "../../store/login_state";
  export default {
    name: "Register",
    data() {
      return {
        username: '',
        password: '',
        password2: '',
        button: '注册',
        btn_class: 'btn-primary',
      }
    },
    created(){
    },
    computed: {
      ...login_state_mapGetters,
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
    },
    methods: {
      ...login_state_mapMutations,
      register(){
        let param = new URLSearchParams();
        param.append('username', this.username);
        param.append('password', this.password);
        param.append('repassword', this.password2);
        this.button = `<svg x="0px" y="0px" width="40px" height="40px" viewBox="0 0 40 40" enable-background="new 0 0 40 40" xml:space="preserve"><path opacity="0.2" fill="#fff" d="M20.201,5.169c-8.254,0-14.946,6.692-14.946,14.946c0,8.255,6.692,14.946,14.946,14.946 s14.946-6.691,14.946-14.946C35.146,11.861,28.455,5.169,20.201,5.169z M20.201,31.749c-6.425,0-11.634-5.208-11.634-11.634 c0-6.425,5.209-11.634,11.634-11.634c6.425,0,11.633,5.209,11.633,11.634C31.834,26.541,26.626,31.749,20.201,31.749z"/><path fill="white" d="M26.013,10.047l1.654-2.866c-2.198-1.272-4.743-2.012-7.466-2.012h0v3.312h0 C22.32,8.481,24.301,9.057,26.013,10.047z"><animateTransform attributeType="xml" attributeName="transform" type="rotate" from="0 20 20" to="360 20 20" dur="0.5s" repeatCount="indefinite"/></path></svg>`;
        this.axios.post(this.$route.meta.path, param).then(res=>{
          if(res.data.status === 200){
            this.btn_class = 'btn-success';
            this.button =  `<svg viewBox="0 0 1024 1024" version="1.1" width="40" height="40"><path d="M857.6 188.928c-168.448 104.448-320 234.496-448.512 385.024L234.496 438.272l-77.312 61.44 301.568 304.64c100.352-216.064 242.176-411.136 417.28-572.928l-18.432-42.496z m0 0" fill="#e6e6e6" p-id="4642"></path></svg>`;
            setTimeout(
              () => this.$router.replace({name: 'login'}),
              1000
            )
          }
          else
            this.button = '注册';
            this.alert_msg = {
              stats: res.data.success ? 'success' : 'warning',
              msg: res.data.msg
            };
        }).catch(error=>{
          console.log(error);
        })
      }
    }
  }
</script>

<style scoped>
  .form-signin {width: 100%;max-width: 330px;padding: 15px;margin: auto;margin-top: 5em; background: #ffffff;}
  .form-signin .checkbox {font-weight: 400;}
  .form-signin .form-control {position: relative;box-sizing: border-box;height: auto;padding: 10px;font-size: 16px;}
  .form-signin .form-control:focus {z-index: 2;}
  .form-signin h1 {margin-bottom: 1.5em!important;}
  .form-signin input{margin-bottom: 10px;}
  .form-signin input[type="text"] {border-bottom-right-radius: 0;border-bottom-left-radius: 0;}
  .form-signin input[name="password2"] {border-top-left-radius: 0;border-top-right-radius: 0;}
</style>
