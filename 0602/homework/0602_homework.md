# 0602_homework

1. SPA(Single Page Application)과 SFC(Single File Component)의 개념에 대해서 간략하게 작성하시오.

```
SPA(Single Page Application): 최초에 필요한 데이터를 모두 받고 변경요청이 있으면 필요한 데이터만 요청해서 페이지를 변경함

SFC(Single File Componenet): html, css, js코드를 하나의 파일(인스턴스가 아님)에 담아서 컴포넌트로 관리함. (대표적으로 .vue파일이 있음)
```



2. 아래 제시된 파일(혹은 폴더)의 역할을 간단하게 작성하시오. 

- src

  `실제 vue코드가 작성되는 파일들이 위치하는 디렉터`

  - router

    `라우터 설정과 관련된 파일을 모아두는 디렉토리`

    - index.js

    `라이터 인스턴스를 만들고 그안에 각각의 path와 component 설정을 하는 파일`

  - views

    `url로 접근할 때 보여지는 페이지에 대한 컴포넌트 파일을 모아두는 디렉토리`

    - Lunch.vue

  - App.vue

    `최상위 컴포넌트로 모든 자식 컴포넌트를 등록해서 관리 할 수 있다.`

  

3. 공식 문서를 참고하여 Vue.js에서 단방향 데이터 흐름을 사용하는 이유에 대해 간략하게 작성하시오. 

```
자식 요소가 의도치 않게 부모 요소의 상태를 변경함으로써 앱의 데이터 흐름을 이해하기 어렵게 만드는 일을 막기 위함
```



4. 아래의 설명을 읽고 T/F 여부를 작성하시오.. 

- 부모 컴포넌트의 데이터가 새로 갱신되는 경우에 자식 요소의 모든 prop들은 최신 값으로 새로고침된다. `T`
-  `prop으로 전달할 수 있는 데이터는 object만 가능하며` 숫자형, 논리 자료형 등은 전달할 수 없다. `F`
-  Django와 다르게 Vue.js는 URL을 통해 동적으로 데이터를 전달하는 Variable Routing을 할 수 없다. `F`
-  Vue.js 는 Single Page Application이기 때문에 브라우저의 뒤로가기 기능을 지원하지 않는다. `F`
-  Vue Router를 사용하면 실제 서버로 요청을 보내지 않고 경로와 연결된 컴포넌트를 보여준다.`T`