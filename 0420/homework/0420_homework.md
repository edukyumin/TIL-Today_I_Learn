# 0420_homework

- 아래의 보기에서 각 문항의 설명에 맞는 용어를 고르시오.
  - `스키마` -관계형 데이터베이스에서 구조와 제약조건에 관련한 전반적인 명세를 기술 한 것 
  - `테이블` -열과 행의 모델을 사용해 조직된 데이터 요소들의 집합
  - `칼럼` - 고유한 데이터 형식이 지정되는 열
  - `레코드`-  단일 구조 데이터 항목을 가리키는 행 
  - `기본키` -각 행의 고유값



- 다음 SQL문법 중, DML이 아닌 것을 고르시오.
  - 1. `CREATE` 2. UPDATE 3. DELETE 4. SELECT



- RDBMS와 NOSQL을 비교하여 작성하시오.
  - RDBMS
    - 관계형 데이터베이스 관리 시스템
    - 관계를 통한 테이블간 연결을 통해 사용
    - 데이터 관리를 효율적
  - NOSQL
    - 테이블과 같은 개념으로 컬렉션이라는 형태로 데이터를 관리
    - RDBMS 보다 자유롭게 데이터를 추가가 가능
    - 컬렉션에 중복된 데이터가 저장이 가능

- 다음과 같은 스키마를 가지는 테이블이 있을 때 보기 중 틀린 문장을 고르시오.

1.  INSERT INTO classmates (name, age, address) VALUES(‘홍길동’, 20, ‘seoul’); 
2. . INSERT INTO classmates VALUES(‘홍길동’, 20, ‘seoul’); 
3. `insert into classmates values(address=‘seoul’, age=20, name=‘홍길동’);`
4. insert into classmates (address, age, name) values(‘seoul’, 20, ‘홍길동’);



- SQL에서 사용가능한 와일드카드 문자인 %와 _을 비교하여 작성하시오.

`%` 는 해당 문자만 있으면 나머지는 상관이 없다

`_` 는 글자수와 위치까지 맞아야한다.