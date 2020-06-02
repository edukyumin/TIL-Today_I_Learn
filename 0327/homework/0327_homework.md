# 0327_homework

1. Django는 MTV 디자인 패턴으로 이루어진 Web Framework이다. 여기서 MTV는 무 엇의 약자이며 각각 MVC 디자인 패턴과 어떻게 매칭이 되는지 작성하시오.
   - `Model, Templates, View`
   - 각각 MVC의 `Model View Controller` 와 매칭된다.
2. ____(a)____는 Django에서 URL 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것 을 의미한다. (a)는 무엇인지 작성하시오.
   - `variable routing`



3. Django 프로젝트는 render할 template 파일들을 찾을 때, 기본적으로 settings.py에 등록된 각 앱 폴더 안의 (a) 폴더 내부를 탐색한다. (a)에 들어갈 폴더 이름을 작성하 시오

   - `templates`



4. Static web page와 Dynamic web page의 특징을 간단하게 서술하시오.
   
   - Static
     - 사용자의 요청에 따라 서버 안에 이미 저장되어 있는 문서(html emd) 자 wk 자체를 사용자에게 제공한다.
     - 문서의 내용이 바뀌지 않고, 모든 사용자는 같은 문서를 제공받아 같은 페이지를 보게 된다.
   - Dynamic
     - 사용자의 요청이 들어오면 서버(django 등)에서 상황에 맞는 문서를 생성해서 제공
     - 사용자마다 다른 문서를 제공해줄 수 있고, 요청에 맞는 데이터를 데이터베이스에서 찾거나 생성하여 보여줄 수 도 있다.
   
   