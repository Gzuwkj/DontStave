<template>
  <div>
    <h6><b><slot/></b></h6>
    <hr>
    <div class="paragraph-content px-2 pt-2 pb-1" v-html="content" />
  </div>
</template>

<script>
  export default {
    name: "paragraph",
    props: {
      content: {
        type: String,
        default: () => ``,
      }
    }
  }
</script>

<style scoped>
.paragraph-content{
  background: rgba(220, 221, 225, .7);
  border-radius: 4px;
  border-left: 3px solid #17bf63;
  }
</style>
