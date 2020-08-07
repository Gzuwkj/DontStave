<template>
  <div class="container px-0" style="display: block">
    <div class="border-radius shadow">
      <table class="mb-0 table bg-white">
        <thead class="thead-light">
        <tr>
          <th scope="col">#</th>
          <th scope="col">标题</th>
          <th scope="col">通过数</th>
          <th scope="col">尝试数</th>
          <th scope="col">通过率</th>
          <th scope="col">是否通过</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(i) in problems" :class="i.is_ac !== undefined ? (i.is_ac ? 'success': 'danger') : ''" :key="i.no">
          <th scope="row">{{i.no}}</th>
          <td>
            <router-link :to="{name: 'contestProblem', params: {contest_id: contest.id, problem_id: i.problem.no}}">
              {{i.problem.title}}
            </router-link>
          </td>
          <td>{{i.ac_num}}</td>
          <td>{{i.total_num}}</td>
          <td>{{isNaN(i.ac_num / i.total_num) ? 0 : Math.floor(i.ac_num / i.total_num * 1000) / 10}} %</td>
          <td>{{i.is_ac ?'通过':'未通过'}}</td>
        </tr>
        </tbody>
      </table>
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
        timer: null
      }
    },
    created() {
      this.timer = setInterval(this.getProblems, 1000 * 30);
    },
    methods: {
      getProblems(){
        request({
          url: this.$route.fullPath.replace(/\?.*/, '') + `/problem`,
          method: 'get',
        }).then(response => {
          const {status, problems} = response;
          if(status === 200) this.problems = problems;
        })
      }
    },
    destroyed() {
      clearInterval(this.timer);
    }
  }
</script>

<style scoped>
  .table thead *{
    white-space:nowrap;
  }
  .table thead tr th:nth-child(1), .table tbody tr td:nth-child(1) {
    min-width: 1.2em;
    max-width: 1.2em;
  }
  .table thead tr th:nth-child(2), .table tbody tr td:nth-child(2) {
    min-width: 12em;
  }
  .table thead tr th:nth-child(3), .table tbody tr td:nth-child(3) {
    min-width: 2.75em;
    max-width: 3em;
  }
  .table thead tr th:nth-child(4), .table tbody tr td:nth-child(4) {
    min-width: 2.75em;
    max-width: 3em;
  }
  .table thead tr th:nth-child(5), .table tbody tr td:nth-child(5) {
    min-width: 2.75em;
    max-width: 3em;
  }
  .table thead tr th:nth-child(6), .table tbody tr td:nth-child(6) {
    min-width: 3.75em;
    max-width: 4em;
  }
  .table tbody *{
    padding: .5rem 0;
  }
  .table tbody a{
    color: rgb(37, 187, 155);
  }
  .table tbody tr.success{
    background-color: rgba(79, 192, 141, 0.2);
    color: #17bf63;
  }
  .table tbody tr.success a{
    color: #17bf63;
  }
  .table tbody tr.danger{
    background-color: rgba(192, 57, 43, 0.1);
    color: #c0392b;
  }
  .table tbody tr.danger a{
    color: #c0392b;
  }
</style>
