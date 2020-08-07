<template>
  <pre><code ref="codeBlock">{{content}}</code></pre>
</template>

<script>
  import hljs from 'highlight.js'
  import { hljsLineNumber } from './highlightjs-line-numbers'
  hljsLineNumber(window, document, hljs);
  import 'highlight.js/styles/github.css'
  export default {
    name: "index",
    props: {
      content: {
        type: String,
        default: () => ``,
      }
    },
    mounted() {
      hljs.highlightBlock(this.$refs.codeBlock);
      hljs.initLineNumbersOnLoad();
    },
  }
</script>

<style>
  td.hljs-ln-numbers {
    -webkit-touch-callout: none;
    -webkit-user-select: none;
    -khtml-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    text-align: center;
    border-right: 1px solid #CCC;
    vertical-align: top;
    width: 2rem;
    padding: 0 .5rem;
    color: gray;
    font-weight: 600;
  }
  td.hljs-ln-code{
    padding-left: .5rem;
  }
  table.hljs-ln{
    width: 100%;
  }
  .hljs tbody tr:nth-child(even){
    background: white;
  }
  .hljs tbody tr:nth-child(even) td:first-child{
    background: #f8f8f8;
  }
</style>
