# 0525_workshop

## get_cat_image_vue.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>CAT IMAGE</h1>
    <div id = "cat">
        <img v-bind:src="catImageUrl" width="300" height="300">
        <button v-on:click="getCatImg">고양이 사진 교체</button>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    
    <script>
        const app = new Vue ({
            el: '#cat',
            data: {
                catImageUrl: ''
            },
            methods: {
                getCatImg: function () {
                    axios.get('https://api.thecatapi.com/v1/images/search')
                        .then(response => {
                            // console.log(response.data[0].url)
                            this.catImageUrl = response.data[0].url
                        })
                }
            }
        })
    </script>
</body>
</html>
```

