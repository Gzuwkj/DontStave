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
          <div v-for="i in contests" :key="i.id" class="card mt-3 card-contest">
            <div class="row no-gutters">
              <div class="col-md-12">
                <div class="card-body position-relative">
                  <h4 class="card-title d-flex align-items-center mb-3">
                    <svg class="mr-3" viewBox="0 0 1024 1024" width="21" height="22">
                      <path v-if="i.is_lock" fill="#e74c3c" d="M696.980645 399.690323H327.019355v-99.096775c0-99.096774 82.580645-181.677419 184.980645-181.677419 102.4 0 184.980645 82.580645 184.980645 181.677419v99.096775z m-142.03871 350.141935v102.4c0 6.606452-3.303226 9.909677-9.909677 9.909677h-62.76129c-6.606452 0-9.909677-3.303226-9.909678-9.909677v-102.4c-29.729032-16.516129-49.548387-46.245161-49.548387-79.277419 0-49.548387 42.941935-89.187097 92.490323-89.187097 49.548387 0 92.490323 39.63871 92.490322 89.187097-3.303226 36.335484-23.122581 66.064516-52.851613 79.277419z m343.535484-350.141935h-85.883871V293.987097C812.593548 132.129032 677.16129 0 512 0S211.406452 132.129032 211.406452 293.987097V396.387097H125.522581c-39.63871 0-72.670968 33.032258-72.670968 72.670968v478.967741c0 39.63871 33.032258 72.670968 72.670968 72.670968h772.954838c39.63871 0 72.670968-33.032258 72.670968-72.670968V472.36129c0-42.941935-33.032258-72.670968-72.670968-72.670967z"/>
                      <path v-if="!i.is_lock" fill="#17bf63" d="M874.666667 401.066667h-529.066667v-153.6c0-76.8 76.8-145.066667 170.666667-145.066667s170.666667 68.266667 170.666666 145.066667v8.533333c0 25.6 25.6 51.2 51.2 51.2s51.2-25.6 51.2-51.2c0-153.6-128-256-281.6-256-153.6 0-281.6 102.4-281.6 256v136.533333h-76.8c-42.666667 0-68.266667 34.133333-68.266666 68.266667v494.933333c0 42.666667 34.133333 68.266667 68.266666 68.266667h716.8c42.666667 0 68.266667-34.133333 68.266667-68.266667v-494.933333c8.533333-34.133333-17.066667-59.733333-59.733333-59.733333z m-315.733334 324.266666v110.933334c0 8.533333-8.533333 8.533333-8.533333 8.533333h-59.733333c-8.533333 0-8.533333-8.533333-8.533334-8.533333v-110.933334c-34.133333-17.066667-51.2-42.666667-51.2-68.266666 0-42.666667 42.666667-85.333333 85.333334-85.333334s85.333333 42.666667 85.333333 85.333334c0 34.133333-17.066667 59.733333-42.666667 68.266666z" />
                    </svg>
                    Round {{ i.id }} : {{ i.title }}
                  </h4>
                  <div class="d-flex flex-md-row flex-column">
                    <div class="mb-2 mr-3 d-flex align-items-center text-dark">
                      <svg class="mr-2" viewBox="0 0 1024 1024" width="18" height="18">
                        <path fill="currentColor" d="M36.162 988.38h951.676c20.286 0 36.162-15.994 36.162-36.43V138.957c0-20.436-15.876-36.43-36.162-36.43H808.792V71.43C808.792 50.993 792.916 35 772.63 35c-20.285 0-36.161 15.993-36.161 36.43v31.097H293.705V71.43C293.705 50.993 277.83 35 257.543 35c-20.285 0-36.161 15.993-36.161 36.43v31.097H36.162C15.876 102.527 0 118.521 0 138.957v813.882c0 19.547 16.758 35.54 36.162 35.54z m36.162-812.994h149.058v19.547c0 20.436 15.876 36.43 36.161 36.43 20.286 0 36.162-15.994 36.162-36.43v-19.547H736.47v19.547c0 20.436 15.876 36.43 36.161 36.43 20.286 0 36.162-15.994 36.162-36.43v-19.547h143.766v94.183H72.324v-94.183z m0 167.041h879.352V916.41H72.324V342.427zM772.63 509.468H252.252c-20.286 0-36.162 15.994-36.162 36.43 0 20.435 15.876 36.429 36.162 36.429H772.63c20.286 0 36.162-15.994 36.162-36.43 0-20.435-15.876-36.429-36.162-36.429zM512.441 685.395h-260.19c-20.285 0-36.161 15.993-36.161 36.43 0 20.435 15.876 36.428 36.162 36.428H512.44c20.286 0 36.162-15.993 36.162-36.429s-15.876-36.43-36.162-36.43z" />
                      </svg>
                      开始时间 : {{ (i.startTime || new Date()).format('yyyy-MM-dd HH:mm:ss') }}
                    </div>
                    <div class="mb-2 mr-3 d-flex align-items-center text-dark">
                      <svg class="mr-2" viewBox="0 0 1024 1024" width="18" height="18">
                        <path fill="currentColor" d="M512.049966 1023.300478c-282.57983 0-511.650239-229.078403-511.650239-511.650239s229.070409-511.650239 511.650239-511.650239c282.571836 0 511.650239 229.078403 511.650239 511.650239s-229.078403 511.650239-511.650239 511.650239z m0-965.319114c-250.551724 0-453.668875 203.116151-453.668875 453.667876 0 250.552724 203.11715 453.669874 453.668875 453.669874 250.552724 0 453.668875-203.11715 453.668875-453.668875 0-250.552724-203.11715-453.668875-453.668875-453.668875z m262.08584 581.956179c-7.046183 15.097679-25.033887 21.584245-40.130567 14.507083l-240.434641-80.381052c-11.499139-5.367331-17.898765-17.045348-17.250208-28.985186-0.147899-1.209173-0.707516-2.211488-0.707516-3.449642V209.488795c0-16.689591 13.504768-30.194359 30.194359-30.19436s30.194359 13.504768 30.19436 30.19436v315.50832l223.598149 74.777883c15.12666 7.077162 21.614225 25.034886 14.536064 40.162545z" />
                      </svg>
                      时长 : {{ i.length | date }}
                    </div>
                    <div class="mb-2 mr-3 d-flex align-items-center text-dark">
                      <svg class="mr-2" viewBox="0 0 1024 1024" width="18" height="18">
                        <path fill="currentColor" d="M761.6 301.653333c0-75.434667-28.501333-146.176-80.213333-199.424a268.117333 268.117333 0 0 0-387.157334 0 284.672 284.672 0 0 0-80.213333 199.424c0 58.453333 17.152 114.517333 49.664 162.133334a28.16 28.16 0 0 0 40.021333 7.168 30.208 30.208 0 0 0 6.997334-41.216c-25.6-37.632-39.253333-81.92-39.253334-128.085334 0-122.88 97.024-222.890667 216.32-222.890666 119.381333 0 216.405333 99.925333 216.405334 222.890666 0 122.88-97.024 222.976-216.405334 222.976-58.88 0-116.053333 11.776-170.069333 35.413334a434.944 434.944 0 0 0-138.922667 96.426666A448.256 448.256 0 0 0 85.162667 799.573333a459.52 459.52 0 0 0-34.389334 175.274667c0 16.384 12.8 29.610667 28.672 29.610667a29.098667 29.098667 0 0 0 28.757334-29.610667c0-215.552 170.24-390.997333 379.477333-390.997333a267.946667 267.946667 0 0 0 193.621333-82.602667 284.330667 284.330667 0 0 0 80.213334-199.594667z m173.397333 316.330667l-79.530666-82.005333a27.221333 27.221333 0 0 0-18.688-8.106667 25.514667 25.514667 0 0 0-18.602667 8.106667L579.754667 781.653333a27.904 27.904 0 0 0-7.850667 19.370667v82.005333c0 15.104 11.776 27.392 26.538667 27.392h79.616a25.941333 25.941333 0 0 0 18.602666-8.277333l238.506667-245.674667a27.904 27.904 0 0 0-0.170667-38.485333z m-261.973333 253.44h-63.146667v-65.621333l151.04-155.648 63.402667 65.365333-151.210667 155.904z m181.418667-186.965333l-63.402667-65.365334 45.909333-47.36 63.402667 65.450667-45.909333 47.274667z m94.976 312.661333H562.688a24.149333 24.149333 0 0 1-23.722667-24.490667c0-13.397333 10.666667-24.405333 23.722667-24.405333h386.730667c12.970667 0 23.722667 11.008 23.722666 24.405333a24.064 24.064 0 0 1-23.722666 24.490667z"/>
                      </svg>
                      发布 :<router-link :to="{name: 'userInfo', params: {user_id: i.owner.id}}" class="ml-1">{{ i.owner.username }}</router-link>
                    </div>
                    <div class="mb-2 mr-3 d-flex align-items-center text-dark">
                      <svg class="mr-2" viewBox="0 0 1024 1024" width="18" height="18">
                        <path fill="currentColor" d="M917.5 918.9c0-0.6-0.2-1.3-0.2-1.9l-0.2-1.3c0-3.1-0.4-6.2-1.1-9.2-17.4-141.3-109.7-263.4-243.1-321.8 78.3-54.1 124.7-141.9 124.3-235.4 2.9-100.9-50.8-195.5-140.3-246.8-89.4-51.3-200.4-51.3-289.8 0-89.4 51.4-143.1 145.9-140.2 246.9-0.4 93.5 46 181.4 124.5 235.4-132.1 57.8-224 178.2-242.7 317.9-1.4 4.2-2.1 8.6-2.2 13l0.2 3.2 0.2 0.4c-0.5 14.4 7.2 28 19.9 35.4 12.8 7.4 28.7 7.4 41.4 0 12.8-7.4 20.4-20.9 19.9-35.4l-0.2-0.4h0.9c17.4-154.7 146.4-274.8 306-285.1 5.7 0.4 11.4 0.6 17.1 0.6 5.9 0 11.6-0.2 17.3-0.6 159.6 10.3 288.6 130.4 306 285.1h0.9v0.4c-0.5 14.4 7.2 28 19.9 35.4 12.8 7.4 28.7 7.4 41.5 0s20.4-20.9 19.9-35.4v-0.4zM308.4 349.6c2.9-106.4 91.6-191.5 201-192.9 109.4-1.4 200.3 81.5 206 187.8 5.7 106.3-75.9 197.9-184.8 207.7-6.1-0.2-12.3-0.4-18.4-0.4-6.1 0-12.5 0.2-18.6 0.4-106.2-11-186.4-98.7-185.2-202.6z m0 0" />
                      </svg>
                      人数 : {{ i.number }}
                    </div>
                  </div>
                  <div class="position-absolute card-link d-flex justify-content-center align-items-center">
                    <router-link :to="{name: 'contestContent', params: {contest_id: i.id}} " :class="i.is_finish ? 'secondary' : 'success'">{{ i.is_finish ? '回顾':'进入' }}</router-link>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Contest',
  filters: {
    date(value) {
      const hours = Math.floor(value / 60);
      value %= 60;
      return hours + (hours ? '小时' : '') + (value ? `${value}分钟` : '')
    }
  },
  data() {
    return {
      filter: 4,
      contests: []
    }
  },
  beforeRouteEnter(to, from, next) {
    axios.get(to.meta.path).then(res => {
      if (res.data.status === 200) {
        next(vm => {
          res.data.contest.forEach(item => {
            vm.contests.push({
              id: item.id,
              title: item.matchName,
              startTime: new Date(item.startTime),
              length: item.howLong,
              owner: item.owner,
              number: item.registerNum,
              is_lock: false,
              is_finish: item.status === 0
            })
          })
        })
      }
    }).catch(error => {
      if (error.status === 401) {
        this.$router.replace({ name: 'login' })
      }
    })
  },
  watch: {
    filter: function(New) {
      const dom = $(`#filter li:eq(${New})`);
      const pos = dom.position();
      const width = dom.width();
      $('#slide').css({ left: +pos.left, width: width });
      this.axios.get(this.$route.meta.path, {
        params: {
          contest_status: New
        }
      }).then(res => {
        if (res.status === 200) {
          this.contests = [];
          res.data.contest.forEach(item => {
            this.contests.push({
              id: item.id,
              title: item.matchName,
              startTime: new Date(item.startTime),
              length: item.howLong,
              owner: item.owner,
              number: item.registerNum,
              is_lock: false,
              is_finish: item.status === 0
            })
          })
        }
      })
    }
  },
  mounted() {
    const dom = $(`#filter li:last-child`);
    const pos = dom.position();
    const width = dom.width();
    $('#slide').css({ left: +pos.left, width: width })
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
  .card-link{
    height: 100%;
    right: 2em;
    top: 1.5em;
  }
  .card-link a{
    border-radius: 5px;
    display: flex;
    box-sizing: border-box;
    width: 5.5em;
    height: 2.45em;
    justify-content: center;
    align-items: center;
    text-decoration: none;
    transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1.05);
  }
  @media (min-width: 768px) {
    .card-link{
      top: 0;
      right: 5em;
    }
  }
  .card-link a.success{
    border: 1px solid #17bf63;
    color: #17bf63;
  }
  .card-link a.success:hover{
    background: rgba(79, 192, 141, 0.2);
  }
  .card-link a.secondary{
    border: 1px solid #bdc3c7;
    color: #bdc3c7;
  }
  .card-link a.secondary:hover{
    background: #ecf0f1;
  }
</style>
