# 0526_workshop

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>0526 workshop</title>
  <style>
    /* 취소선 */
    .completed {
      text-decoration: line-through;
      opacity: 0.6;
    }
  </style>
</head>
<body>
  <!-- 여기에 코드를 작성하시오 -->
  <div id="app">
    <select v-model="status">
      <option value="all">전체</option>
      <option value="active">진행중</option>
      <option value="completed">완료</option>
    </select>

    <!-- todo.completed가 true이면 해당 키 값이 활성화됨 -->
    <div v-for="todo in todosByStatus" :key="todo.id" v-bind:class="{ completed: todo.isCompleted }">
      <input type="checkbox" v-model="todo.isCompleted">
      <span>{{ todo.content }}</span>
    </div>
  

    <div>
      <input type="text" v-model="newTodo">
      <button @click="addTodo">todo</button>
    </div>
    <button @click="clearCompleted">완료된 할일 지우기</button>
  </div>
  <!-- <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script> -->
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    // 여기에 코드를 작성하시오
    const app = new Vue({
      el: '#app',
      data: {
        status: 'all',
        newTodo:'',
        todos:[
          {
            id: 1,
            content: 'Django 복습',
            isCompleted: true,
          },
          {
            id: 2,
            content: 'js 학습',
            isCompleted: false,
          },
          {
            id: 3,
            content: 'vuejs 복습',
            isCompleted: false,
          },
        ],
      },
      methods: {
        check: function (todo) {
          todo.isCompleted = !todo.isCompleted
        },
        addTodo: function () {
          this.todos.push({
             id: Date.now(),
            content: this.newTodo,
            isCompleted: false,
          })
          this.newTodo = ''
        },
        clearCompleted: function () {
          const notCompletedTodos = this.todos.filter( todo => {
            return !todo.isCompleted
          })
          this.todos = notCompletedTodos
        },
      },
      computed: {
        todosByStatus: function () {
          // 진행중인 일(완료되지 않은 일)
          if (this.status === 'active') {
            return this.todos.filter( todo => {
              return !todo.isCompleted
            })
          }
          // 완료된 일
          if (this.status === 'completed') {
            return this.todos.filter( todo => {
              return todo.isCompleted
            })
          }
          return this.todos
        },

      }
    })
  </script>
</body>
</html>
```

