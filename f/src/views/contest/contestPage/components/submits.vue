<template>
  <div class="container px-0" style="display: block">
    <div class="w-100 d-flex flex-wrap px-0">
      <div class="input-group mb-3 col-6 col-md-2 px-1 outline-none-search">
        <div class="input-group-prepend">
          <svg viewBox="0 0 1024 1024" class="m-auto" width="30" height="30">
            <path fill="#dadce0" d="M238.762667 238.805333a277.333333 277.333333 0 0 1 432.170666 341.632l141.056 141.056a64 64 0 1 1-90.538666 90.496l-141.013334-141.056A277.333333 277.333333 0 0 1 238.762667 238.805333zM299.136 299.093333a192 192 0 1 0 271.530667 0 192 192 0 0 0-271.530667 0z" />
          </svg>
        </div>
        <label>
          <input type="text" v-model.lazy="filter.username" placeholder="按用户名搜索" class="form-control">
        </label>
      </div>
      <div @click.stop="downSelect($event, 'problem_id')" class="input-group mb-3 col-3 col-md-2 col-lg-1 px-1 outline-none-search down-select-search">
        <label>
          <input type="text" placeholder="题目" class="form-control" readonly/>
        </label>
        <div class="input-group-prepend">
          <svg viewBox="0 0 1024 1024" width="30" height="30">
            <path fill="#dadce0" d="M821.020444 341.333333c27.818667 0 42.552889 36.067556 24.177778 58.936889L536.177778 784.497778a30.378667 30.378667 0 0 1-48.355556 0L178.801778 400.270222C160.426667 377.400889 175.217778 341.333333 202.979556 341.333333h618.040888z"/>
          </svg>
        </div>
        <div class="position-absolute w-100 bg-white shadow-sm">
          <ul class="d-flex flex-column align-items-center p-0 m-0">
            <li>全部</li>
            <li v-for="i in problems"  :data-v-value='i.problem.no' :key="i.no">{{i.no}}</li>
          </ul>
        </div>
      </div>
      <div @click.stop="downSelect($event, 'language')" class="input-group mb-3 col-3 col-md-2 col-lg-1 px-1 outline-none-search down-select-search">
        <label>
          <input type="text" placeholder="语言" class="form-control" readonly/>
        </label>
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
      <div @click.stop="downSelect($event, 'judge_states')" class="input-group mb-3 col-4 col-md-2 px-1 outline-none-search down-select-search">
        <label>
          <input style="max-width: 7.5rem" type="text" placeholder="运行结果" class="form-control" readonly/>
        </label>
        <div class="input-group-prepend">
          <svg viewBox="0 0 1024 1024" width="30" height="30">
            <path fill="#dadce0" d="M821.020444 341.333333c27.818667 0 42.552889 36.067556 24.177778 58.936889L536.177778 784.497778a30.378667 30.378667 0 0 1-48.355556 0L178.801778 400.270222C160.426667 377.400889 175.217778 341.333333 202.979556 341.333333h618.040888z"/>
          </svg>
        </div>
        <div class="position-absolute w-100 bg-white shadow-sm">
          <ul class="d-flex flex-column align-items-center p-0 m-0">
            <li>全部</li>
            <li v-for="(i, index) in new Array(8)" :key="index" :data-v-value="index + 1">{{index | format}}</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="status-list border-radius shadow tab-contest">
      <table class="mb-0 table bg-white">
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
          <td>{{i.runID}}</td>
          <td><router-link to="#">{{i.user.username}}</router-link></td>
          <td>
            <router-link :to="{ name: 'contestProblem',params: { contest_id: contest.id, problem_id: i.problem.no } }">
              {{(problems.find(item=>item.problem.no === i.problem.no) || {'no': 'A'}).no}}
            </router-link>
          </td>
          <td>
            <router-link :to="{name: 'contestCode', params: {contest_id: contest.id, run_id: i.runID}}">
              {{i.result | format}}
            </router-link>
          </td>
          <td>{{i.memory}}</td>
          <td>{{i.time}}</td>
          <td>{{i.language}}</td>
          <td>{{(i.subTime || new Date()) | formatDate('yyyy-MM-dd HH:mm:ss')}}</td>
        </tr>
        </tbody>
      </table>
      <nav v-if="pages > 1">
        <ul class="pagination justify-content-center">
          <li class="page-item" :class="{disabled : filter.page === 1}">
            <a class="page-link" @click.prevent="filter.page = 1" href="#">
              <span aria-hidden="true">&laquo;</span>
            </a>
          </li>
          <li class="page-item" v-for="(i, index) in new Array(pages)" :key="index" :class="{active: filter.page === index + 1}">
            <a class="page-link"  href="#" @click.prevent="filter.page = index + 1">{{index + 1}}</a>
          </li>
          <li class="page-item" :class="{disabled : filter.page === pages}">
            <a class="page-link" @click.prevent="filter.page = pages" href="#" aria-label="Next">
              <span aria-hidden="true">&raquo;</span>
            </a>
          </li>
        </ul>
      </nav>
    </div>
  </div>
</template>

<script>
  import request from '@/utils/request'
  export default {
    props: {
      contest: {
        type: Object,
        required: true
      },
      problems: {
        type: Array,
        required: true
      }
    },
    data(){
      return {
        statusList: [],
        filter: {
          judge_states: ``,
          language: ``,
          problem_id: ``,
          username: ``,
          page: 1
        },
        pages: 1,
      }
    },
    created() {
      this.getStatus();
    },
    methods: {
      downSelect(event, key){
        let target = event.target;
        let node = $(event.currentTarget);
        if(target.nodeName === 'LI'){
          node.children('label').children('input').attr('value', $(target).text());
          if(typeof $(target).attr('data-v-value') !== 'undefined')
            this.filter[key] = $(target).attr('data-v-value');
          else
            this.filter[key] = $(target).text();
          this.filter.page = 1;
        }
        node.children('div:last-child').toggleClass('show');
      },

      getStatus(params = {}){
        request({
          url: this.$route.fullPath.replace(/\?.*/, '') + `/submit`,
          method: 'get',
          params
        }).then(data => {
          const { status, statusList, pages } = data;
          if(status === 200){
            this.statusList = statusList.map(item => {
              item.subTime = new Date(item.subTime);
              return item;
            });
            this.pages = pages;
          }
        })
      }
    },
    watch: {
      filter: {
        handler(value){
          this.getStatus(Object.keys(value).reduce((params, key) => {
            if(value[key] !== `` && value[key] !== `全部`)
              params[key] = value[key];
            return params;
          }, {}));
        },
        deep: true
      }
    },
    filters: {
      format(value){
        const fmt = [`答案正确`, `答案错误`, `内存超限`, `时间超限`, `运行错误`, `编译错误`, `格式错误`, `输出超限`];
        return fmt[value];
      }
    }
  }
</script>

<style scoped>
  .status-list tbody td{
    min-width: 2em;
    max-width: 2.5em;
    vertical-align: middle;
    height: 3.25em;
    word-break: break-all;
    font-family: Arial,serif;
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
    min-width: 3em;
    max-width: 4em;
    vertical-align: middle;
  }
  .status-list tbody td:nth-child(1), .status-list thead th:nth-child(1){
    min-width: 4em;
    max-width: 4.5em;
  }
  .status-list tbody td:nth-child(2), .status-list thead th:nth-child(2){
    min-width: 4em;
    max-width: 4.5em;
  }
  .status-list tbody td:nth-child(4), .status-list thead th:nth-child(4){
    min-width: 5em;
    max-width: 5.5em;
  }
  .status-list tbody td:nth-child(5), .status-list thead th:nth-child(5){
    min-width: 4.5em;
    max-width: 5em;
  }
  .status-list tbody td:nth-child(8), .status-list thead th:nth-child(8){
    min-width: 4.5em;
    max-width: 5em;
  }
  .status-list tbody td:nth-child(8){
    padding: 0 .25em;

  }
  .page-item .page-link{
    color: rgb(37, 187, 155);
  }
  .page-item.disabled .page-link{
    color: #6c757d;
  }
  .page-item.active .page-link{
    background: rgb(37, 187, 155);
    border-color: rgb(37, 187, 155);
    color: white;
  }
</style>
