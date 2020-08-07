<template>
  <router-link :to="`${route.meta.path}`" >
    <i class="fa fa-2x">
      <svg-icon :icon-name="`${route.meta.iconName}`"/>
    </i>
    <span class="nav-text">{{route.meta.name}}</span>
  </router-link>
</template>

<script>
    export default {
      props: {
        route: {
          type: Object,
          default: ()=>{
            return {
              meta: {
                name: 'default name',
                path: '#',
                iconName: 'icon-default'
              }
            }
          },
        }
      },
    }
</script>
