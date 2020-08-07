<template>
  <div class="w-100">
    <div class="w-100 px-0 pt-3">
      <div class="w-100 px-0 mx-0 row" style="overflow-y: auto;max-height: calc(100vh - 60px - 55px);">
        <div class="col-12 col-md-6 mx-0 px-0 pl-md-1">
          <information :problem="problem.problem"/>
        </div>
        <div class="col-12 col-md-6 mx-0 px-0 pr-md-2 mb-3 mb-md-0">
          <code-editor :problem="problem.problem"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import request from '@/utils/request'
  import information from './components/information/index'
  import codeEditor from "./components/codeEditor";
  export default {
    name: "index",
    data(){
      return {
        problem: {
          problem: {},

        },
      }
    },
    components: {
      information,
      codeEditor
    },
    beforeRouteEnter(to, from, next){
      request({
        url: to.fullPath.replace(/\?.*/, ''),
      }).then(data => {
        const { problem } = data;
        next(vm => vm.problem = problem);
      });
    }
  }
</script>

<style scoped>

</style>
