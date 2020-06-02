1. #### 프로젝트 만들기

   ```bash
   django-admin startproject 프로젝트이름
   ```

   settings.py 에서 HOST설정('*')
   LANGUAGE_CODE, TIME_ZONE 는 옵션


   -> 로켓 확인

   ```bash
   python manage.py runserver 8080
   ```

   

2. #### 앱 만들기

   ```bash
   python manage.py startapp 앱이름
   ```

   settings.py의 INSTALLED_APPS에 만든 앱 추가.
   

3. #### 모델 만들기(migration)->데이터 베이스를 만들기 위한.

   앱의 models.py에 클래스 만들기

   ```python
   class Article(models.Model):
       title = models.CharField(max_length=20)
       content = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
   ```

   터미널에 클래스 migration, migrate

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

   관리자 생성 후, 데이터베이스 생성 확인(글 쓰기, 수정, 삭제)

   - `관리자는 migrate까지 한 후에 만들어야 한다!`

   관리자 생성

   ```bash
   python manage.py createsuperuser
   ```

   관리자 생성 후, 앱의 admin에 게시판을 추가해줘야 한다.

   ```python
   from django.contrib import admin
   from .models import Article
   # Register your models here.
   
   admin.site.register(Article)
   ```

   게시판 확인.

4. #### base.html

   프로젝트 폴더에 base.html용 templates폴더 만들기
   앱 폴더에 templates폴더 만들기. templates 폴더 안에 앱 명으로 폴더 하나 더 만들기

   프로젝트 폴더의 templates 폴더 안에 base.html 파일 만들기

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
       <title>Document</title>
   </head>
   <body>
       {% block content %}
       {% endblock %}
       <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
       <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
       <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
   </body>
   </html>
   ```

   프로젝트 폴더의 settings.py에 TEMPLATES 설정하기

   ```python
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [os.path.join(BASE_DIR, 'templates')],
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
           },
       },
   ]
   ```

   프로젝트 폴더의 urls.py에 앱 이름으로 url 설정하기.

   ```python
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('articles/', include('articles.urls')),
   ]
   ```

   

   앱 폴더 안에 urls.py를 만들어주기.

   ```python
   from django.urls import path
   
   urlpatterns = [
   
   ]
   ```



5. #### CRUD 만들기.(Urls, Views, Templates(html))

   ****

   ##### -R먼저 만들어주면서 현재까지 만들어진 내용 확인하기.

   index를 만들자.
   /articles/로 들어왔을 때를 위해 urls.py에 내용 넣기

   ```python
   from django.urls import path
   from . import views
   
   urlpatterns = [
       path('', views.index),
   ]
   ```

   views 설정하기.

   ```python
   from django.shortcuts import render
   from .models import Article
   
   
   # Create your views here.
   def index(request):
       articles = Article.objects.all()
       context = {
           'articles': articles,
       }
       return render(request, 'articles/index.html', context)
   
   ```

   index.html 만들기(Read먼저 구현)

   ```html
   {% extends 'base.html' %}
   
   {% block body %}
       <h1>INDEX</h1>
       <a href="">NEW</a>
       {% for article in articles %}
           <h2>제목: {{ article.title }}</h2>
           <h3>내용: {{ article.content }}</h3>
           <a href="">DETAIL</a>
           <hr>
       {% endfor %}
   {% endblock %}
   ```

   ##### Read 완성

   ****

   ##### create 구현

   1. new만들기
      urls.py에 new 추가

      ```python
      path('new/', views.new),
      ```

      views.py에 new 추가

      ```python
      def new(request):
          return render(request, 'articles/new.html')
      ```

      templates의 articles 폴더 안에 new.html만들기

      ```html
      {% extends 'base.html' %}
      
      {% block content %}
          <h1>NEW</h1>
          <form action="/articles/create/">
              <label for="title">TITLE:</label>
              <input type="text" id="title" name="title"><br>
              <label for="content">CONTENT</label>
              <textarea name="content" id="content" cols="30" rows="10"></textarea><br>
              <input type="submit" value="작성">
          </form>
      {% endblock %}
      ```

   2. create 만들기

      작성 클릭시 이동할 create 만들어주기!
      urls.py에 create 추가

      ```python
      path('create/', views.create),
      ```

      views.py에 create 추가

      ```python
      def create(request):
          article = Article()
          article.title = request.GET.get('title')
          article.content = request.GET.get('content')
          article.save()
          return render(request, 'articles/index.html')
      #아직 detail을 안만들어서 임시로 index로 보냄.(글 작성은 가능)
      ```

      `templates는 원래 detail로 연결시켜줘야 하는데 아직 구현을 안해서 임시로 index로 연결.`

      ##### Create 완성.

   ****

   ##### detail 만들기(여기서부터 variable routing 스펠링 맞나? 베리어블라우팅 필요.)(url에 pk값 같이 줄때 쓰는거.)

   urls.py에 detail 추가

   ```python
   path('detail/<int:pk>/', views.detail),
   ```

   views.py에 detail 추가

   ```python
   def detail(request, pk):
       article = Article.objects.get(pk=pk)
       context ={
           'article':artielc,
       }
       return render(request, 'articles/detail.html', context)
   ```

   templates폴더의 articles에 detail.html 추가

   ```html
   {% extends 'base.html' %}
   {% block content %}
       <h1>DETAIL</h1>
       <h2>{{ article.title }}</h2>
       <h3>{{ article.content }}</h3>
       <h3>작성일:{{ article.created_at }}</h3>
       <h3>수정일:{{ article.updated_at }}</h3>
       <a href="/articles/edit/{{ article.pk }}">EDIT</a>  <a href="">DELETE</a>
   {% endblock %}
   ```

   맨 밑의 a태그 두 개는 수정과 삭제 버튼, 현재 수정 버튼만 주소를 넣어놓음.

   ->index.html 의 detail 버튼 주소에 `href="/articles/detail/{{ article.pk }}"`추가

   ##### detail 완료.

   ****

##### update 만들기

1. edit 만들기

   urls.py에 edit 추가

   ```python
   path('edit/<int:pk>/', views.edit),
   ```

   view에 edit 추가

   ```python
   def edit(request, pk):
       article = Article.objects.get(pk=pk)
       context = {
           'article':article
       }
       return render(request, 'articles/edit.html', context)
   ```

   templates폴더의 articles폴더에 edit추가

   ```html
   {% extends 'base.html' %}
   {% block content %}
       <h1>EDIT</h1>
       <form action="/articles/update/{{ article.pk }}/"></form>
           <label for="title">TITLE:</label>
           <input type="text" id="title" name="title" value="{{ article.title }}"><br>
           <label for="content">{{ article.content }}</label>
           <textarea name="content" id="content" cols="30" rows="10"></textarea><br>
           <input type="submit" value="수정">
   
   {% endblock %}
   ```

2. update 만들기

   urls.py에 update 추가

   ```python
   path('update/<int:pk>/', views.update),
   ```

   views.py에 update 추가

   ```python
   def update(request, pk):
       article = Article.objects.get(pk=pk)
       article.title = request.GET.get('title')
       article.content = request.GET.get('content')
       article.save()
       context ={
           'article':article,
       }
       return render(request, 'articles/detail.html', context)
   ```

   detail.html의 a태그 중 edit에 `href="/articles/edit/{{ article.pk }}"`추가

   수정 저장 후, detail.html 불러오기.

##### update완료

****

##### delete만들기

urls.py에 delete 추가

```python
path('delete/<int:pk>/', views.delete'),
```

views.py에 delete 추가

```python
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('/articles/')
```

redirect를 사용하기 위해 맨 위 import 줄에

```python
from django.shortcuts import render, redirect
```

추가

detail.html의 a태그 중 edit에 `href="/articles/delete/{{ article.pk }}"`추가

##### delete완료

->초반에 views.py의 create에 임시로 index로 연결한 것을 detail로 옮기자.

```python
return redirect('articles:index')
```

## 여기까지 CRUD 구현완료. 명세서 내의 BACK버튼 등 기타 구현하기.

new.html에 BACK 추가

```html
{% extends 'base.html' %}

{% block content %}
    <h1>NEW</h1>
    <form action="/articles/create/">
        <label for="title">TITLE:</label>
        <input type="text" id="title" name="title"><br>
        <label for="content">CONTENT</label>
        <textarea name="content" id="content" cols="30" rows="10"></textarea><br>
        <input type="submit" value="작성">
    </form>
    <a href="/articles/">BACK</a>
{% endblock %}
```

맨 밑에서 2번째 줄에 추가함.

detail.html에 BACK 추가

```html
{% extends 'base.html' %}
{% block content %}
    <h1>DETAIL</h1>
    <h2>{{ article.title }}</h2>
    <h3>{{ article.content }}</h3>
    <h3>작성일:{{ article.created_at }}</h3>
    <h3>수정일:{{ article.updated_at }}</h3>
    <a href="/articles/edit/{{ article.pk }}">EDIT</a>  <a href="/articles/delete/{{ article.pk }}">DELETE</a><br>
    <a href="/articles/">BACK</a>
{% endblock %}
```

edit.html에 BACK 추가

```html
{% extends 'base.html' %}
{% block content %}
    <h1>EDIT</h1>
    <form action="/articles/update/{{ article.pk }}/">
        <label for="title">TITLE:</label>
        <input type="text" id="title" name="title" value="{{ article.title }}"><br>
        <label for="content">CONTENT:</label>
        <textarea name="content" id="content" cols="30" rows="10">{{ article.content }}</textarea><br>
        <input type="submit" value="수정">
    </form>
    <a href="/articles/detail/{{ article.pk }}">BACK</a>
{% endblock %}
```





# name기능 붙여 수정하기.

1. urls.py에 appname과 url name 만들기.

   ```python
   from django.urls import path
   from . import views
   app_name = 'articles'
   urlpatterns = [
       path('', views.index, name='index'),
       path('new/', views.new, name='new'),
       path('create/', views.create, name='create'),
       path('edit/<int:pk>/', views.edit, name='edit'),
       path('detail/<int:pk>/', views.detail, name='detail'),
       path('update/<int:pk>/', views.update, name='update'),
       path('delete/<int:pk>/', views.delete, name='delete'),
   ]
   ```

2. 각 HTML 수정.
   index.html
   수정 전

   ```html
   {% extends 'base.html' %}
   
   {% block content %}
       <h1>INDEX</h1>
       <a href="new/">NEW</a>
       {% for article in articles %}
           <h2>제목: {{ article.title }}</h2>
           <h3>내용: {{ article.content }}</h3>
           <a href="/articles/detail/{{ article.pk }}">DETAIL</a>
           <hr>
       {% endfor %}
   {% endblock %}
   ```

   수정 후

   ```html
   {% extends 'base.html' %}
   
   {% block content %}
       <h1>INDEX</h1>
       <a href="new/">NEW</a>
       {% for article in articles %}
           <h2>제목: {{ article.title }}</h2>
           <h3>내용: {{ article.content }}</h3>
           <a href="{% url 'articles:detail' article.pk %}">DETAIL</a>
           <hr>
       {% endfor %}
   {% endblock %}
   ```


   new.html
   수정 전

   ```html
   {% extends 'base.html' %}
   
   {% block content %}
       <h1>NEW</h1>
       <form action="/articles/create/">
           <label for="title">TITLE:</label>
           <input type="text" id="title" name="title"><br>
           <label for="content">CONTENT</label>
           <textarea name="content" id="content" cols="30" rows="10"></textarea><br>
           <input type="submit" value="작성">
       </form>
       <a href="/articles/">BACK</a>
   {% endblock %}
   ```

   수정 후

   ```html
   {% extends 'base.html' %}
   
   {% block content %}
       <h1>NEW</h1>
       <form action="{% url 'articles:create' %}">
           <label for="title">TITLE:</label>
           <input type="text" id="title" name="title"><br>
           <label for="content">CONTENT</label>
           <textarea name="content" id="content" cols="30" rows="10"></textarea><br>
           <input type="submit" value="작성">
       </form>
       <a href="{% url 'articles:index' %}">BACK</a>
   {% endblock %}
   ```

   

   detail.html
   수정 전

   ```html
   {% extends 'base.html' %}
   {% block content %}
       <h1>DETAIL</h1>
       <h2>{{ article.title }}</h2>
       <h3>{{ article.content }}</h3>
       <h3>작성일:{{ article.created_at }}</h3>
       <h3>수정일:{{ article.updated_at }}</h3>
       <a href="{/articles/edit/{{ article.pk }}">EDIT</a>  <a href="/articles/delete/{{ article.pk }}">DELETE</a><br>
       <a href="/articles/">BACK</a>
   {% endblock %}
   ```

   수정 후

   ```html
   {% extends 'base.html' %}
   {% block content %}
       <h1>DETAIL</h1>
       <h2>{{ article.title }}</h2>
       <h3>{{ article.content }}</h3>
       <h3>작성일:{{ article.created_at }}</h3>
       <h3>수정일:{{ article.updated_at }}</h3>
       <a href="{% url 'articles:edit' article.pk %}">EDIT</a>  <a href="{% url 'articles:delete' article.pk %}">DELETE</a><br>
       <a href="/articles/">BACK</a>
   {% endblock %}
   ```


   수정 전

   ```html
   {% extends 'base.html' %}
   {% block content %}
       <h1>EDIT</h1>
       <form action="/articles/update/{{ article.pk }}/">
           <label for="title">TITLE:</label>
           <input type="text" id="title" name="title" value="{{ article.title }}"><br>
           <label for="content">CONTENT:</label>
           <textarea name="content" id="content" cols="30" rows="10">{{ article.content }}</textarea><br>
           <input type="submit" value="수정">
       </form>
       <a href="/articles/detail/{{ article.pk }}">BACK</a>
   {% endblock %}
   ```

   수정 후

   ```html
   {% extends 'base.html' %}
   {% block content %}
       <h1>EDIT</h1>
       <form action="{% url 'articles:update' article.pk %}/">
           <label for="title">TITLE:</label>
           <input type="text" id="title" name="title" value="{{ article.title }}"><br>
           <label for="content">CONTENT:</label>
           <textarea name="content" id="content" cols="30" rows="10">{{ article.content }}</textarea><br>
           <input type="submit" value="수정">
       </form>
       <a href="{% url 'articles:detail' article.pk %}">BACK</a>
   {% endblock %}
   ```

   views의 redirect도 수정하자!

   'app이름:url이름'

   형식으로.



## GET방식으로 POST 방식으로 변환.

form태그의 method의 default 값인 GET을 POST로 바꾼 후, request.GET -> request.POST 로 바꾼다.

이때 form 태그 밑에 {% csrf_token %}를 추가하는걸 잊지 말자.


edit.html수정전

```python
{% extends 'base.html' %}
{% block content %}
    <h1>EDIT</h1>
    <form action="{% url 'articles:update' article.pk %}/">
        <label for="title">TITLE:</label>
        <input type="text" id="title" name="title" value="{{ article.title }}"><br>
        <label for="content">CONTENT:</label>
        <textarea name="content" id="content" cols="30" rows="10">{{ article.content }}</textarea><br>
        <input type="submit" value="수정">
    </form>
    <a href="{% url 'articles:detail' article.pk %}">BACK</a>
{% endblock %}
```

수정 후

```python
{% extends 'base.html' %}
{% block content %}
    <h1>EDIT</h1>
    <form action="{% url 'articles:update' article.pk %}/" method="POST">
        {% csrf_token %}
        <label for="title">TITLE:</label>
        <input type="text" id="title" name="title" value="{{ article.title }}"><br>
        <label for="content">CONTENT:</label>
        <textarea name="content" id="content" cols="30" rows="10">{{ article.content }}</textarea><br>
        <input type="submit" value="수정">
    </form>
    <a href="{% url 'articles:detail' article.pk %}">BACK</a>
{% endblock %}
```

views.py의 update도 수정.

```python
article.title = request.POST.get('title')
article.content = request.POST.get('content')
```



new.html 수정 전

```python
{% extends 'base.html' %}

{% block content %}
    <h1>NEW</h1>
    <form action="{% url 'articles:create' %}">
        <label for="title">TITLE:</label>
        <input type="text" id="title" name="title"><br>
        <label for="content">CONTENT</label>
        <textarea name="content" id="content" cols="30" rows="10"></textarea><br>
        <input type="submit" value="작성">
    </form>
    <a href="{% url 'articles:index' %}">BACK</a>
{% endblock %}
```

수정 후

```python
{% extends 'base.html' %}

{% block content %}
    <h1>NEW</h1>
    <form action="{% url 'articles:create' %}" method="POST">
        {% csrf_token %}
        <label for="title">TITLE:</label>
        <input type="text" id="title" name="title"><br>
        <label for="content">CONTENT</label>
        <textarea name="content" id="content" cols="30" rows="10"></textarea><br>
        <input type="submit" value="작성">
    </form>
    <a href="{% url 'articles:index' %}">BACK</a>
{% endblock %}
```

views.py의 create도 수정

```python
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
```







## 오류 바꾸기.

views의 import에 get_object_or_404` 추가

```python
from django.shortcuts import render, redirect, get_object_or_404
```

detail의 article 지정을 다음과 같이 변경

```python
article = Article.objects.get(pk=pk)	#이 모습에서 에서

article = get_object_or_404(Article, pk=pk) #이렇게 수정
```


![image-20200407005606242](C:\Users\a\Desktop\image-20200407005606242.png)![image](https://user-images.githubusercontent.com/60081212/78578383-6b487a80-786a-11ea-80d7-a525d26dba9d.png)

아직 저장하지 않은 pk값의 detail을 요청했을 때, 위의 오류 모습에서 아래와 같은 모습으로 바뀌게 된다.


![image](https://user-images.githubusercontent.com/60081212/78578583-b1054300-786a-11ea-8353-66ce657ed3b3.png)

![image](https://user-images.githubusercontent.com/60081212/78578319-4f44d900-786a-11ea-88e2-87704e4cdf8c.png)



끝.