<template>
  <nav id="breadcrumb" aria-label="breadcrumb">
    <ol class="breadcrumb bg-white mb-0 border-bottom">
<!--      <li class="breadcrumb-item" :class="{'active': index == breadcrumbList.length - 1}" v-for="(i,index) in breadcrumbList" :key="index">-->
<!--        <router-link v-if="index != breadcrumbList.length - 1" :to="i.path" class="text-green">{{i.name}}</router-link>-->
<!--        <span v-else>{{i.name}}</span>-->
<!--      </li>-->
    </ol>
  </nav>
</template>

<script>
    export default {
    }
</script>

<style scoped>
  #breadcrumb{
    border-top: 1px solid #dadce0;
    font-size: 1rem;
    height: 55px;
  }
  #breadcrumb ol{
    height: 100%;
    box-sizing: border-box;
  }
  .breadcrumb-item.active{
    color: #273849;
  }
  .text-green{
    color: #17bf63;
  }
  .breadcrumb-item.active .text-green{
    color: #273849;
  }
</style>
