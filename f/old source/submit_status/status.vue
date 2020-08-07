<template>
  <div class="w-100">
    <div class="bg-white shadow-sm">
      <div class="container px-0">
        <div class="status-filter px-3 px-md-0 w-100 d-flex align-items-center flex-wrap py-3">
          <h5>筛选：</h5>
          <div class="col-4 col-md-2 input-group pb-1 pb-md-0 px-0 mx-2 outline-none-search">
            <div class="input-group-prepend">
              <svg viewBox="0 0 1024 1024" class="m-auto" width="30" height="30">
                <path fill="#dadce0" d="M238.762667 238.805333a277.333333 277.333333 0 0 1 432.170666 341.632l141.056 141.056a64 64 0 1 1-90.538666 90.496l-141.013334-141.056A277.333333 277.333333 0 0 1 238.762667 238.805333zM299.136 299.093333a192 192 0 1 0 271.530667 0 192 192 0 0 0-271.530667 0z" />
              </svg>
            </div>
            <input type="text" placeholder="按用户名搜索" class="form-control">
          </div>
          <div class="col-5 col-md-2 input-group pb-1 pb-md-0 px-0 mx-2 outline-none-search">
            <div class="input-group-prepend">
              <svg viewBox="0 0 1024 1024" class="m-auto" width="30" height="30">
                <path fill="#dadce0" d="M238.762667 238.805333a277.333333 277.333333 0 0 1 432.170666 341.632l141.056 141.056a64 64 0 1 1-90.538666 90.496l-141.013334-141.056A277.333333 277.333333 0 0 1 238.762667 238.805333zM299.136 299.093333a192 192 0 1 0 271.530667 0 192 192 0 0 0-271.530667 0z" />
              </svg>
            </div>
            <input type="text" placeholder="按标题或题目编号搜索" class="form-control">
          </div>
          <div @click.stop="downSelect($event)" class="input-group outline-none-search down-select-search">
            <input style="max-width: 7.5rem;" type="text" placeholder="语言" class="form-control" readonly>
            <div class="input-group-prepend">
              <svg viewBox="0 0 1024 1024" width="30" height="30">
                <path fill="#dadce0" d="M821.020444 341.333333c27.818667 0 42.552889 36.067556 24.177778 58.936889L536.177778 784.497778a30.378667 30.378667 0 0 1-48.355556 0L178.801778 400.270222C160.426667 377.400889 175.217778 341.333333 202.979556 341.333333h618.040888z"/>
              </svg>
            </div>
            <div class="position-absolute w-100 bg-white shadow-sm">
              <ul class="d-flex flex-column align-items-center p-0 m-0">
                <li>全部</li>
                <li>C</li>
                <li>C++</li>
                <li>Java</li>
              </ul>
            </div>
          </div>
          <div @click.stop="downSelect($event)" class="input-group outline-none-search down-select-search">
            <input style="max-width: 7.5rem;" type="text" placeholder="运行状态" class="form-control" readonly>
            <div class="input-group-prepend">
              <svg viewBox="0 0 1024 1024" width="30" height="30">
                <path fill="#dadce0" d="M821.020444 341.333333c27.818667 0 42.552889 36.067556 24.177778 58.936889L536.177778 784.497778a30.378667 30.378667 0 0 1-48.355556 0L178.801778 400.270222C160.426667 377.400889 175.217778 341.333333 202.979556 341.333333h618.040888z"/>
              </svg>
            </div>
            <div class="position-absolute w-100 bg-white shadow-sm">
              <ul class="d-flex flex-column align-items-center p-0 m-0">
                <li>全部</li>
                <li>答案正确</li>
                <li>答案错误</li>
                <li>内存超限</li>
                <li>时间超限</li>
                <li>运行错误</li>
                <li>编译错误</li>
                <li>格式错误</li>
                <li>输出超限</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="status-list w-100">
      <div class="container px-0 py-3">
        <table class="mb-0 table bg-white shadow">
          <thead class="thead-light">
          <tr>
            <th scope="col">运行ID</th>
            <th scope="col">用户名</th>
            <th scope="col">题目</th>
            <th scope="col">运行结果</th>
            <th scope="col">运行时间(ms)</th>
            <th scope="col">内存(KB)</th>
            <th scope="col">语言</th>
            <th scope="col">提交时间</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(i, index) in statusList" :key="index">
            <td  scope="row">{{i.runID}}</td>
            <td><router-link :to="{name: 'userInfo', params: {user_id: i.user.id}}">{{i.user.username}}</router-link></td>
            <td><router-link to="#">{{i.problem.title}}</router-link></td>
            <td><router-link to="#">{{i.result}}</router-link></td>
            <td>{{i.time}}</td>
            <td>{{i.memory}}</td>
            <td>{{i.language}}</td>
            <td>{{(new Date(i.subTime) || new Date()).format('yyyy-MM-dd HH:mm:ss')}}</td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    name: "status",
    data(){
      return {
        statusList: ''
      }
    },
    beforeRouteEnter(to, from, next){
      axios.get(to.meta.path).then(res=>{
        if(res.data.status === 200){
          next(vm=>{

            vm.statusList = res.data.statusList;
          })
        }
      })
    },
    methods: {
      downSelect(event){
        let target = event.srcElement || event.target;
        let node = $(event.currentTarget);
        if(target.nodeName == 'LI'){
          node.children('input').attr('value', $(target).text())
        }
        node.children('div:last-child').toggleClass('show');
      }
    }
  }
</script>

<style scoped>
  .status-filter h5{
    width: 3rem;
    font-size: 1rem;
    font-weight: 600;
    margin: 0;
  }
  .outline-none-search input{
    border: 1px solid #dadce0;
    background-color: white;
    border-radius: 14px!important;
    padding-left: 2.35em;
    box-sizing: border-box;
    height: 1.75rem;
    font-size: 14px;
  }
  .outline-none-search input:focus{
    box-shadow: none;
    border: 1px solid #17bf63;
  }
  .outline-none-search.input-group{
    position: relative;
  }
  .outline-none-search .input-group-prepend{
    position: absolute;
    background: transparent;
    z-index: 4;
    width: 23px;
    top: -1px;
    left: 5px;
  }
  .down-select-search {
    width: 8rem;
  }
  .down-select-search input{
    cursor: pointer;
  }
  .down-select-search div:last-child{
    display: none;
    top: 1.75rem;
    border-radius: 5px;
    border: 1px solid #dadce0;
    max-height: 225px;
    overflow-y: auto;
  }
  .down-select-search div:last-child.show{
    display: block;
  }
  .down-select-search div:last-child ul li{
    list-style: none;
    cursor: pointer;
    line-height: 2.25em;
    width: 100%;
    text-align: center;
    border-bottom: 1px solid #dadce0;
  }
  .down-select-search div:last-child ul li:hover{
    color:#17bf63;
    background-color: rgba(79, 192, 141, 0.2);
  }
  .status-list{
    max-height: calc(100vh - 60px - 55px - (2rem + 1.75rem + .25rem + 1.75rem));
    overflow-y: auto;
  }
  @media (min-width: 992px) {
    .status-list{
      max-height: calc(100vh - 60px - 55px - (2rem + 1.75rem));
    }
  }

  table *{
    text-align: center;
    user-select: none;
    padding: 0;
    font-size: 14px;
  }
  table thead th{
    padding: .65em .25em;
    box-sizing: border-box;
    font-weight: 500;
    font-size: 16px;
    background-color: #eee;
    border-top: 1px solid #95a5a6;
  }
  table tbody th, table tbody td{
    border-bottom-style: dashed;
    border-top-style: dashed;
    border-top-color: #95a5a6;
    border-bottom-color: #95a5a6;
    border-top-width: 1px;
    border-bottom-width: 1px;
  }
  .status-list tbody td{
    vertical-align: middle;
    height: 3.25em;
    word-break: break-all;
    font-family: Arial;
  }
  .status-list tbody a{
    color: rgb(37, 187, 155);
  }
  .status-list tbody a.success{
    background-color: #17bf63;
    color: #f5f6fa;
    padding: .3em .5em;
    border-radius: 3px;
    text-decoration: none;
  }
  .status-list tbody a.danger{
    background-color: #ed3f14;
    color: #f5f6fa;
    padding: .3em .5em;
    border-radius: 3px;
    text-decoration: none;
  }
  .status-list thead th{
    vertical-align: middle;
  }
  .status-list tbody td:nth-child(1), .status-list thead th:nth-child(1){
    min-width: 4rem;
    max-width: 4rem;
  }
  .status-list tbody td:nth-child(2), .status-list thead th:nth-child(2){
    min-width: 4rem;
    max-width: 4.5rem;
  }
  .status-list tbody td:nth-child(3), .status-list thead th:nth-child(3){
     min-width: 7rem;
     text-align: left;
   }
  .status-list thead th:nth-child(3){
    text-align: center;
  }
  .status-list tbody td:nth-child(4), .status-list thead th:nth-child(4){
    min-width: 5rem;
    max-width: 5rem;
  }
  .status-list tbody td:nth-child(5), .status-list thead th:nth-child(5){
    min-width: 4.5rem;
    max-width: 4.5rem;
    flex-grow: 0;
  }
  .status-list tbody td:nth-child(6), .status-list thead th:nth-child(6){
    min-width: 3rem;
    max-width: 3rem;
    flex-grow: 0;
  }
  .status-list tbody td:nth-child(7), .status-list thead th:nth-child(7){
    min-width: 2.5rem;
    max-width: 2.5rem;
  }
  .status-list tbody td:nth-child(8), .status-list thead th:nth-child(8){
    min-width: 4.5em;
    max-width: 5em;
  }
  .status-list tbody td:nth-child(8){
    padding: 0 .25em;
  }
</style>
