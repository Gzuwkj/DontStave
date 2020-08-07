<template>
  <div class="w-100">
    <div class="bg-white shadow-sm">
      <div class="container px-0">
        <div class="problem-filter px-3 px-md-0 w-100 d-flex flex-wrap py-3">
          <h5>题目筛选：</h5>
          <div class="col-8 col-md-5 input-group mb-1 mb-md-0 px-0 mx-2 outline-none-search">
            <div class="input-group-prepend">
              <svg viewBox="0 0 1024 1024" class="m-auto" width="30" height="30">
                <path fill="#dadce0" d="M238.762667 238.805333a277.333333 277.333333 0 0 1 432.170666 341.632l141.056 141.056a64 64 0 1 1-90.538666 90.496l-141.013334-141.056A277.333333 277.333333 0 0 1 238.762667 238.805333zM299.136 299.093333a192 192 0 1 0 271.530667 0 192 192 0 0 0-271.530667 0z" />
              </svg>
            </div>
            <input type="text" placeholder="按标题或题目编号搜索" class="form-control">
          </div>
          <div @click.stop="downSelect($event)" class="mr-1 input-group outline-none-search down-select-search">
            <input style="max-width: 7.5rem;" type="text" placeholder="算法" class="form-control" readonly>
            <div class="input-group-prepend">
              <svg viewBox="0 0 1024 1024" width="30" height="30">
                <path fill="#dadce0" d="M821.020444 341.333333c27.818667 0 42.552889 36.067556 24.177778 58.936889L536.177778 784.497778a30.378667 30.378667 0 0 1-48.355556 0L178.801778 400.270222C160.426667 377.400889 175.217778 341.333333 202.979556 341.333333h618.040888z"/>
              </svg>
            </div>
            <div class="position-absolute w-100 bg-white shadow-sm">
              <ul class="d-flex flex-column align-items-center p-0 m-0">
                <li>全部</li>
                <li>字符串</li>
                <li>模拟</li>
                <li>动态规划</li>
                <li>数论</li>
                <li>图论</li>
              </ul>
            </div>
          </div>
          <div @click.stop="downSelect($event)" class="mr-1 input-group outline-none-search down-select-search">
            <input style="max-width: 7.5rem;" type="text" placeholder="难度" class="form-control" readonly>
            <div class="input-group-prepend">
              <svg viewBox="0 0 1024 1024" width="30" height="30">
                <path fill="#dadce0" d="M821.020444 341.333333c27.818667 0 42.552889 36.067556 24.177778 58.936889L536.177778 784.497778a30.378667 30.378667 0 0 1-48.355556 0L178.801778 400.270222C160.426667 377.400889 175.217778 341.333333 202.979556 341.333333h618.040888z"/>
              </svg>
            </div>
            <div class="position-absolute w-100 bg-white shadow-sm">
              <ul class="d-flex flex-column align-items-center p-0 m-0">
                <li>全部</li>
                <li>入门</li>
                <li>基础</li>
                <li>提高</li>
                <li>很难</li>
                <li>非常难</li>
                <li>难上加难</li>
              </ul>
            </div>
          </div>
          <div @click.stop="downSelect($event)" class="input-group outline-none-search down-select-search">
            <input style="max-width: 7.5rem;" type="text" placeholder="状态" class="form-control" readonly>
            <div class="input-group-prepend">
              <svg viewBox="0 0 1024 1024" width="30" height="30">
                <path fill="#dadce0" d="M821.020444 341.333333c27.818667 0 42.552889 36.067556 24.177778 58.936889L536.177778 784.497778a30.378667 30.378667 0 0 1-48.355556 0L178.801778 400.270222C160.426667 377.400889 175.217778 341.333333 202.979556 341.333333h618.040888z"/>
              </svg>
            </div>
            <div class="position-absolute w-100 bg-white shadow-sm">
              <ul class="d-flex flex-column align-items-center p-0 m-0">
                <li>全部</li>
                <li>未提交</li>
                <li>尝试</li>
                <li>已通过</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="w-100 problem-list">
      <div class="container px-0 pt-3">
        <div class="border-radius shadow">
          <table class="mb-0 table bg-white">
            <thead class="thead-light">
            <tr>
              <th scope="col">编号</th>
              <th scope="col">标题</th>
              <th scope="col">算法</th>
              <th scope="col">难度</th>
              <th scope="col">通过率</th>
              <th scope="col">状态</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(i, index) in problems" :key="index">
              <th scope="row">{{i.no}}</th>
              <td><router-link :to="{name: 'contestProblem', params: {contest_id: 1, problem_id: 1000}}">{{i.title}}</router-link></td>
              <td>
                <div class="type-item">数论</div>
                <div class="type-item">动态规划</div>
                <div class="type-item">图论</div>
                <div class="type-item">字符串</div>
              </td>
              <td>很难</td>
              <td>{{i.ac_nums}} / {{i.submit_nums}}</td>
              <td>未提交</td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    name: "problem",
    data(){
      return {
        problems: '',
      }
    },
    beforeRouteEnter(to, from, next){
      axios.get(to.meta.path).then(res=>{
        if(res.status === 200){
          next(vm=>{
            vm.problems = res.data.problems;
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
  .problem-filter{
    display: flex;
    align-items: center;
  }
  .problem-filter h5{
    width: 5rem;
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
    width: 6rem;
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
  table *{
    text-align: center;
    vertical-align: middle;
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
    text-align: center!important;
  }
  table tbody th, table tbody td{
    border-bottom-style: dashed;
    border-top-style: dashed;
    border-top-color: #95a5a6;
    border-bottom-color: #95a5a6;
    border-top-width: 1px;
    border-bottom-width: 1px;
  }
  .problem-list{
    max-height: calc(100vh - 60px - 55px - (2rem + 1.75rem + .25rem + 1.75rem));
    overflow-y: auto;
  }
  @media (min-width: 992px) {
    .problem-list{
      max-height: calc(100vh - 60px - 55px - (2rem + 1.75rem));
    }
  }
  .problem-list .table thead *{
    white-space:nowrap;
  }
  .problem-list .table thead tr th:nth-child(1), .problem-list .table tbody tr td:nth-child(1) {
    min-width: 2.2rem;
    max-width: 2.2rem;
  }
  .problem-list .table thead tr th:nth-child(2), .problem-list .table tbody tr td:nth-child(2) {
    min-width: 8rem;
    text-align: left;
  }
  .problem-list .table thead tr th:nth-child(3), .problem-list .table tbody tr td:nth-child(3) {
    min-width: 5rem;
    max-width: 5rem;
    text-align: right;
  }
  .problem-list .table thead tr th:nth-child(4), .problem-list .table tbody tr td:nth-child(4) {
    min-width: 2.75rem;
    max-width: 3rem;
  }
  .problem-list .table thead tr th:nth-child(5), .problem-list .table tbody tr td:nth-child(5) {
    min-width: 2.75rem;
    max-width: 3rem;
  }
  .problem-list .table thead tr th:nth-child(6), .problem-list .table tbody tr td:nth-child(6) {
    min-width: 3.75rem;
    max-width: 4rem;
  }
  .problem-list .table tbody *{
    padding: .5rem 0rem;
  }
  .problem-list .table tbody a{
    color: rgb(37, 187, 155);
  }
  .type-item{
    display: inline-block;
    padding: 0px 7px!important;
    margin: 0;
    font-size: 12px;
    color: #8a8a8a;
    border: 1px solid rgb(37, 187, 155);
    border-radius: 10px;
    cursor: pointer;
  }
</style>
