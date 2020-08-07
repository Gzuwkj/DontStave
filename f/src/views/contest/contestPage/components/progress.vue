<template>
  <div class="container px-0">
    <div class="w-100 bg-white py-3 my-3">
      <div class="mb-3 d-flex justify-content-between">
        <div class="col-3 d-none d-md-flex justify-content-center align-items-center">
          <span class="font-weight-bolder mr-1">开始时间 :</span>
          {{ contest.startTime | formatDate('yyyy-MM-dd HH:mm:ss')}}
        </div>
        <div class="col-12 d-flex col-md-3 justify-content-center flex-wrap">
          <h4 class="mr-2">Round {{contest.id}} :</h4>
          <h4>{{contest.title}}</h4>
        </div>
        <div class="col-3 col-3 d-none d-md-flex justify-content-center align-items-center">
          <span class="font-weight-bolder mr-1">结束时间 :</span>
          {{ contest.endTime | formatDate('yyyy-MM-dd HH:mm:ss')}}
        </div>
      </div>
      <div class="progress mx-3">
        <div class="progress-bar" :class="progressColor" role="progressbar" :style="{width: progress + '%'}" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"/>
      </div>
    </div>
<!--    {{progress }}-->
  </div>
</template>

<script>
  export default {
    props: {
      contest: {
        type: Object,
        required: true,
      },
    },
    data(){
      return {
        timer: {
          progress: 0,
          timer: null
        }
      }
    },
    mounted() {
      this.timer.timer = setInterval(() => {
        this.timer.progress = Math.max(Math.min((new Date().getTime() - this.contest.startTime.getTime())/(10 * 60 * this.contest.length), 100), 0);
        this.timer.progress = isNaN(this.timer.progress) ? 0 : this.timer.progress;
      }, 1000);
    },
    computed: {
      progressColor(){
        if(this.timer.progress < 50) return "bg-success";
        else if(this.timer.progress >= 50 && this.timer.progress <= 75) return "bg-warning";
        else if(this.timer.progress > 75) return "bg-danger";
      },
      progress(){
        return this.timer.progress ||
          Math.max(Math.min((new Date().getTime() - this.contest.startTime.getTime())/(10 * 60 * this.contest.length), 100), 0);
      }
    },
    watch: {
      timer: {
        handler(value){
          if(value.progress >= 100) {
            clearInterval(this.timer.timer);
          }
        },
        deep: true,
      }
    },

  }
</script>

<style scoped>
  .progress{
    height: .85em;
  }
</style>
