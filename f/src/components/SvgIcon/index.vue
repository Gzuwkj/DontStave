<template>
  <svg :class="`svg-icon ${iconClass}`" aria-hidden="true">
    <use :xlink:href="`#${iconName}`" />
  </svg>
</template>

<script>
  export default {
    name: "SvgIcon",
    props: {
      iconClass: {
        type: String,
        default: ``
      },
      iconName: {
        type: String,
        default: ``
      }
    },
  }
</script>

<style scoped>
  .svg-icon {
    width: 1.15em;
    height: 1.15em;
    vertical-align: middle;
    fill: currentColor;
    overflow: hidden;
  }
</style>
