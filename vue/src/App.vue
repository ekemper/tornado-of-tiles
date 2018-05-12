<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>

html {
  height: 100%;
}

body {
  margin:0;
  padding:0;
  width:100%;
  height: 100%;
  min-height: 100%;
}

#app {
  background-color: #424242;
  height: 100%;
}

</style>

<style lang="scss">
  @import '../node_modules/bootstrap/scss/bootstrap.scss';
</style>
