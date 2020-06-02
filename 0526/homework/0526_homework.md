# 0526_homework

1. computed와 watch의 개념과 그 차이에 대해서 간략하게 설명하시오.

   ```markdown
   computed
   계산해야 하는 목표 데이터를 정의하는 방식으로, 해당 속성이 종속된 대상이 변경될 때만 함수를 실행.
   단순히 데이터로부터 계산된 값을 출력하기 위한 속성.
   선언형 프로그래밍 방식 (무엇을 할지 나열,What)
   
   Watch
   감시할 데이터를 지정하고 그 데이터가 바뀌면 이런 함수를 실행하는 방식.
   데이터의 변경을 관찰하고 이에 일어날 동작을 설정하기 위한 속성.
   명령형 프로그래밍 방식(어떻게 할지를 구현,how)
   
   일반적으로 선언형 프로그래밍이 명령형 프로그래밍보다 코드 반복이 적은 등 우수하다고 평가하는 경향이 있음
   ```

   

2. 아래의 설명을 읽고 T/F 여부를 작성하시오.. 

   - 동일한 노드에 v-for와 v-if, 두 디렉티브가 함께 있다면 v-if가 더 높은 우선 순위를 가지며, v-if는 루프가 반복 될 때마다 실행된다. `F`

   -  Vue.js에서 HTML 속성에 Interpolation(보간법) 형태로 값을 넣을 수 있지만 코드 작성의 통일성을 위해 v-bind 디렉티브를 사용한다. `F`

   -  v-bind 디렉티브는 “ @ “, v-on 디렉티브는 “ : ” shortcut(약어)을 제공한다. `F`

   -  v-model 디렉티브는 input, textarea, select 같은 HTML Element와 단방향 데이터 바인딩을 이루기 때문에 v-model 속성값의 제어를 통해 값을 바꿀 수 있다.`F`

     

3. 다음의 빈칸 (a), (b), (c), (d)에 들어갈 코드를 작성하시오.

![image-20200526173125159](0526_homework.assets/image-20200526173125159.png)

```
(a): v-for
(b): v-if
(c): {{ number }}
(d): data
```
