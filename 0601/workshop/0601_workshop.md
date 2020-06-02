# 0601_workshop

## App.vue

```vue
<template>
  <div>
    <SearchBar @input-change="onInputChange"/>
    <VideoList :videos="videos"/>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from '@/components/SearchBar.vue'
import VideoList from '@/components/VideoList.vue'
// 아래 키 값은 크롬의 유튜브 API_KEY받아온것
// API_KEY와 같은 값은 가려주는게 맞으므로 .env.local에 숨기고 변수로 불러와줬다.!
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'
export default {
  name: 'App',
  data() {
    return {
      videos: []
    }
  },
  components: {
    SearchBar,
    VideoList
  },
  methods: {
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
        // console.log(response.data.items)
        this.videos = response.data.items
      })
      .catch(error => { console.log(error) })
    }
  }
}

</script>

<style>

</style>

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

<style>

</style>
```



## VideoList.vue

```vue
<template>
  <div>
    VideoList
    {{ videos.length }}
    {{ videos }}
  </div>
</template>

<script>
export default {
  name: "VideoList",
  props: {
    videos: {
      type: Array,
    },
  },
};
</script>

<style></style>
```



## .env.local

```
VUE_APP_YOUTUBE_API_KEY=AIzaSyC1tQrciIigfPf2s0Acn9xsYsNgagaWT5g

```

