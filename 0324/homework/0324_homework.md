# 0324_homework

```html
<div class="{a}">
    <div class="{b}">
        <div class="col-{c}-{d}">...		</div>
    </div>
</div>
```

1. 상단 코드에 Bootstrap Grid System을 적용시키고자 할 때, {a},{b} 각각에 입력해야 할 클래스 이름을 작성하시오.

   - {a} : container

   - {b} : row





2.Bootstrap Grid System에서 요소의 크기를 지정하기 위해서는 상단 코드와 같은 형태로 클래스 이름을 지정해야 한다.

- {c}에 들어갈 수 있는 값과 그 값들이 가지는 의미를 작성하시오.
  
  - `{c} : 넓이에 따른 아이템 배치를 위해 각각 고유의 breakpoint`
    -  sm
    -  md
    -  lg
    -  xl
- {d}에 들어갈 수 있는 값과 그 값들이 가지는 의미를 작성하시오.
  
  - {d}
  
    - 12이하의 수: 12개로 나누어진 공간중에 몇칸을 차지하는지 정의
  
    



3. Align-items-center를 사용하려면 d-flex 클래스와 함께 사용하여야 했었다. 그러나, Grid System 에서는 d-flex 클래스를 생략하여도 올바르게 동작한다. 그 이유를 작성하시오.
   - `row에 이미 display: flex 를 가지고 있다.`

```html
<div class="container">
    <div class="row align-items-center">
        <div class="col">
            One of three columns
        </div>
        <div class="col">
            One of three columns
        </div>
        <div class="col">
            One of three columns
        </div>
    </div>
</div>
```



4.  Nav를 그림과 같이 오른쪽 정렬 하고자 할 때 {a}에 들어가야 할 클래스 이름을 작성하시오.

   ​																						Active		Link

   ```html
   <ul class="nav {a}">
       <li class="nav-item">
       	<a class="nav-link active" href>Active</a>
       </li>
       <li class="nav-item">
       	<a class="nav-link" href>Link</a>
       </li>
   </ul>
   ```

   - `justify-content: end`