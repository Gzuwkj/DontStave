<template>
  <div>
    <v-navbar @toggle-collapse="sidebarCollapse=!sidebarCollapse"/>
    <main class="position-relative">
      <v-sidebar :collapse="sidebarCollapse"/>
      <div class="main-content">
        <div class="draw-bg" :class="{active: sidebarCollapse}" @click="sidebarCollapse = false"/>
        <v-breadcrumb/>
        <v-appview/>
      </div>
    </main>
  </div>
</template>

<script>
  import { breadcrumb, navbar, sidebar, AppView } from './components'
  export default {
    name: "Layout",
    components: {
      'v-breadcrumb': breadcrumb,
      'v-navbar': navbar,
      'v-sidebar': sidebar,
      'v-appview': AppView
    },
    data: function () {
      return {
        sidebarCollapse: false,
      }
    },
    methods: {

    }
  }
</script>

<style scoped>
  body{
    min-height: 100vh;
    margin: 0;
    padding: 0;
    width: 100vw!important;
    background: #f1f2f6!important;
  }
  .main-content{
    max-height: calc(100vh - 60px);
    min-height: calc(100vh - 60px);
    max-width: calc(100vw - 0px);
    min-width: calc(100vw - 0px);
    overflow: hidden;
    margin-left: 0;
    position: relative;
  }
  @media (min-width: 768px) {
    .main-content{
      max-height: calc(100vh - 60px);
      min-height: calc(100vh - 60px);
      max-width: calc(100vw - 60px);
      min-width: calc(100vw - 60px);
      margin-left: 60px;
      overflow: hidden;
    }
  }
  .active.draw-bg{
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    background: rgba(0, 0, 0, 0.3);
    z-index: 4;
  }
</style>
