# 2020.03.31

## ORM 장점

- SQL을 몰라도 DB 연동이 가능하다. (SQL 문법을 몰라도 쿼리를 조작할 수 있다.)
- SQL의 절차적인 접근이 아닌 객체 지향적인 접근으로 인해 `생산성`이 대폭 증가한다.
- ERD를 보는 것에 대한 의존도를 낮출 수 있다.
- ORM은 해당 객체들을 재활용 할 수 있다. 때문에 모델에서 가공된 데이터를 view와 template과 합쳐지는 형태로 MTV디자인 패턴을 유지할 수 있다.

## ORM 단점

- ORM만으로는 완전한 혹은 거대한 서비스를 구현하기는 어렵다.
- 사용이 쉬운 방면 설계는 신중하게 해야 한다.
- 오히려 프로젝트의 복잡성이 커질 경우 SQL 보다 난이도가 상승할 수 있다.





### Model 의 정의

> 데이터에 대한 단일 정보 소스

- Model : MTV 패턴에서 데이터를 관리
- Migration : Model로 정의된 데이터베이스 스키마를 반영
- ORM : python 객체언어로 데이터베이스를 조작

### DB 정의

> 체계화된 통합, 관리하는 데이터의 집합



## 모델 작성 또는 변경 시 필수 3단계

### 1. models.py 작성

### 2. makemigrations

### 3. migrate

#### DB만드는 순서

```ba
$ python manage.py makemigrations
$ python manage.py sqlmigrate articles 0001
$ python manage.py showmigrations(( 상태 확인 하는 것임 ))
$ python manage.py migrate 
```

#### Shell 활용 하기위해

```bash
$ pip install ipython django-extensions
설치후
$ ipython 
```



## DB입력 (orm -> python 쓰듯이 작성)   //   만드는 법 3가지

```bash
# 첫번째 방법
In [1]: article = Article()                                                               
In [2]: article.title = 'first'                                                           
In [3]: article.content = 'django!'                                                                     

In [4]: article                                                                           
Out[4]: <Article: Article object (None)>

In [5]: article.save() 

In [6]: article                                                                
Out[6]: <Article: Article object (1)>

In [7]: Article.objects.all()
Out[7]: <QuerySet [<Article: Article object (1)>]>

# title -> titile 로 잘못 입력함..
In [8]: article.titile                                                                                  
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-8-c778138f8549> in <module>
----> 1 article.titile

AttributeError: 'Article' object has no attribute 'titile'

In [9]: article.title  
Out[9]: 'first'

In [10]: article.content    
Out[10]: 'django!'

# 두번째 방법
In [11]: article = Article(title='second', content='django!!')                                          
In [12]: article      
Out[12]: <Article: Article object (None)>

In [13]: article.save()   

In [14]: article      
Out[14]: <Article: Article object (2)>

In [15]: Article.objects.all()     
Out[15]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]>

In [16]: article.title   
Out[16]: 'second'

In [17]: article.content    
Out[17]: 'django!!'

# 세번째 방법
# 인스턴스를 생성하지 않고 만드는과 동시에 save() 함
In [18]: Article.objects.create(title='third', content='django!!!')       
Out[18]: <Article: Article object (3)>

# id == pk(primary key)  99%같은 의미
# 차이는 내부적인 동작
# id__exact / id / pk => 다 적용되지만  django 는 `pk`를 선호합니다!
In [19]: article.pk    
Out[19]: 2

In [20]: article.id     
Out[20]: 2

# 전체 조회
In [21]: Article.objects.all()   
Out[21]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>

# 선택 조회
In [22]: Article.objects.get(pk=2)
Out[22]: <Article: Article object (2)>

# pk=1 수정~
In [24]: article = Article.objects.get(pk=1)                                                            
In [26]: article     
Out[26]: <Article: Article object (1)>

In [27]: article.title = 'byebye'                                                                       
In [28]: article.title     
Out[28]: 'byebye'

In [29]: article.save()                                                                                 
In [30]: article.title  
Out[30]: 'byebye'

# pk=2 삭제하기~  => delete() 활용
In [31]: article = Article.objects.get(pk=2)                                                            
In [32]: article 
Out[32]: <Article: Article object (2)>

In [33]: article.delete()  
Out[33]: (1, {'articles.Article': 1})

#  2번 삭제됬는지 확인차 해봄..
In [34]: Article.objects.get(pk=2)                                                                      
---------------------------------------------------------------------------
DoesNotExist                              Traceback (most recent call last)
<ipython-input-34-834e448f9502> in <module>
----> 1 Article.objects.get(pk=2)

~/.local/lib/python3.7/site-packages/django/db/models/manager.py in manager_method(self, *args, **kwargs)
     80         def create_method(name, method):
     81             def manager_method(self, *args, **kwargs):
---> 82                 return getattr(self.get_queryset(), name)(*args, **kwargs)
     83             manager_method.__name__ = method.__name__
     84             manager_method.__doc__ = method.__doc__

~/.local/lib/python3.7/site-packages/django/db/models/query.py in get(self, *args, **kwargs)
    397             raise self.model.DoesNotExist(
    398                 "%s matching query does not exist." %
--> 399                 self.model._meta.object_name
    400             )
    401         raise self.model.MultipleObjectsReturned(

DoesNotExist: Article matching query does not exist.
```



## django 관리자 만들기

- 관리자 계정은 반드시 migrate 이후에 진행해야 한다.
- 관리자 계정도 DB 에 저장할 곳이 있어야 하기 때문에

```bash
$ python manage.py createsuperuser
사용자 이름 (leave blank to use 'ubuntu'): admin
이메일 주소: 
Password: 
Password (again): 
# password가 너무 간단하면 뜨는 거임
비밀번호가 너무 일상적인 단어입니다.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

#### admin.py

```python
from django.contrib import admin
from .models import Article
# Register your models here.

admin.site.register(Article) # 등록
```

## Article.objects.all()

## Article(title=title, content=content)

## Article.objects.get(pk=1)