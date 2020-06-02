# 0601_exercise

## App.vue

```vue
<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">TodoView</router-link>
    </div>
    <router-view />
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
```



## TodoView.vue

```vue
<template>
  <div>
      <!-- Input emit 1. 하위 컴포넌트의 create-todo 이벤트 감지 -->
      <TodoInput @create-todo="createTodo"/>
      <!-- prop 2. 하위 컴포넌트로 전달 데이터 바인딩 (오른쪽 todos가 하위 컴포넌트가 받는이름) -->
      <!-- emit 2. 하위 컴포넌트의 checked 이벤트 감지 -->
      <todoList :todos="todos" @checked="updateTodo"/>
  </div>
</template>

<script>
import TodoInput from '@/components/TodoInput.vue'
import TodoList from '@/components/TodoList.vue'

export default {
    name: 'TodoView',
    components: {
        TodoInput,
        TodoList
    },
    data() {
        return {
            todos: [
                {
                id: 1,
                content: 'Vue',
                isCompleted: true,
                },
                {
                id: 2,
                content: 'Django',
                isCompleted: false,
                },
                {
                id: 1,
                content: 'Python',
                isCompleted: false,
                }
            ]
        }
        
    },
    methods: {
        updateTodo(todo) {
            todo.isCompleted = !todo.isCompleted
        },
        createTodo(todo) {
            this.todos.push(todo)
        }
    }
}
</script>

<style>

</style>
```



## TodoInput.vue

```vue
<template>
  <div>
    <!-- 2. v-model 작성 -->
    <!-- 3. 입력 후 상위 컴포넌트로 보낼 이벤트를 작성시킬 메서드(createTodo)작성 -->
      <input type="text" v-model="todo" @keypress.enter="createTodo">
      <button @click="createTodo">작성</button>
  </div>
</template>

<script>
export default {
    name: 'TodoInput',
    // 1. data 작성
    data() {
      return {
        todo: ''
      }
    },
    // 4. emit 이벤트를 만드는 메서드
    methods: {
      createTodo() {
        if (this.todo.trim()) {
        this.$emit('create-todo', {
          id: Date.now(),
          content: this.todo,
          isCompleted: false
        })
        this.todo = ''
        }

      }
    }

}
</script>

<style>

</style>
```



## TodoList.vue

```vue
<template>
  <div>
      <h1>TodoList</h1>
      <ul>
          <li v-for="todo in todos" :key="todo.id" :class="{ completed: todo.isCompleted }">
            <!-- emit 1. 하위 컴포넌트에서 체크박스 클릭 시 checked 이벤트를 부모 컴포넌트에 알려줌 -->
            <input type="checkbox" @click="$emit('checked', todo)" :checked="todo.isCompleted">
            {{ todo.content }}
          </li>
      </ul>
  </div>
</template>

<script>
export default {
    name: 'TodoList',
    props: {
        todos: {
            type: Array,
            required: true
        } 
    }
}
</script>

<style>
    .completed {
        text-decoration: line-through;
    }
</style>
```

## index.js

```javascript
import Vue from 'vue'
import VueRouter from 'vue-router'
import TodoView from '@/views/TodoView.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'TodoView',
    component: TodoView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

```



