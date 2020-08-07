<template>
  <div class="w-100">
    <div class="w-100">
      <transition name="fade" mode="out-in" appear>
        <div v-if="contest.is_start" key="title">
          <div class="w-100 bg-white shadow-sm">
            <div class="mt-0 w-100 container px-0">
              <ul :class="{'show': mobileMenu.show}" class="nav-contest nav flex-column flex-md-row align-items-center position-relative">
                <li class="slide position-absolute"/>
                <li @click="toggleTab(1)" class="nav-item" :class="{'active': tab === 1}">
                  <a class="nav-link" >比赛说明</a>
                </li>
                <li @click="toggleTab(2)" class="nav-item" :class="{'active': tab === 2}">
                  <a class="nav-link" >题目</a>
                </li>
                <li @click="toggleTab(3)" class="nav-item" :class="{'active': tab === 3}">
                  <a class="nav-link" >排名</a>
                </li>
                <li @click="toggleTab(4)" class="nav-item" :class="{'active': tab === 4}">
                  <a class="nav-link" >提交记录</a>
                </li>
                <li @click="mobileMenu.show =! mobileMenu.show" class="bg-white position-absolute nav-item d-md-none w-100">
                  <svg-icon class="mx-2" icon-name="icon-down"/>
                  {{ mobileMenu.active }}
                </li>
              </ul>
            </div>
          </div>
          <div class="content-contest">
            <div class="w-100 px-0">
              <contest-progress :contest="contest"/>
              <div class="w-100 pb-5">
                <transition name="component-fade" mode="out-in">
                  <component :problems="problems" :contest="contest" :is="view" />
                </transition>
              </div>
            </div>
          </div>
        </div>
        <div v-if="!contest.is_start" class="content-contest pt-5" key="countdown">
          <contest-countdown  :contest="contest"/>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
  import {info, progress, problems, rank, submits, countdown} from './components'
  import request from '@/utils/request'
  import axios from "axios";
  export default {
    name: "contestPage",
    data(){
      return {
        mobileMenu: {
          show: false,
          active: `比赛说明`,
        },
        tab: 1,
        contest: {
          startTime: new Date(1),
          matchName: 'unknown contest',
          endTime: new Date(),
          id: -1,
          is_start: false,
        },
        components: [`contest-info`, `contest-problems`, `contest-rank`, `contest-submits`],
        problems: [],
      }
    },
    components: {
      'contest-info': info,
      'contest-problems': problems,
      'contest-rank': rank,
      'contest-submits': submits,
      'contest-countdown': countdown,
      'contest-progress': progress
    },
    created() {
      request({
        url: this.$route.fullPath.replace(/\?.*/, ''),
        method: 'get',
      }).then(response => {
        const { contest, is_start, status } = response;
        console.log(response)
        if(status === 200) {
          this.contest = {
            id: contest.id,
            title: contest.matchName,
            info: contest.info,
            owner: contest.owner,
            length: contest['howLong'],
            is_start: is_start,
            is_finish: contest.status >= 3,
            startTime: new Date(contest.startTime),
            endTime: new Date(new Date(contest.startTime).getTime() + (1000 * 60 * contest['howLong']))
          }
        }
      })

      request({
        url: this.$route.fullPath.replace(/\?.*/, '') + `/problem`,
        method: 'get',
      }).then(response => {
        const {status, problems} = response;
        if(status === 200) this.problems = problems;
      })
    },
    computed: {
      view(){
        return this.components[this.tab-1];
      }
    },
    methods: {
      toggleTab(tab){
        this.tab = tab;
        this.mobileMenu.show = false;
        this.mobileMenu.active = $(`.nav-contest li:eq(${tab}) a`).text();
      }
    },
    watch: {
      tab(value){
        let dom = $(`.nav-contest li:eq(${value})`);
        $(".nav-contest li.slide").css({left: + dom.position().left, width: '5.95em' });
      },
    }
  }
</script>

<style scoped>
  .nav-contest{
    height: 60px;
    overflow: hidden;
    transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1.05);
  }
  .nav-contest.show{
    height: calc(60px + 1.8em*3 + 17px*3 + 5px);
  }
  .nav-contest li.active{
    display: none;
  }
  .nav-contest li{
    line-height: 1.8em;
    font-size: 17px;
    text-align: center;
    width: 100%;
    cursor: pointer;
  }
  .nav-contest li a{
    color: #273849;
  }
  .nav-contest.show li:last-child{
    border-top: 1px solid #dadce0;
  }
  .nav-contest li:last-child{
    bottom: 0;
    height: 60px;
    display: flex;
    font-size: 18px;
    align-items: center;
    cursor: pointer;
    color: #273849;
  }
  .nav-contest.show li:last-child svg{
    transform: rotate(180deg);
    transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1.05);
  }
  .content-contest{
    min-height: calc(100vh - 60px - 55px - (60px + 1.8em*3 + 17px*3 + 5px));
    max-height: calc(100vh - 60px - 55px - 60px);
    overflow-y: auto;
  }
  @media (min-width: 768px) {
    .nav-contest, .nav-contest.show{
      height: 80px;
    }
    .nav-contest li{
      margin-right: 7px;
      width: 5.95em;
    }
    .nav-contest li.slide{
      display: block;
      height: calc(1.7em + 1.025em);
      border-bottom: 4px solid #17bf63;
      border-radius: 2px;
      transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1.05);
      left: 0;
    }
    .nav-contest li.active{
      display: inline-block;
    }
    .nav-contest li.active a{
      color: #17bf63;
    }
    .tab-contest{
      max-width: calc(100vw - 60px);
    }
  }
  .fade-enter-active,.fade-leave-active{
    transition: opacity .25s;
  }

  .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
    opacity: 0;
  }

  .component-fade-enter-active, .component-fade-leave-active {
    transition: opacity .3s ease;
  }
  .component-fade-enter, .component-fade-leave-to
    /* .component-fade-leave-active for below version 2.1.8 */ {
    opacity: 0;
  }
</style>

<style>
  table *{
    text-align: center;
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

  .border-radius{
    border-radius: 5px 5px 5px 5px;
  }
  .tab-contest{
    overflow-x: auto;
  }
  .outline-none-search input{
    border: 1px solid #dadce0;
    background-color: white;
    border-radius: 13px!important;
    padding-left: 2.35em;
    box-sizing: border-box;
    height: 2rem;
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
    z-index: 1050;
    width: 23px;
    top: 1px;
    left: .6em;
  }
  .down-select-search input{
    cursor: pointer;
  }
  .down-select-search div:last-child{
    display: none;
    top: 2rem;
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
</style>
