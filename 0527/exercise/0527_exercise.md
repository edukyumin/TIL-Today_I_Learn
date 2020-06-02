# 0527_exercise

App.vue

```vue
<template>
  <div id="app">
    <div>
      <button @click="statusIndex">Index</button>
      <button @click="statusLunch">Lunch</button>
      <button @click="statusLotto">Lotto</button>
    </div>
    <!-- 3. 사용하기 -->
    <Index v-if="status === 'index'"/>
    <hr>
    <Lunch v-if="status === 'lunch'"/>
    <hr>
    <Lotto v-if="status === 'lotto'"/>
  </div>
</template>

<script>
// 1. 불러오기
import Index from './components/Index.vue'
import Lunch from './components/Lunch.vue'
import Lotto from './components/Lotto.vue'

export default {
  name: 'App',
  // 2. 등록하기
  components: {
    Index,
    Lunch,
    Lotto,
  },
  data: function () {
    return {
      status: 'index'
    }
  },
  methods:{
    statusIndex: function () {
      this.status = 'index'
    },
    statusLunch: function () {
      this.status = 'lunch'
    },
    statusLotto: function () {
      this.status = 'lotto'
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
```

## Index.vue

```vue
<!--html코드를 작성하는 부분. 기존의 <div id="app"></div>라고 생각-->
<template>
  <div>
      <p>사용 가능한 기능</p>
      <p>메뉴 추천, 로또번호 생성</p>
  </div>
</template>

<!-- js 코드를 작성하는 부분. 기존의 const app = new Vue({})의 내부라고 생각.-->
<script>
export default {

}
</script>

<!-- css 코드를 작성하는 부분. -->
<style>

</style>
```

## Lotto.vue

```vue
<template>
  <div>
      <h1>로또번호선택</h1>
      <p>{{ numbers }}</p>
      <button @click="createNumber">추첨</button>
      <p>{{ lucky }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
    name: 'Lotto',
    data: function () {
        return {
            numbers: _.range(1, 46),
            lucky: ''
        }
    },
    methods: {
        createNumber: function () {
            this.lucky = _.sampleSize(this.numbers, 6)
        }
    },
}
</script>

<style>

</style>
```

## Lunch.vue

```vue
<template>
  <div>
      <h1>Lunch</h1>
      <p>{{ menus }}</p>
      <button @click="pick">랜덤선택</button>
      <p>{{ choice }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
    name: 'Lunch',
    data: function () {
        return {
            menus: ['짬뽕', '짜장', '김밥', '라면'],
            choice: ''
        }
    },
    methods: {
        pick: function () {
            this.choice = _.sample(this.menus)
        }
    }
}
</script>

<style>

</style>
```

