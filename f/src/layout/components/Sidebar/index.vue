<template>
  <nav class="main-menu" :class="{'active': collapse}">
    <ul>
      <template v-if="is_login">
        <li class="d-flex d-md-none">
          <router-link to="#">
            <i class="fa fa-2x">
              <svg-icon icon-name="icon-profile"/>
            </i>
            <span class="nav-text">个人中心</span>
          </router-link>
        </li>
<!--        <li class="d-flex d-md-none">-->
<!--          <a href="#">-->
<!--            <i class="fa fa-2x">-->
<!--              <svg-icon icon-name="icon-setting"/>-->
<!--            </i>-->
<!--            <span class="nav-text">设置</span>-->
<!--          </a>-->
<!--        </li>-->
      </template>
      <template v-else>
        <li class="login d-flex d-md-none justify-content-center align-items-center">
          <router-link :to="{name: 'login'}" >
            登陆 / 注册
          </router-link>
        </li>
        <hr class="d-block d-md-none">
      </template>
      <li v-for="route in routes" :key="route.id">
        <bar-item :route="route"/>
      </li>

    </ul>
  </nav>
</template>

<script>
  import BarItem from "./BarItem";
  import {mapGetters} from "vuex";
  export default {
    props: {
      collapse: {
        type: Boolean,
        default: false
      }
    },
    computed: {
      ...mapGetters([
        'user',
        'is_login',
        'routes',
      ])
    },
    components: {
      'bar-item': BarItem,
    },
  }
</script>

<style>
  .fa-2x {
    font-size: 2em;
  }
  .fa {
    position: relative;
    display: table-cell;
    width: 60px;
    height: 43px;
    text-align: center;
    vertical-align: middle;
    font-size:20px;
  }
  .main-menu:hover,nav.main-menu.expanded,.main-menu.active:hover, nav.main-menu.active.expanded {
    width:250px;
    overflow-x:hidden;
    overflow-y: auto;
  }
  .main-menu {
    background:#fff;
    position:absolute;
    top:0;
    bottom:0;
    height:100%;
    z-index: 10;
    left:0;
    width:0;
    overflow-x:hidden;
    overflow-y: auto;
    transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1.05);
    border-right: 1px solid #dadce0;
    border-top: 1px solid #dadce0;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .main-menu>ul {
    margin:7px 0;
  }
  .main-menu li {
    position:relative;
    display:block;
    width:250px;
  }
  .main-menu li>a {
    position:relative;
    display:table;
    border-collapse:collapse;
    border-spacing:0;
    color:#8a8a8a;;
    font-family: arial,serif;
    font-size: 14px;
    text-decoration:none;
    transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1.05);
  }
  .main-menu .nav-text {
    display:table-cell;
    vertical-align:middle;
    width:190px;
    font-size: 1.05rem;
  }

  a:hover,a:focus {
    text-decoration:none;
  }
  nav {
    user-select:none;
  }
  nav ul,nav li {
    outline:0;
    margin:0;
    padding:0;
  }
  .main-menu li:hover>a,nav.main-menu li.active>a,.dropdown-menu>li>a:hover,.dropdown-menu>li>a:focus,.dropdown-menu>.active>a,.dropdown-menu>.active>a:hover,.dropdown-menu>.active>a:focus,.no-touch .dashboard-page nav.dashboard-menu ul li:hover a,.dashboard-page nav.dashboard-menu ul li.active a {
    color:#17bf63;
    background-color: rgba(79, 192, 141, 0.2);
    text-shadow: 0 0 0;
  }
  hr{
    display: block;
    unicode-bidi: isolate;
    margin-block-start: 0.5em;
    margin-block-end: 0.5em;
    margin-inline-start: auto;
    margin-inline-end: auto;
    overflow: hidden;
  }
  .main-menu.active{
    width: 250px;
  }
  @media (min-width: 768px) {
    .main-menu, .main-menu.active{
      width: 60px;
    }
  }
  li.login{
    height: 60px;
  }
  li.login a{
    display: block;
    font-size: 1.1em;
    padding: .5em .7em;
  }
</style>
