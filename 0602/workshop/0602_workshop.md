# 0602_workshop

## index.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <link rel="icon" href="<%= BASE_URL %>favicon.ico">
    <title><%= htmlWebpackPlugin.options.title %></title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
  </head>
  <body>
    <noscript>
      <strong>We're sorry but <%= htmlWebpackPlugin.options.title %> doesn't work properly without JavaScript enabled. Please enable it to continue.</strong>
    </noscript>
    <div id="app"></div>
    <!-- built files will be auto injected -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
  </body>
</html>

```

## SearchBar.vue

```vue
<template>
  <div>
      <input type="text" @keypress.enter="onInput">
  </div>
</template>

<script>
export default {
    name: 'SearchBar',
    methods: {
        onInput(event) {
            // 아래 코드는 개발자도구에서 직접 코드 찍어가면서 위치를 찾아준 것!
            // console.log(event.target.value)
            this.$emit('input-change', event.target.value)
        }
    }
}
</script>

<style scoped>
input {
    width: 75%;
}

div {
    text-align: center;
    margin: 20px;
}


</style>
```

## VideoDetail.vue

```vue
<template>
<div v-if="video" class="col-lg-8">
    <div class="embed-responsive embed-responsive-16by9">
        <iframe class="embed-responsive-item" type="text/html" :src="videoUrl" frameborder="0"></iframe>
    </div>
    <div class="details">
        <h4 v-html="video.snippet.title"></h4>
        <p v-html="video.snippet.description"></p>
    </div>
</div>
</template>

<script>
export default {
    name: 'VideoDetail',
    props: {
        video: {
            type: Object,
        }
    },
    computed: {
        videoUrl() {
            const videoId = this.video.id.videoId
            return `https://www.youtube.com/embed/${videoId}`
        } 
    }
}
</script>

<style scoped>
.details {
    margin-top: 10px;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
}
</style>
```

## VideoList.vue

```vue
<template>
  <ul classs="list-group col-lg-4">
    <VideoListItem v-for="video in videos" :key="video.etag" :video="video"
    @video-select="onVideoSelect"/>
  </ul>
</template>

<script>
import VideoListItem from '@/components/VideoListItem.vue'


export default {
  name: 'VideoList',
  components: {
    VideoListItem
  },
  props: {
    videos: {
      type: Array
    }
  },
  methods: {
    onVideoSelect(video) {
      this.$emit('video-select', video)
    }
  }
}
</script>

<style>

</style>
```

## VideoListItem.vue

```vue
<template>
    <li @click="onVideoSelect" class="list-group-item">
        <img :src="thumbnailUrl" alt="youtube-thumbnail-img">
        <div class="media-body" v-html="video.snippet.title"></div>
    </li>
</template>

<script>
export default {
  name: 'VideoListItem',
  props: {
    video: {
      type: Object
    }
  },
  computed: {
    thumbnailUrl() {
      return this.video.snippet.thumbnails.default.url
    }
  },
  methods: {
    onVideoSelect() {
      this.$emit('video-select', this.video)
    }
  }
}
</script>


<style scoped>
li {
    display: flex;
    cursor: pointer;
}

li:hover {
    background-color: #eee;
}

.media-body {
    margin: auto 0;
}
</style>
```

## App.vue

```vue
<template>
  <div class="container">
    <SearchBar @input-change="onInputChange"/>
    <div class="row">
      <VideoDetail :video="selectedVideo"/>
      <VideoList :videos="videos" @video-select="onVideoSelect"/>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
import SearchBar from '@/components/SearchBar.vue'
import VideoList from '@/components/VideoList.vue'
import VideoDetail from '@/components/VideoDetail.vue'
// 아래 키 값은 크롬의 유튜브 API_KEY받아온것
// API_KEY와 같은 값은 가려주는게 맞으므로 .env.local에 숨기고 변수로 불러와줬다.!
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  data() {
    return {
      videos: [],
      selectedVideo: null
    }
  },
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  methods: {
    onVideoSelect(video){
      // console.log(video)
      this.selectedVideo = video
    },
    onInputChange(inputValue) {
      // console.log(inputValue)
      axios.get(API_URL, {
        params: {
          key: API_KEY,
          part: 'snippet',
          type: 'video',
          q: inputValue
        }
      })
      .then(response => {
        console.log(response.data.items)
        this.videos = response.data.items
      })
      .catch(error => { console.log(error) })
      this.selectedVideo = null
    }
  }
}

</script>

<style>

</style>

```

## main.js

```javascript
import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')

```

## .env.local

```
VUE_APP_YOUTUBE_API_KEY=AIzaSyC1tQrciIigfPf2s0Acn9xsYsNgagaWT5g

```

