<template>
  <div :style="{height, width}">
    <textarea ref="textarea" :input="$emit(`input`, this.value)"/>
  </div>
</template>

<script>
  import _CodeMirror from 'codemirror'
  import 'codemirror/mode/clike/clike.js'
  import './setting.js'

  const codemirror = window.CodeMirror || _CodeMirror;
  export default {
    model: {
      prop: 'content',
      event: 'input'
    },
    props: {
      height: {
        type: String,
        default: () => `100%`
      },
      width: {
        type: String,
        default: () => `100%`
      },
      content: {
        type: String,
        default: () => ``
      },
      language: {
        type: String,
        default: () => `text/x-c++src`
      }
    },
    data () {
      return {
        value: this.content,
        coder: null,
        options: {
          tabSize: 2, // tab
          lineNumbers: true, // 显示行号
          styleSelectedText: true,
          scrollbarStyle: 'overlay',
          line: true,
          foldGutter: true, // 块槽
          gutters: ['CodeMirror-linenumbers', 'CodeMirror-foldgutter'],
          highlightSelectionMatches: { showToken: /\w/, annotateScrollbar: true }, // 可以启用该选项来突出显示当前选中的内容的所有实例
          // hint.js options
          // 快捷键 可提供三种模式 sublime、emacs、vim
          keyMap: 'sublime',
          matchBrackets: true,
          showCursorWhenSelecting: true,
          theme: 'darcula', // 主题
          extraKeys: { 'Ctrl': 'autocomplete' }, // 可以用于为编辑器指定额外的键绑定，以及keyMap定义的键绑定
          cursorHeight: 1,
          autoCloseBrackets: true,
        }
      }
    },
    mounted () {
      // 初始化
      this._initialize()
    },
    methods: {
      // 初始化
      _initialize () {
        // 初始化编辑器实例，传入需要被实例化的文本域对象和默认配置
        this.coder = codemirror.fromTextArea(this.$refs.textarea, this.options);
        // 编辑器赋值
        this.coder.setValue(this.content || this.value);
        this.coder.setSize(`100%`, `100%`);
        this.coder.setOption('mode', this.language);
        // 支持双向绑定
        this.coder.on('change', (coder) => {
          this.value = coder.getValue();
        });
      }
    },
    watch: {
      language(value){
        this.coder.setOption('mode', value);
      }
    }
  }
</script>

<style scoped>

</style>
