import Vue from 'vue'
import Router from 'vue-router'
/*
const contest = () =>import("../components/contest/contest");
const contestContent = () =>import("../components/contest/contestContent");
const login = () =>import("../components/login_register/login");
const register = () =>import("../components/login_register/register");
const contestProblem = () =>import("../components/contest/contestProblem");
const userInfo = () =>import("../components/uer/userInfo");
const problem = () =>import("../components/problem/problem");
const status = () =>import("../components/submit_status/status");
const contestProblemCode = () =>import("../components/contest/contestProblemCode");
*/
import Layout from "@/layout"

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    /*******************比赛模块路由****************/
    {
      path: '/',
      component: Layout,
      redirect: '/contest',
      name: 'contest',
      meta: {
        iconName: 'icon-contest',
        path: '/contest',
        name: '比赛',
      },
      children: [
        {
          path: 'contest',
          name: 'contestList',
          component: ()=> import('@/views/contest/contestList/index'),
        },
        {
          path: 'contest/:contest_id',
          name: 'contestPage',
          component: ()=> import('@/views/contest/contestPage/index'),
          meta: {
            allowAnonymous: false,
          }
        },
        {
          path: 'contest/:contest_id/problem/:problem_id',
          name: 'contestProblem',
          component: ()=>import('@/views/commonComponents/problemPage/index'),
          meta: {
            allowAnonymous: false,
          }
        },
        {
          path: 'contest/:contest_id/code/:run_id',
          name: 'contestCode',
          component: ()=>import('@/views/commonComponents/codePage'),
          meta: {
            allowAnonymous: false,
          }
        }
      ]
    },
    {
      path: '/problem/',
      component: Layout,
      redirect: '/problem/list',
      name: 'problem',
      meta: {
        iconName: 'icon-problems',
        path: '/problem/list',
        name: '题库',
      },
      children: [
        {
          path: 'list',
          name: 'problemList',
          component: ()=>import('@/views/problem/problemList'),
        },
        {
          path: 'list/problem/:problem_id',
          name: 'problemPage',
          component: ()=>import('@/views/commonComponents/problemPage/index'),
          meta: {
            allowAnonymous: false,
          }
        },
      ]
    },
    {
      path: '/submit/',
      component: Layout,
      redirect: '/submit/list',
      name: 'submit',
      meta: {
        iconName: 'icon-submits',
        path: '/submit/list',
        name: '提交记录',
      },
      children: [
        {
          path: 'list',
          name: 'submitList',
          component: ()=>import('@/views/submit/submitList'),
        },
        {
          path: 'list/code/:run_id',
          name: 'submitCode',
          component: ()=>import('@/views/commonComponents/codePage'),
          meta: {
            allowAnonymous: false,
          }
        }
      ]
    },
    {
      path: '/user/',
      component: Layout,
      name: 'user',
      redirect: '/user/login',
      children: [
        {
          path: 'login',
          name: 'login',
          component: () => import('@/views/user/login'),
        },
        {
          path: 'register',
          name: 'register',
          component: () => import('@/views/user/register'),
        },
        {
          path: ':user_id/info',
          name: 'userInfo',
          component: () => import('@/views/user/info'),
          meta: {
            allowAnonymous: false
          }
        }
      ]
    }
  ],
})


// `{
//   /**
//    * 比赛列表
//    */
//   path: '/contest/',
//     name: 'contest',
//   component: contest,
//   meta: {
//   name: '比赛列表',
//     path: '/contest/',
//     reg_path: '/contest/',
//     index: 1,
//     parent: undefined,
//     nameHandler: undefined,
// },
// },
// {
//   /**
//    * 比赛内容
//    */
//   path: '/contest/:contest_id/',
//     name: 'contestContent',
//   component: contestContent,
//   params: {contest_id: 1},
//   meta: {
//     name: 'Round ',
//       path: '/contest/:contest_id/',
//       reg_path: '/contest/:contest_id/',
//       index: 2,
//       parent: {path: '/contest/', name: 'contest'},
//     nameHandler:(name, params)=>{
//       return name + params['contest_id'];
//     }
//   },
// },
// {
//   /**
//    * 比赛题目
//    */
//   path: '/contest/:contest_id/problem/:problem_id/',
//     name: 'contestProblem',
//   component: contestProblem,
//   meta: {
//   name: '',
//     path: '/contest/:contest_id/problem/:problem_id/',
//     reg_path: '/contest/:contest_id/problem/:problem_id/',
//     index: 3,
//     parent: {path: '/contest/:contest_id/', name: 'contestContent'},
//   nameHandle: undefined,
// },
// },
// {
//   path: '/contest/:contest_id/status/:run_id/code/',
//     name: 'contestProblemCode',
//   component: contestProblemCode,
//   meta: {
//   name: '',
//     path: '/contest/:contest_id/status/:run_id/code/',
//     reg_path: '/contest/:contest_id/status/:run_id/code/',
//     index: 3,
//     parent: {path: '/contest/:contest_id/', name: 'contestContent'},
//   nameHandler: (name, params)=>{
//     return name + params['run_id'];
//   },
// },
// },
// /*******************用户操作路由***********************/
// {
//   path: '/login/',
//     name: 'login',
//   component: login,
//   meta: {
//   name: '登陆',
//     path: '/login/',
//     reg_path: '/login/',
//     index: 1,
//     parent: undefined,
//     nameHandle: undefined,
// }
// },
// {
//   path: '/register/',
//     name: 'register',
//   component: register,
//   meta: {
//   name: '注册',
//     path: '/register/',
//     reg_path: '/register/',
//     index: 1,
//     parent: undefined,
//     nameHandle: undefined,
// }
// },
// {
//   path: '/user/:user_id/',
//     name: 'userInfo',
//   component: userInfo,
//   meta: {
//   name: '个人中心',
//     path: '/user/:user_id/',
//     reg_path: '/user/:user_id/',
//     index: 1,
//     parent: undefined,
//     nameHandle: undefined,
// }
// },
// /*******************题库模块*******************************/
// {
//   /**
//    * 题目列表
//    */
//   path: '/problem/',
//     name: 'problem',
//   component: problem,
//   meta: {
//   name: '题库',
//     path: '/problem/',
//     reg_path: '/problem/',
//     index: 1, /* 一级目录 */
//     parent: undefined,
//     nameHandler: undefined,
// },
// },
// /*********************提交记录********************************/
// {
//   /**
//    * 提交记录
//    */
//   path: '/status/',
//     name: 'status',
//   component: status,
//   meta: {
//   name: '提交记录',
//     path: '/status/',
//     reg_path: '/status/',
//     index: 1, /* 一级目录 */
//     parent: undefined,
//     nameHandler: undefined,
// },
// },`;

// let constantRoutes = [
//   {
//     path: '/',
//     component: Layout,
//     redirect: '/contest',
//     children: {
//       path: 'contest',
//       component: ()=> import('../views/contest/index'),
//     }
//   }
// ];

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
});



