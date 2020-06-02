# 0330_homework

아래 링크를 참고하여 각 문제들을 해결하기 위한 코드를 작성하시오. https://docs.djangoproject.com/en/2.1/ref/templates/builtins/ 

1. menus 리스트를 반복문으로 출력하시오.

```html
{% for menu in menus %}
	<p>{{ menu }}</p>
{% endfor %}
```



2. posts 리스트를 반목문을 활용하여 0번 글부터 출력하시오.

```html
{% for post in posts %}
	<p>{{ forloop.counter }}번글: {{  post  }}</p>
{% endfor %}
```



3. users 리스트가 비어있다면 현재 가입한 유저가 없습니다. 텍스트를 출력하시오.

```python
{% for user in users %}
	<p>{{ user }}</p>
{% empty %}
	<p>현재 가입한 유저가 없습니다</p>
{% endfor %}
```



4. 첫 번째 반복문일 때와 아닐 때를 조건문으로 분기처리 하시오.

```python
{% if forloop.first %}
	<p>첫번쨰 반복문 입니다.</p>
{% else %}
	<p>첫번쨰 반복문이 아닙니다.</p>
{% endif %}
```



5. 출력된 결과가 주석과 같아지도록 하시오.

```python
<!--5-->
<p>{{'hello'|length }}
<!--My name is Tom-->
<p>{{'my name is tom'|title }}
```

6. 변수 today에 datetime 객체가 들어있을 때 출력된 결과가 주석과 같아지도록 하시오.

```python
<!-- 2020년 02월 02일 (sun) pm 02:02 -->
{{ today|date:"Y m d D aA h i"}}
```



다음은 form tag에 관한 문제이다. 올바른 답을 작성하시오.

1. 지문의 코드 중 form 태그의 속성인 action의 역할에 대해 설명하시오.

`폼 데이터(for data)를 서버로 보낼때 해당 데이터가 도착할 url을 명시합니다.`

2. 지문의 코드 중 method가 가질 수 있는 속성 값을 작성하시오.

`폼데이터가 서버로 제출될 떄 사용되는 http 메소드를 명시합니다.`

`GET`

`POST`

`HOST`

`DELETE`

3. input 태그에 각각 `안녕하세요`, `반갑습니다`, `파이팅` 문자열을 넣고 submit 버튼을 눌렀을 때 이동하는 url 경로를 작성하시오.

`.com/pages/create`

