<template>
  <div class="w-100 px-0">
    <div class="container px-0 pt-2 pb-3 d-flex justify-content-center">
      <span>距离比赛开始还有:</span>
    </div>
    <div class="container px-0 timer-contest d-flex justify-content-center">
      <ul class="p-0 d-flex justify-content-between">
        <li class="bg-white d-flex flex-column"><div>{{clock.days}}</div><small>天</small></li>
        <li class="bg-white d-flex flex-column"><div>{{clock.hours}}</div><small>小时</small></li>
        <li class="bg-white d-flex flex-column"><div>{{clock.minutes}}</div><small>分钟</small></li>
        <li class="bg-white d-flex flex-column"><div>{{clock.seconds}}</div><small>秒</small></li>
      </ul>
    </div>
    <div class="container px-0 d-flex justify-content-center">
      <router-link to="#" class="btn btn-green">立即报名</router-link>
    </div>
  </div>
</template>

<script>
    export default {
      props: {
        contest: {
          type: Object,
          required: true
        }
      },
      data(){
        return {
          timer: null,
          ms: -1,
        }
      },
      mounted() {
        this.timer = setInterval(() => {
            this.ms = Math.max(0, this.contest.startTime.getTime() - new Date().getTime());
          },
          1000);
      },
      computed: {
        clock(){return this.getClock(this.ms)},
      },
      methods: {
        parse(value){
          if(value >= 10) return value;
          else return `0${value}`;
        },
        getClock(ms){
          let p = [24, 60, 60, 1];
          const keys = [`days`, `hours`, `minutes`, `seconds`];
          ms = Math.max(Math.floor(ms / 1000), 0);
          let ret = {
            days: `00`,
            hours: `00`,
            minutes: `00`,
            seconds: `00`,
          }, i = 0;
          while (ms > 0){
            let t = p.reduce((l, r) => l * r, 1);
            ret[keys[i]] = this.parse(Math.floor(ms / t));
            ms %= t;
            p[i++] = 1;
          }
          return ret;
        }
      },
      watch: {
        ms(value){
          if(value <= 0){
            clearInterval(this.timer);
          }
        }
      }
    }
</script>

<style scoped>
  @font-face {
    font-family: 'Pathway Gothic One';
    font-style: normal;
    font-weight: 400;
    src: local('Pathway Gothic One Regular'), local('PathwayGothicOne-Regular');
    unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;
  }
  /* latin */
  @font-face {
    font-family: 'Pathway Gothic One';
    font-style: normal;
    font-weight: 400;
    src: local('Pathway Gothic One Regular'), local('PathwayGothicOne-Regular');
    unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
  }
  .timer-contest ul{
    max-width: calc(5.95rem*4 + .99rem);
    width: calc(5.95rem*4 + .99rem);
    min-width: calc(5.95rem*4);
  }
  .timer-contest ul li{
    list-style: none;
    color: #17bf63;
    width: 5.95rem;
    height:7.95rem;
    border-radius: 7px;
    overflow: hidden;
    box-sizing: border-box;
    border: 1px solid #dadce0;
    font-family: Pathway Gothic One,serif;
  }
  .timer-contest ul li div{
    width: 100%;
    height: 5.5rem;
    font-size: 3.85rem;
    font-weight: 400;
    text-align: center;
  }
  .timer-contest ul li small{
    font-size: 1.25rem;
    height: calc(7.95rem - 5.5rem + .1rem);
    text-align: center;
    color: white;
    background: rgba(79, 192, 141, 0.55);
  }
  .btn.btn-green{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 2.25rem;
    max-width: calc(5.95rem*4 + .99rem);
    width: calc(5.95rem*4 + .99rem);
    min-width: calc(5.95rem*4);
    background: #17bf63;
    color: white;
  }
  .btn.btn-green.active{
    background:#b2bec3;
  }
</style>
