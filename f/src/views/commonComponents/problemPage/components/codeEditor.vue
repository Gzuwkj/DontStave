<template>
  <div class="px-0 pt-5 bg-white position-relative" id="codeEditor">
    <div @click.stop="downSelect($event)" class="position-absolute input-group col-4 col-md-3 col-lg-2 px-1 outline-none-search down-select-search">
      <label>
        <input type="text" placeholder="语言" class="form-control" readonly>
      </label>
      <div class="input-group-prepend">
        <svg viewBox="0 0 1024 1024" width="30" height="30">
          <path fill="#dadce0" d="M821.020444 341.333333c27.818667 0 42.552889 36.067556 24.177778 58.936889L536.177778 784.497778a30.378667 30.378667 0 0 1-48.355556 0L178.801778 400.270222C160.426667 377.400889 175.217778 341.333333 202.979556 341.333333h618.040888z"/>
        </svg>
      </div>
      <div class="position-absolute w-100 bg-white shadow-sm">
        <ul class="d-flex flex-column align-items-center p-0 m-0">
          <li>C</li>
          <li>C++</li>
          <li>Java</li>
        </ul>
      </div>
    </div>
    <codemirror v-model="code" :width="'100%'" :height="'calc(100vh - 175px - 4rem)'" :language="language.mime" />
    <div class="position-relative submit-status-box">
      <div class="position-absolute submit-status px-1">
        <svg viewBox="0 0 1024 1024" width="20" height="20">
          <path fill="rgb(45, 52, 54)" d="M821.020444 341.333333c27.818667 0 42.552889 36.067556 24.177778 58.936889L536.177778 784.497778a30.378667 30.378667 0 0 1-48.355556 0L178.801778 400.270222C160.426667 377.400889 175.217778 341.333333 202.979556 341.333333h618.040888z"/>
        </svg>
        <div class="w-100 pt-1">
          <div class="alert alert-success m-0" role="alert">
            A simple success alert—check it out!
          </div>
        </div>
      </div>
      <button class="position-absolute btn btn-green" @click="submit">提交代码</button>
    </div>
  </div>
</template>

<script>
  import {codemirror} from "@/components/codeMirror";
  import request from '@/utils/request'
  const language = {'c': `text/x-csrc`, 'c++':  `text/x-c++src`, 'java':  `text/x-java`};

  export default {
    name: "codeEditor",
    props: {
      problem: {
        type: Object,
        required: true
      }
    },
    data(){
      return {
        language:  {
          label: ``,
          mime: `text/x-csrc`
        },
        code: ``
      }
    },
    components: {
      codemirror
    },
    methods: {
      downSelect(event){
        const target = event.srcElement || event.target;
        const node = $(event.currentTarget);
        if(target.nodeName === 'LI'){
          node.children('label').children('input').attr('value', $(target).text());
          this.language.mime = language[$(target).text().toLowerCase()];
          this.language.label = $(target).text();
        }
        node.children('div:last-child').toggleClass('show');
      },
      submit(){
        request({
          url: this.$route.fullPath.replace(/\?.*/, ``),
          method: 'post',
          data: {
            language: this.language.label,
            code: this.code
          }
        }).then(data => {
          console.log(data);
        })
      }
    },
  }
</script>

<style scoped>
  #codeEditor{
    border: 1px solid #dadce0;
    border-radius: 0 5px 5px 0;
  }
  @media (min-width: 768px) {
    #problem{
      border-radius: 5px;
    }
    #codeEditor{
      border-radius: 5px;
    }
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
    left: .5rem;
    top: .5rem;
  }
  .outline-none-search .input-group-prepend{
    position: absolute;
    background: transparent;
    z-index: 5;
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
    z-index: 5;
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
  .submit-status-box{
    height: 60px;
  }
  .btn.btn-green{
    right: 1rem;
    top: 50%;
    transform: translateY(-50%);
    display: flex;
    justify-content: center;
    align-items: center;
    height: 2.25rem;
    width: 8.75rem;
    background: #17bf63;
    color: white;
  }
  .submit-status{
    height: 0;
    width: 100%;
    left: 0;
    z-index: 5;
    bottom: 60px;
    border-radius: 5px 5px 0 0;
    border-top: 1px solid #dadce0;
    background: white;
    display: flex;
    transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1.05);
  }
  .submit-status svg{
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    position: absolute;
    background: white;
    border: 1px solid #dadce0;
    height: 1rem;
    width: 2rem;
    border-radius: 3px 3px 0 0;
    transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1.05);

  }
  .submit-status div{
    visibility: hidden;
    transition-delay: 0s;
    transition: 0s;
  }
  .submit-status.show{
    height: 75px;
  }
  .submit-status.show svg{
    bottom: 75px;
  }
  .submit-status.show div{
    visibility: visible;
    transition-delay: .25s;
    transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1.05);
  }

</style>
