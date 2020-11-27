<template>
  <div class="hello">
    <h2 class="title">{{ msg }}</h2>
    <p class="subtitle">Demo Spotify API - Docker</p>
    <span class="playlist" v-for="(playlist, idx) in playlists" v-bind:key="idx">
      <iframe v-bind:src="playlist" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
    </span>
  </div>
</template>

<script>


export default {
  name: "Playlist",
  props: {
    msg: String,
    playlists: Array
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.playlist {
  margin: 15px 10px;
}
</style>
