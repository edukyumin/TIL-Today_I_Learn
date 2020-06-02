0406_homework

1. 

   (a):  {% url 'resevations:update' reservation.id %}

   (b): {% csrf_token %}

   (c):  value="{{ reservation.name }}''

   (d): value="{{ reservation.date }}"

   

2. reservations:delete

   

3. (a):reservation_id

   (b): delete

   (c): reservation:index

   

4. GET

   - 서버로부터 정보를 조회하기 위한 http 메서드
   - 데이터 크기 제한..

   POST

   - 서버에서 리소스를 생성, 수정,  삭제 등 변경하기 위한 http 메서드
   - 데이터를 http body에 담아서 보내기 때문에 길이의 제한 없이 데이터 전송 가능
   - url에 안보인다고 해서 안전하다고 생각될 수 있지만, 개발자 도구나 다른 개발 툴을 이용하면 확인이 가능. 반드시 민감한 정보의 경우 암호화해서 전송해야함
   - 게시판 글 작성, 사용자 추가, 회원가입