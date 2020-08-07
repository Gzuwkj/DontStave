<template>
  <div class="container px-0" style="display: block">
    <div class="white" v-html="contest.info" />
  </div>
</template>

<script>
    export default {
      props: {
        contest: {
          type: Object,
          required: true
        },
        problems: {
          type: Array,
          required: true
        }
      },
    }
</script>

<style scoped>
.white{
  padding: 1em;
  background: rgba(220, 221, 225, 0.5);
  border-radius: 5px;
}
</style>
