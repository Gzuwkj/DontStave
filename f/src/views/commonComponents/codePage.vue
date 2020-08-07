<template>
  <div class="w-100">
    <div class="w-100 py-3">
      <div class="container px-0 bg-white" v-if="submit !== null">
        <div class="col-12 px-0">
          <div class="alert alert-info d-flex flex-column" id="alert">
            <h5 class="my-2">
              <router-link class="text-success" :to="{name: 'contestProblem',
                                                                     params: {contest_id: submit.match.id, problem_id: submit.problem.no}}">
                {{submit.problem.title}}
              </router-link>
            </h5>
            <div class="text-muted d-flex my-2 flex-column flex-md-row">
              <div class="mr-2 mb-1 mb-md-0">
                <span><b class="mr-1">提交时间 :</b> {{(new Date(submit.subTime)) | formatDate('yyyy-MM-dd HH:mm:ss')}}</span>
              </div>
              <div class="mr-2 mb-1 mb-md-0">
                <span><b class="mr-1">语言 :</b> {{submit.language}}</span>
              </div>
              <div class="mr-2 mb-1 mb-md-0">
                <span><b class="mr-1">运行时间 :</b> {{submit.time}}ms</span>
              </div>
              <div class="mr-2 mb-1 mb-md-0">
                <span><b class="mr-1">内存 :</b> {{submit.memory}}kb</span>
              </div>
            </div>
            <div class="text-muted">
              <span class="d-flex align-items-center"><b>运行状态 :</b> <div class="success ml-2">{{submit.result}}</div></span>
            </div>
          </div>
        </div>
        <div class="col-12 px-4 pb-4">
          <h5><router-link class="text-success" :to="{name: 'userInfo', params: {user_id: submit.user.id}}">{{submit.user.username}}</router-link> 的代码</h5>
          <div>
            <highLightBlock :content="submit.content"/>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import request from '@/utils/request'
  import {highLightBlock} from '@/components/highLightCode'
  export default {
    name: "codePage",
    data(){
      return {
        submit: null
      }
    },
    components: {
      highLightBlock
    },
    mounted() {
      request({
        url: this.$route.fullPath.replace(/\?.*/, '')
      }).then(data => {
        const {submit} = data;
        this.submit = submit;
      })
    }
  }
</script>

<style scoped>
  #alert h5{
    font-size: 17px;
  }
  #alert .text-muted{
    font-size: 14px;
  }
  #alert .success{
    background-color: #17bf63;
    color: #f5f6fa;
    font-size: 13px;
    padding: .3em .5em;
    border-radius: 3px;
    text-decoration: none;
  }
  #alert .danger{
    background-color: #ed3f14;
    font-size: 13px;
    color: #f5f6fa;
    padding: .3em .5em;
    border-radius: 3px;
    text-decoration: none;
  }
</style>
