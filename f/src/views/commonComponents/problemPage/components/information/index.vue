<template>
  <div class="d-flex flex-column bg-white px-3 pt-3 mx-0 pb-5" id="problem">
    <h5 class="mb-3">{{problem.title}}</h5>
    <div class="alert alert-secondary text-muted d-flex flex-column flex-md-row">
      <span class="mr-3">
        <b style="font-size: 14px">时间限制 : </b>
        {{problem.time}} ms
      </span>
      <span>
        <b style="font-size: 14px">内存限制 : </b>
        {{problem.memory}} mb
      </span>
    </div>
    <paragraph :content="problem.content">题目描述</paragraph>
    <paragraph class="mt-3" :content="problem.InputFormat">输入描述</paragraph>
    <paragraph class="mt-3" :content="problem.OutputFormat">输出描述</paragraph>
    <div class="mt-3" v-if="problem.problemExample && problem.problemExample.length !== 0">
      <h6><b>样例</b></h6>
      <hr>
      <div class="d-flex flex-column px-2" v-for="(i, index) in problem.problemExample" :key="index">
        <div>
          <h6 class="my-1"><b>#{{index + 1 }} </b> 输入</h6>
          <div class="p-1 paragraph-content" v-html="i.sampleInput"/>
        </div>
        <div class="mt-2">
          <h6 class="my-1"><b>#{{index + 1}} </b> 输出</h6>
          <div class="p-1 paragraph-content" v-html="i.sampleOutput"></div>
        </div>
      </div>
    </div>
    <paragraph :content="problem.tips">提示</paragraph>
  </div>
</template>

<script>
  import paragraph from "./paragraph";
  export default {
    props: {
      problem: {
        type: Object,
        required: true
      }
    },
    components: {
      paragraph
    }
  }
</script>

<style scoped>
  #problem{
    border: 1px solid #dadce0;
    border-radius: 5px 0 0 5px;
    max-height: calc(100vh - 60px - 55px - 1rem);
    overflow-y: auto;
    overflow-x: hidden;
  }
  @media (min-width: 768px) {
    #problem{
      border-radius: 5px;
    }
  }
  .paragraph-content{
    background: rgba(220, 221, 225, .5);
    border-radius: 4px;
  }
</style>
