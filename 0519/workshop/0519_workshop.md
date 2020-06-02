# 0519_workshop

## index.html

```html
{% extends 'base.html' %} {% block content %}
<h2>INDEX</h2>
{% for article in articles %}
<h3>작성자: {{ article.user }}</h3>
<h4>제목: {{ article.title }}</h4>
<p>내용: {{ article.content }}</p>
{% if user in article.like_users.all %}
<i class="fas fa-heart fa-lg like-button" style="color: crimson;" data-id="{{ article.pk }}"></i>
{% else %}
<i class="fas fa-heart fa-lg like-button" style="color: black;" data-id="{{ article.pk }}"></i>
{% endif %}
</a>
<span id="like-count-{{ article.pk }}">{{ article.like_users.all|length }}</span>명이 이 글을 좋아합니다.
<hr />
{% endfor %}
<a href="{% url 'articles:create' %}">CREATE</a>

<script>
  // 1. 좋아요 하트버튼 모두 가져오기
  const likeButtonList = document.querySelectorAll('.like-button')
  // 2. 각각의 좋아요 하트에 이벤트리스너 추가
  likeButtonList.forEach(likeButton => {
    likeButton.addEventListener('click', function (event) {
      // console.log(event)
      // axios를 통해서 좋아요 view 함수에 요청을 보내야 하는데...
      // 각 글의 좋아요 요청이 구분되어야 한다.(각 article id가 필요하다)
      // 3. 좋아요 하트를 구분하기 위해 articleId 가져오기
      const articleId = event.target.dataset.id
      // 4. 좋아요함수에 요청 보내기
      {% if request.user.is_authenticated %}
      axios.get(`/articles/${articleId}/like/`)
        .then(response => {
          console.log(response)
          // 4-1. 좋아요 개수 바꾸기
          document.querySelector(`#like-count-${articleId}`).innerText = response.data.count
          // 4-2. 하트색깔 바꾸기
          // 그런데 좋아요 상태를 파악할 값이 없다.
          // 상태가 2가지 인 경우 boolean 값을 사용하면 좋다.
          if (response.data.liked) {
            event.target.style.color = 'crimson'
          } else {
            event.target.style.color = 'black'
          }
        })
        .catch(error => {
          console.log(error)
        })
        {% else %}
        alert('비로그인 사용자는 누를 수 없습니다.')
        {% endif %}
    })
  })

</script>
{% endblock %}
```

## base.html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>workshop</title>
  <!-- font-awesome -->
  <script src="https://kit.fontawesome.com/5fb041fb6b.js" crossorigin="anonymous"></script>
  <!-- axios -->
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>

</head>
<body>
  {% if request.user.is_authenticated %}
    <li>
      {{ request.user.username }}님 로그인
    </li>
    <li>
      <a href="{% url 'accounts:logout' %}">로그아웃</a>
    </li>
  {% else %}
    <li>
      <a href="{% url 'accounts:login' %}">로그인</a>
    </li>
    <li>
      <a href="{% url 'accounts:signup' %}">회원가입</a>
    </li>
  {% endif %}

  {% block content %}
  {% endblock %}
</body>
</html>

```

views.py

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Article
from .forms import ArticleForm


def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/form.html', context)


def like(request, article_pk):
    user = request.user 
    article = get_object_or_404(Article, pk=article_pk)
    
    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
        liked = False
    else:
        article.like_users.add(user)
        liked = True

    context = {
        'count' : article.like_users.count(),
        'liked' : liked,
    }
    return JsonResponse(context)

```





