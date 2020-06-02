# 0525_exercise

## 00_vue_tutorial

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div id="app">
        {{ message }}
    </div>
    <hr>
    <div id="app-2">
        <span v-bind:title="message">
            내 위에 잠시 마우스를 올리면 동적으로 바인딩 된 title을 볼 수 있습니다!
        </span>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        const app = new Vue({
            el: '#app',
            // data : vue 인스턴스의 데이터 속성을 나타냄
            // 다양한 정보들이 담길 수 있으며, 인스턴스가 들고있어야 하는 각종 데이터나 인스턴스의 상태정보를 담는다.
            data: {
                message: 'Hello, Vue!'
            }
        })

    
        const app2 = new Vue({
            el: '#app-2',
            data: {
                message : '이 페이지는 ' + new Date() + ' 에 로드 되었습니다.'
            }
        })
    </script>

    
</body>
</html>
```



## 01_vue_directive

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div id="app-3">
        <p v-if="seen">이제 나를 볼 수 있어요.</p>
    </div>
    <hr>
    <div id="app-4">
        <ol>
            <li v-for="todo in todos">{{ todo.text }}</li>
        </ol>
    </div>
    <div id="app-5">
        <p>{{ message }}</p>
        <button v-on:click="reverseMessage">뒤집어!!</button>
    </div>
    <div id="app-6">
        <p>{{ message }}</p>
        <input type="text" v-model="message">
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        const app3 = new Vue({
            el: '#app-3',
            data: {
                seen: true
            }
        })

        const app4 = new Vue({
            el: '#app-4',
            data: {
                todos: [
                    { text: 'JS 배우기'},
                    { text: 'vue 배우기'},
                    { text: '파이썬 배우기'}
                ]
            }
        })

        const app5 = new Vue({
            el: '#app-5',
            data: {
                message: '안녕 vue !!'
            },
            methods: {
                reverseMessage: function() {
                    this.message = this.message.split('').reverse().join('')
                }
            }
        })

        const app6 = new Vue({
            el: '#app-6',
            data: {
                message: '반갑습니다 vue !!'
            }
        })
    </script>
</body>
</html>
```

