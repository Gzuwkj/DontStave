<template>
  <li class="container px-0 d-block">
    <div class="w-100 d-flex px-0">
      <div class="input-group mb-3 col-6 col-md-2 px-1 outline-none-search">
        <div class="input-group-prepend">
          <svg viewBox="0 0 1024 1024" class="m-auto" width="30" height="30">
            <path fill="#dadce0" d="M238.762667 238.805333a277.333333 277.333333 0 0 1 432.170666 341.632l141.056 141.056a64 64 0 1 1-90.538666 90.496l-141.013334-141.056A277.333333 277.333333 0 0 1 238.762667 238.805333zM299.136 299.093333a192 192 0 1 0 271.530667 0 192 192 0 0 0-271.530667 0z" />
          </svg>
        </div>
        <label>
          <input v-model.lazy="filter.username" type="text" placeholder="按用户名搜索" class="form-control">
        </label>
      </div>
      <div class="input-group mb-3 col-6 col-md-2 px-1 outline-none-search">
        <div class="input-group-prepend">
          <svg viewBox="0 0 1024 1024" class="m-auto" width="30" height="30">
            <path fill="#dadce0" d="M238.762667 238.805333a277.333333 277.333333 0 0 1 432.170666 341.632l141.056 141.056a64 64 0 1 1-90.538666 90.496l-141.013334-141.056A277.333333 277.333333 0 0 1 238.762667 238.805333zM299.136 299.093333a192 192 0 1 0 271.530667 0 192 192 0 0 0-271.530667 0z" />
          </svg>
        </div>
        <label>
          <input v-model.lazy="filter.school" type="text" placeholder="按学校搜索" class="form-control">
        </label>
      </div>
    </div>
    <div class="row flex-nowrap justify-content-between mx-0 rank-list border-radius shadow tab-contest">
      <div class="px-0">
        <table class="table bg-white">
          <thead class="thead-light">
          <tr>
            <th scope="col">#</th>
            <th scope="col">用户</th>
            <th scope="col">AC</th>
            <th scope="col">昵称</th>
            <th scope="col">罚时</th>
            <th scope="col">学校</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(i, index) in rankList" :key="index">
            <td>{{i.ranking}}</td>
            <td><router-link :to="{name: 'userInfo', params: {user_id: i.user.id}}">{{i.user.username}}</router-link></td>
            <td>{{i.acNum}}</td>
            <td>{{i.user.nickname}}</td>
            <td>{{i.total_time | parseDate}}</td>
            <td>{{i.user.school}}</td>
          </tr>
          </tbody>
        </table>
      </div>
      <div class="px-0" ref="tableScreen">
        <table class="table mb-0">
          <thead class="thead-light">
          <tr>
            <th scope="col" v-for="i in problems" :key="i.no">{{i.no}}</th>
          </tr>
          </thead>
          <tbody @mousedown="dragScroll($event)" ref="tableMove">
          <tr v-for="(i, index) in rankList" :key="index">
            <td :class="j['is_ac']?'success':'danger'" :key="_index" v-for="(j, _index) in i['rank']">
                        <span v-if="j['is_ac']">
                          {{j["useTime"] | parseDate}}
                        </span>
              (-{{j["wrongTime"]}})
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  </li>
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
        rankList: [],
        total_rankList: [],
        filter: {
          school: ``,
          username: ``,
        }
      }
    },
    created() {
      this.getRank();
    },
    methods: {
      dragScroll(event){
        let startX = event.pageX;
        let _this = this;
        $(this.$refs.tableMove).mousemove(function (e) {
          let x = e.pageX;
          let realX =  $(_this.$refs.tableScreen).scrollLeft() - (x - startX) / 8;
          $(_this.$refs.tableScreen).scrollLeft(realX);
        });
        $(document).mouseup(function () {
          $(_this.$refs.tableMove).off('mousemove');
        })
      },
       getRank(){
        request({
          url: this.$route.fullPath.replace(/\?.*/, '') + `/rank`,
          method: `get`
        }).then(response=>{
          const {status, ranks} = response;
          if(status === 200){
            this.rankList = ranks.map(item => {
              item.total_time = 0;// 算罚时
              const {rank} = item;
              rank.forEach( i => {
                if(i["is_ac"])
                  item.total_time += i["useTime"] + (20 * 60 * i["wrongTime"]);
              });
              return item;
            });
            this.rankList.sort((a, b)=>{
              if(a["acNum"] > b["acNum"] || (a["acNum"] === b["acNum"] && a.total_time > b.total_time))
                return 1;
              else if((a["acNum"] === b["acNum"] && a.total_time === b.total_time))
                return 0;
              else if(a["acNum"] < b["acNum"] || (a["acNum"] === b["acNum"] && a.total_time < b.total_time))
                return -1;
            });
            for(let i = 0;i < this.rankList.length;i++)
              this.rankList[i]['ranking'] = i + 1;
            this.total_rankList = this.rankList;
          }
        })
      }
    },
    watch: {
      filter: {
        handler(value){
          let ret = this.total_rankList;
          Object.keys(value).forEach(key => {
            if(value[key] === ``) return;
            ret = ret.filter(i => {
              return value[key] === i[`user`][key];
            })
          });
          this.rankList = ret;
        },
        deep: true
      }
    },
    filters: {
      parseNum(value, index){
        value = value.toString();
        index = (index - value.length) < 0 ? 0 :  (index - value.length);
        while (index--){
          value = '0' + value;
        }
        return value;
      },
      parseDate(value){
        let hours = Math.floor(value / (60 * 60));
        value %= (60 * 60);
        let mints = Math.floor(value / 60);
        value %= 60;
        let seconds = value;
        function parseNum(value, index){
          value = value.toString();
          index = (index - value.length) < 0 ? 0 :  (index - value.length);
          while (index--){
            value = '0' + value;
          }
          return value;
        }
        return `${parseNum(hours, 2)}:${parseNum(mints, 2)}:${parseNum(seconds, 2)}`;
      },
    },
  }
</script>

<style scoped>
  .rank-list table tbody *{
    vertical-align: middle;
    height: 5em;
    word-break: break-all;
    font-family: Arial,sans-serif;
    font-size: 14px;
  }
  .rank-list div:first-child{
    flex: 1;
    border-right: 1px solid #bdc3c7;
  }
  .rank-list div:first-child table thead th:nth-child(1), .rank-list div:first-child table tbody tr td:nth-child(1) {
    min-width: 1.5em;
    max-width: 1.75em;
    padding-left: .5em;
  }
  .rank-list div:first-child table tbody tr td:nth-child(1){
    padding-left: .25em;
  }
  .rank-list div:first-child table thead th:nth-child(2), .rank-list div:first-child table tbody tr td:nth-child(2) {
    min-width: 4em;
    max-width: 4.5em;
  }
  .rank-list div:first-child table tbody tr td:nth-child(2) a{
    color: rgb(37, 187, 155);
  }
  .rank-list div:first-child table tbody tr td:nth-child(2){
    padding-left: .75em;
    padding-right: .75em;
  }
  .rank-list div:first-child table thead th:nth-child(3), .rank-list div:first-child table tbody tr td:nth-child(3) {
    min-width: 2.25em;
    max-width: 2.75em;
  }
  .rank-list div:first-child table thead th:nth-child(4), .rank-list div:first-child table tbody tr td:nth-child(4) {
    min-width: 4.5em;
    max-width: 5em;
  }
  .rank-list div:first-child table tbody tr td:nth-child(4) {
    padding-left: .75em;
    padding-right: .75em;
  }
  .rank-list div:first-child table thead th:nth-child(5), .rank-list div:first-child table tbody tr td:nth-child(5) {
    min-width: 3.5em;
    max-width: 4em;
  }
  .rank-list div:first-child table thead th:nth-child(5), .rank-list div:first-child table tbody tr td:nth-child(6) {
    min-width: 5.5em;
  }
  .rank-list div:first-child table tbody tr td:nth-child(6) {
    padding-left: .35em;
    padding-right: .35em;
  }
  .rank-list div table tbody tr th,.rank-list div table tbody tr td{
    background-color: rgb(252, 252, 252);
  }
  .rank-list div:last-child *{
    user-select: none;
  }
  .rank-list div:last-child{
    min-width: 6.5em;
    max-width: calc(6em * 7 + 1em);
    overflow-x: auto;
  }
  .rank-list div:last-child table thead th{
    width: 6em;
    min-width: 6em;
  }
  .rank-list div:last-child table tbody{
    cursor: grab;
  }
  .rank-list div:last-child table tbody td span{
    display: block;
    height: 1rem;
  }
  .rank-list div:last-child table tbody tr td.success{
    background-color: rgba(79, 192, 141, 0.2);
  }
  .rank-list div:last-child table tbody tr td.danger{
    background-color: rgba(192, 57, 43, 0.1);
  }
</style>
