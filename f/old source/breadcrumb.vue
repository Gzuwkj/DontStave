<template>
  <nav id="breadcrumb" aria-label="breadcrumb">
    <ol class="breadcrumb bg-white mb-0 border-bottom">
      <li class="breadcrumb-item" :class="{'active': index === breadcrumbList.length - 1}" v-for="(i,index) in breadcrumbList" :key="index">
        <router-link v-if="index !== breadcrumbList.length - 1" :to="i.path" class="text-green">{{i.name}}</router-link>
        <span v-else>{{i.name}}</span>
      </li>
    </ol>
  </nav>
</template>

<!--面包屑导航-->
<script>
  import router from "@/router";

  export default {
    name: "breadcrumb",
    data(){
      return {
        breadcrumbList:[]
      }
    },
    watch: {
      $route(to, from){
        // if(this.breadcrumbList.length !== 0){
        //   if(!to.meta.parent){
        //     this.breadcrumbList = [];
        //     this.breadcrumbList.push(this.getBreadcrumbItem(to, this.$route.params))
        //   }
        //   else{
        //     if(this.breadcrumbList.length >= to.meta.index){
        //       this.breadcrumbList = this.breadcrumbList.filter(item=>item.index < to.meta.index);
        //     }
        //     this.breadcrumbList.push(this.getBreadcrumbItem(to, this.$route.params));
        //   }
        // }
        // else {
        //
        // }
        let _route = this.$route;
        this.breadcrumbList = [];
        while (1){
          this.breadcrumbList.unshift(this.getBreadcrumbItem(_route, this.$route.params));
          if(!_route.meta.parent) break;
          _route = router.matcher.match(_route.meta.parent.path);
        }
      }
    },
    methods: {
      getBreadcrumbItem(_route, params){
        return {
          name:
            _route.meta.nameHandler ? _route.meta.nameHandler(_route.meta.name, params) : _route.meta.name,
          path: (()=>{
            for(let key in params)
              _route.meta.path = _route.meta.path.replace(':'+key, params[key]);
            return _route.meta.path;
          })(),
          index: _route.meta.index,
          parent: _route.meta.parent,
        }
      }
    }
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
