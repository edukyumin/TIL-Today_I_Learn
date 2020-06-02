# 0326_workshop

1. intro/urls.py

```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('lotto/', views.lotto),
    path('admin/', admin.site.urls),
]

```

2. pages/views.py

```python
import random
from django.shortcuts import render

# Create your views here.
def lotto(request):
    numbers= range(1, 46)
    lotto = random.sample(numbers, 6)
    context ={
        #trailing comma
        'lotto' : lotto,
    }
    return render(request, 'lotto.html', context)
```



3. templates/lotto.html

```cmd
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>제 000회 로또 번호 추천</h1>
    <!--Django Template Language-->
    <p>{{ lotto }}</p>

</body>
</html>
```

