# 0512_homework

1. “Javascript는 __(a)__를 조작할 수 있는 유일한 언어이며 전세계에서 가장 인기 있는 프로그래밍 언어 중 하나 이다.” __(a)__에 들어 갈 말을 작성하시오.

```
1번
(a): 브라우저
```



2. Javascript에서 변수를 다룰 때 사용하는 키워드는 크게 var, let, const 3가지가 있다. 각각의 핵심 특징을 나열하고 block scope와 function scope의 차이를 나타내는 예시를 작성하시오.
   - var
   - let 
   - const

```
2번
var는 function-scoped고 
let, const는 block-scoped다
let은 변수의 재할당이 가능하지만
const는 재할당이 불가능하다

Function Scope와 Block Scope의 차이
var a = 1
let b = 2

if (a === 1){
    var a = 11
    let b = 22

    console.log(a) // 11 전역변수 a 덮어씌워짐
    console.log(b) // 22
}

console.log(a) // 11
console.log(b) // 2
```



3. 아래의 설명을 읽고 T/F 여부를 작성하시오. - javascript에서는 python의 type()과 비슷하게 typeof 연산자를 통해서 자료형을 파악할 수 있다. - JSON은 Javascript Object Notation의 약자로 Javascript의 Object 표기법을 따른 문자다. - 화살표 함수는 함수의 선언식 & 표현식과 문법적으로 차이가 있지만 내부 동작은 완전히 동일하기 때문에 무엇을 사용하든 관계없다. - null과 undefined는 javascript의 설계상의 실수이며 typeof 연산자를 통해 확인해보면 모두 undefined로 나온다,

```
3번
T
T
F
F
```





4. 동등 연산자(==)와 일치 연산자(===)의 차이를 간략히 설명하시오.

```
4번
== 연산자는 동등 연산자로, 피연산자가 서로 다른 타입이면 타입을 강제로 변환하여 비교한다. 
하지만 형 변환이 어떻게 되는지 하나하나 외워서 사용하는 것은 복잡하기만 할 뿐이다.
=== 연산자는 일치 연산자로, 두 피연산자를 더 정확하게(엄격하게) 비교한다. 
```

