<template>
  <div class="w-100">
    <div class="w-100">
      <div class="mt-0 bg-white w-100 d-flex shadow-sm flex-column flex-md-row">
        <div class="container filter-menu">
          <ul id="filter" class="pl-0 position-relative">
            <h5>比赛状态 : </h5>
            <li id="slide"/>
            <li :class="filter === 1 ? 'active':''" @click="filter=1">未开始</li>
            <li :class="filter === 2 ? 'active':''" @click="filter=2">进行中</li>
            <li :class="filter === 3 ? 'active':''" @click="filter=3">已结束</li>
            <li :class="filter === 4 ? 'active':''" @click="filter=4">全部</li>
          </ul>
        </div>
      </div>
      <div style="overflow: auto; max-height: calc(100vh - 60px - 55px - 80px)">
        <div class="container px-0 px-md-2 d-flex flex-column">
          <transition-group name="list" tag="p">
          <v-contest-item v-for="i in contests" :key="i.id" :contest="i"/>
          </transition-group>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import contestItem from "./contestItem";
  import request from "@/utils/request"
  import {deepSearch} from "@/utils/utils";
  import router from "@/router";
  export default {
    name: "index",
    data(){
      return {
        contests: [],
        filter: 4,
      }
    },
    components: {
      'v-contest-item': contestItem
    },
    mounted() {
      const dom = $(`#filter li:eq(${ this.filter })`);
      $('#slide').css({ left: + dom.position().left, width: dom.width() })
      this.getList();
    },
    methods: {
      getList(params = {}){
        request({
          url: this.$route.fullPath.replace(/\?.*/, ''),
          method: 'get',
          params
        }).then(response => {
          const { contest, status } = response;
          if(status === 200){
            this.contests = contest.map(item => {
              return {
                id: item.id,
                title: item.matchName,
                startTime: new Date(item.startTime),
                length: item.howLong,
                owner: item.owner,
                number: item.registerNum,
                is_lock: false,
                is_finish: item.status >= 3
              }
            });
            this.contests = this.contests ? this.contests : [];
          }
        }).catch(error => {

        })
      }
    },
    watch: {
      filter(value) {
        const dom = $(`#filter li:eq(${value})`);
        const pos = dom.position();
        const width = dom.width();
        $('#slide').css({ left: + pos.left, width: width });
        this.getList({contest_status: value});
      }
    }
  }
</script>

<style scoped>
  .filter-menu{
    height: 80px;
  }
  .filter-search{
    height: 80px;
    padding: 0;
    width: 340px;
  }
  .filter-menu ul{
    list-style: none;
    user-select: none;
    display: flex;
    height: 80px;
    width: 340px;
    justify-content: space-between;
    align-items: center;
  }
  #slide{
    position: absolute;
    display: inline-block;
    height: 1.8em;
    width: 4.25em;
    border-radius: 15px;
    border: 1px solid #17bf63;
    background: rgba(79, 192, 141, 0.2);
    transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1.05);
    right: 0;
  }
  .filter-menu ul h5{
    display: block;
    color: #273849;
    height: 1.3em;
    font-size: 1rem;
    font-weight: 600;
    margin-right: 5px;
    margin-bottom: 0;
  }
  .filter-menu ul li{
    cursor: pointer;
    display: inline-block;
    line-height: 1.8em;
    color: #273849;
    width: 4em;
    text-align: center;
    vertical-align: middle;
    box-sizing: border-box;
    transition: color 0.4s linear;
  }
  .filter-menu ul li.active{
    color: #17bf63;
  }

  .list-item {
    display: inline-block;
  }
  .list-enter-active, .list-leave-active {
    transition: all 0.25s linear;
  }
  .list-enter, .list-leave-to
    /* .list-leave-active for below version 2.1.8 */ {
    opacity: 0;
    transform: translateY(10px);
  }
  .list-move {
    transition: transform 0.25s;
  }
</style>
