OOO이름으로 프로젝트 생성

- django-admin startproject OOO

로켓 확인을 위한 세팅 설정

- HOST [`*`]

- 시간

로켓 확인

- python manage.py runserver 8080



# 같은 form을 공유하는 C와 U 만들기.

-R을 만들고, C와 U를 같은 porm.html에서 해결하자. D는 생략.(base.html 생략)



앱 만들기

- python manage.py startapp OOO
- settings.py의 INSTALLED_APPS에  OOO추가.



모델 설정

- OOO앱 내의 models.py에 모델 설정하기.

  ```python
  from django.db import models
  
  # Create your models here.
  class Article(models.Model):
      title = models.CharField(max_length=20)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```

- 설정한 모델 마이그레이션 해주기(설정 등록)

  - python manage.py makemigrations

- 마이그레이트 해주기(설정 업로드)
  - python manage.py migrate

- 관리자 계정 생성

  - python manage.py createsuperuser



관리자 계정 설정 및 게시글 생성 확인

- admin.py에 관리자 계성 설정하기

  ```python
  from django.contrib import admin
  from .models import Article
  
  # Register your models here.
  class Articleadmin(admin.ModelAdmin):
      list_display = ['title', 'content', 'created_at', 'updated_at']
  admin.site.register(Article, Articleadmin)
  ```

  Articleadmin의 경우 관리자 계정으로 Article이라는 모델을 통해 만들어진 게시글들을 표시할때 보여질 것을 설정하는 것. 없어도 무방.

- 설정 후, 관리자 로그인 및 게시글 생성 수정 삭제 확인.



### R을 만들기(detail 생략)

- 먼저 urls를 설정하기 위해 앱이 아닌, 프로젝트의 urls.py에 app이름으로 url요청이 왔을 때를 설정

  ```python
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('articles/', include('articles.urls')),
  ]
  ```

- app폴더 내에 urls.py 생성

  ```python
  from django.urls import path
  from . import views
  
  
  app_name = 'articles'
  urlpatterns = [
      path('', views.index, name='index')	#R생성을 위한 path
  ]
  ```

  app_name과 url name 설정 잊지말기(주소가 아닌, urlname활용을 위함.)

- views폴더 내에 index def하기.

  ```python
  from django.shortcuts import render
  from .models import Article
  # Create your views here.
  def index(request):
      articles = Article.objects.all()
      context = {
          'articles': articles
      }
      return render(request, 'articles/index.html', context)
  ```

- 앱 폴더에 templates/articles 라는 폴더 생성 후, index.html 생성

  ```html
  <!DOCTYPE html>
  <html lang="ko">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>R페이지</title>
  </head>
  <body>
      <a href="#">새 글 작성</a>
      {% for article in articles %}
          <h2>{{ article.title }}</h1>
          <h2>{{ article.content }}</h2>
          <h2>{{ article.created_at }}</h2>
          <a href="#">수정하기</a>
          <hr>
      {% endfor %}
  </body>
  </html>
  ```



### C만들기

- urls에 C 페이지 추가.

- views.create에서 사용할 form 만들어주기.

  - ### forms.py를 앱 폴더 내에 생성

    ```python
    from django import forms
    from .models import Article
    
    class ArticleForm(forms.ModelForm):
        class Meta:
            model = Article
            fields = '__all__'
    ```

- views에 create추가

  ```python
  from .forms import ArticleForm
  
  def create(request):
      if request.method == 'POST':
          path
  
      else:
          form = ArticleForm
      context = {
          'form': form,
      }
      return render(request, 'articles/form.html', context)
  ```

  해당 내용 추가.

- templates/articles에 form.html 생성.

  ```html
  <!DOCTYPE html>
  <html lang="ko">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
  </head>
  <body>
      <form action="", method="POST">
          {% csrf_token %}
          {{ form.as_p }}
          <button>작성</button>
      </form>
  </body>
  </html>
  ```

- views.create에 POST로 요청 왔을때 설정

  ```python
  from django.shortcuts import render, redirect	#redirect 추가.
  
  def create(request):
      if request.method == 'POST':
          form = ArticleForm(request.POST)
          if form.is_valid:
              article = form.save()
          	return redirect('articles:index')	#detail을 생략했기 대문에 index로 이동.
      else:
          form = ArticleForm
      context = {
          'form': form,
      }
      return render(request, 'articles/form.html', context)
  ```

- index의 새 글 작성 링크 활성화

  ```html
  <a href="{% url 'articles:create' %}">새 글 작성</a>
  ```



### U 만들기

- urls에 update추가.

  ```python
  path('<int:pk>/update/', views.update, name='update'),
  ```

- views.update추가.

  ```python
  from django.shortcuts import render, redirect, get_object_or_404	#숏컷에 get_ob..추가
  
  def update(request, pk):
      article = get_object_or_404(Article, pk=pk)
      if request.method == 'POST':
          pass
  
      else:
          form = ArticleForm(instance=article)
      context = {
          'form': form,
      }
      return render(request, 'articles/form.html', context)
  ```

- index.html의 수정하기 활성화

  ```html
  <a href="{% url 'articles:update' article.pk %}">수정하기</a>
  ```

- views.update의 post로 요청 왔을 때, 수정하기.

  ```python
  def update(request, pk):
      article = get_object_or_404(Article, pk=pk)
      if request.method == 'POST':
          form = ArticleForm(request.POST, instance=article)
          if form.is_valid():
              article = form.save()
          	return redirect('articles:index')
      else:
          form = ArticleForm(instance=article)
      context = {
          'form': form,
      }
      return render(request, 'articles/form.html', context)
  ```

  
  

****

# 회원가입

-유저 생성을 위한 폼 이용하기.

- urls.py에 signup추가

  ```python
  path('signup/', views.signup, name='signup'),
  ```

- views.signup추가

  ```python
  from django.contrib.auth.forms import UserCreationForm
  
  def signup(request):
      if request.method == 'POST':
          pass
      else:
          form = UserCreationForm()
      context = {
          'form': form,
      }
      return render(request, 'articles/signup.html', context)
  ```

- templates/articles/signup.html생성

  ```html
  <!DOCTYPE html>
  <html lang="ko">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>회원가입</title>
  </head>
  <body>
      <form action="" method="POST">
          {% csrf_token %}
          {{ form.as_p }}
          <button>가입</button>
      </form>
  </body>
  </html>
  ```

- views.signup에 POST로 요청왔을 때 수정.

  ```python
  def signup(request):
      if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
              form.save()
              return redirect('articles:index')
      else:
          form = UserCreationForm()
      context = {
          'form': form,
      }
      return render(request, 'articles/signup.html', context)
  ```

- index에 회원가입 버튼 만들기.

  ```html
  <a href="{% url 'articles:signup' %}">회원가입</a><br>
  ```

​	가입이 잘 되는지는 admin 페이지에서 하자. (get_user_model을 이용해서 유저 목록을 불러올 수 있지만, 지금은 생략)

****

# 로그인 구현

- urls에 login 추가

  ```python
  path('login/', views.login, name='login'),
  ```

  

- views.login 추가

  ```python
  from django.contrib.auth.forms import AuthenticationForm
  from django.contrib.auth import login as auth_login	#login이라는 이름으로 정의된 함수가 있기 때문에, auth_login으로 이름을 바꿔서 import.
  
  def login(request):
      if request.method == 'POST':
          pass
      else:
          form = AuthenticationForm()
      context = {
          'form': form,
      }
      return render(request, 'artielce/login.html', context)
  ```

- templates/articles/login.html작성

  ```html
  <!DOCTYPE html>
  <html lang="ko">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>로그인</title>
  </head>
  <body>
      <form action="" method='POST'>
          {% csrf_token %}
          {{ form.as_p }}
          <button>로그인</button>
      </form>
  </body>
  </html>
  ```

- login에 POST요청 왔을 때, 수정

  ```python
  def login(request):
      if request.method == 'POST':
          form = AuthenticationForm(request, request.POST)
          if form.is_valid():
              auth_login(request, form.get_user())
              return redirect('articles:index')
      else:
          form = AuthenticationForm()
      context = {
          'form': form,
      }
      return render(request, 'articles/login.html', context)
  ```

  두 가지 class의 사용법 잘 알아두자.

  `AuthenticationForm(request, request.POST)`

  `auth_login(request, form.get_user())`

****

# 로그아웃 구현

- urls.py에 logout추가

  ```python
  path('logout/', views.logout, name='logout'),
  ```

- views.logout 만들기

  ```python
  from django.contrib.auth import logout as auth_logout
  
  def logout(request):
      auth_logout(request)
      return redirect('articles:index')
  ```

****

# 로그인, 로그아웃 버튼 index에 구현

- views.py에 get_user_model import 및 user로 정의

  ```python
  from django.contrib.auth import get_user_model
  
  User = get_user_model()
  
  def index(request):
      articles = Article.objects.all()
      users = User.objects.all()	#이 부분 추가
      context = {
          'articles': articles,
          'users': users	#이 부분 추가
      }
      return render(request, 'articles/index.html', context)
  ```

- index.html에 로그인, 로그아웃 분기 해주기.

  ```html
  <body>
      <!-- 추가된 부분 -->
      {% if user.is_authenticated %}
          <h1>{{ user.username }}님 안녕하세요.</h1>
          <a href="{% url 'articles:logout' %}">로그아웃</a>
          <a href="{% url 'articles:create' %}">새 글 작성</a>
      {% else %}
          <a href="{% url 'articles:login' %}">로그인</a>
          <a href="{% url 'articles:signup' %}">회원가입</a><br>
      {% endif %}
  	<!-- 여기까지 -->
      {% for article in articles %}
          <h2>{{ article.title }}</h1>
          <h2>{{ article.content }}</h2>
          <h2>{{ article.created_at }}</h2>
          <a href="{% url 'articles:update' article.pk %}">수정하기</a>
          <hr>
      {% endfor %}
  </body>
  </html>
  ```

  # 끝!



