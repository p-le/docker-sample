<template>
  <a href="https://www.youtube.com/channel/UCRWDR9vuoRny63i464-pZrg" target="_blank"> 
    <img alt="Vue logo" src="./assets/logo.jpg" />
  </a>
  <Playlist msg="Chào mừng anh em đến với FullstacKAGE" :playlists="playlists"/>
</template>

<script>
import Playlist from "./components/Playlist.vue";
import axios from 'axios';

export default {
  name: "App",
  components: {
    Playlist
  },
  data() {
    return {
      playlists: []
    };
  },
  mounted () {
    axios
      .get('http://localhost:9000/playlists')
      .then(response => this.playlists = response.data.playlists)
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 100%
}
</style>
