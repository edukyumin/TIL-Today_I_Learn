1. flights 테이블을 생성하시오.

   ```SQL
   CREATE TABLE flights(
      ...> id INTEGER PRIMARY KEY AUTOINCREMENT,
      ...> flight_num TEXT NOT NULL,
      ...> departure TEXT NOT NULL,
      ...> waypoint TEXT,
      ...> arrival TEXT,
      ...> price INTEGER
      ...> );
   ```

   

2. 데이터를 입력하시오.

   ```sql
   INSERT INTO flights VAlUES (1, 'RT9122', 'Madrid', 'Beijing', 'Incheon', 200),(2, 'XZ0352', 'LA', 'Moscow', 'Incheon', 800),(3, 'SQ0972', 'London', 'Beijing', 'Sydney', 500) ;
   ```

   

3.  flights 테이블 전체 데이터를 조회하시오.

   ```SQL
   .mode column
   select * FROM flights;
   ```

   

4. 모든 waypoint를 조회하시오.

   ```SQL
   select waypoints from flights;
   ```

   

5. 항공권 가격이 600 미만인 항공편들의 id와 flight_num을 조회하시오.

   ```SQL
   select id, flight_num from flights where price<600;
   ```

   

6. 도착지가 Incheon이고 가격이 500 이상인 항공편의 departure를 조회하시오.

   ```SQL
   select departure from flights where arrival='Incheon' and price>500;
   departure;
   ```

   

7. 항공편의 숫자부분이 0으로 시작하고 2로 끝나면서 경유지가 Beijing인 항공편들의 id와 flight_num을 조회하시오.

   ```SQL
    select id, flight_num from flights where flight_num LIKE '%0%2' AND  waypoint='Beijing';
   ```

   

8. 항공편 SQ0972의 경유지를 Tokyo로 수정하시오.

   ```SQL
   UPDATE flights SET waypoing='Tokyo' where flight_num='SQ0972';
   ```

   

9. 항공편 RT9122를 테이블에서 삭제하시오.

   ```SQL
   DELETE FROM flights where flight_num='RT9122';
   ```

   

10. flights 테이블을 삭제하시오.

    ```SQL
     DROP TABLE flights;  
    ```

    