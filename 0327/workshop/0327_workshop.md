# 0327_workshop

1. intro/url.py

```cmd
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('dinner/<str:menu>/<int:people>/',views.dinner),
    path('admin/', admin.site.urls),
]

```

2.pages/views.py

```cmd
from django.shortcuts import render

# Create your views here.
def dinner(request, menu, people):
    context ={
        'menu' : menu,
        'people' : people,
    }
    return render(request, 'dinner.html', context)

```

3.templates/dinner.html

```cmd
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>저녁 메뉴 추천</title>
</head>
<body>
    <h1>저녁 메뉴 추천</h1>
    <h2>저녁 먹을 사람?? {{ people }}</h2>
    <h2>어떤 메뉴 ?! {{ menu }}</h2>

</body>
</html>
```

