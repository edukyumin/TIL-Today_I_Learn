# 0421_homework

- 지문의 코드에서 ‘__gt’ 부분을 lookup이라고 한다. 링크를 참고하여 Django에서 사용 가능 한 lookup 세가지와 그 의미를 작성하시오

```
filter() - parameter로 들어오는 인자와 match되는 QuerySet을 반환한다
exclude() - parameter로 들어오는 인자와 match되지 않는 QuerySet을 반환한다
get() - parameter로 들어오는 인자와 match되는 object 한개를 반환한다
```



- 지문은 1:N 관계 설정을 하기 위하여 정의된 모델이다. 링크를 참고하여 빈 칸에 들어갈 수 있는 값 세가지와 그 의미를 작성하시오. 

```
CASCADE - ForeignKeyField가 바라보는 값이 삭제될 때 ForeignKeyField를 포함하는 모델 인스턴스(row)도 삭제된다.
PROTECT - ForeignKeyField가 바라보는 값이 삭제될 때 삭제가 되지않도록 ProtectedError를 발생시킨다.
DO_NOTHING - ForeignKeyField가 바라보는 값이 삭제될 때 아무런 행동을 취하지 않는다. 참조무결성을 해칠 위험이 있다
```



지문은 댓글 기능을 작성하기 위한 코드이다. 빈 칸에 들어갈 코드를 작성하시오.

```
commit=FALSE
```



 게시물 아래에 댓글을 출력하려고 한다. post와 comment 모델이 1:N으로 관계설정이 되어 있다고 가정 할 때 아래의 빈칸에 적절한 코드를 작성하시오..

```
article.comment_set.all
```

