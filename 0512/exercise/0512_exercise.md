# 0512_exercise

### 타입과 연산자

primitive 타입

```javascript
// Number
let a = 13
let b = 3.14
let c = 4.123e8 // 4.123 * 10^8
let d = Infinity
let e = -Infinity
let f = NaN

// String
// 곱셉, 나눗셈, 뺄셈은 불가능, 덧세만 가능
let sentence1 = 'hello js'
let sentence2 = 'bye'
let newSentence = sentence1 + sentence2

// Template Literal
// ES6+ 부터 지원, Backtick(`)을 이용하며, 여러줄에 걸쳐 문자열을 정의할수도 있고, JS의 변수를 문자열 안에 바로 사용할 수 있다.
let name = `안녕하
세요`

let age = 1
let greeting = `안녕하세요 저는 ${age}살 입니다.`

// Boolean
// true, false

// Empty Value
// JS는 값이 존재하지 않음을 표현하는 값으로 undefined, null이 있다.
```

연산자

```javascript
// 할당연산자
let g = 0

// 비교연산자
// >, >=, <, <=

// 동등연산자
// ==
// 메모리의 같은 객체를 가리키거나 같은 값을 같도록 변환할 수 있다면 서로 같다고 판단한다.

// 일치연산자
// ===
// 메모리의 같은 객체를 가리키거나 같은 타입이며, 같은 값인지 비교한다.

// 논리연산자
// 불리언 타입을 연산할 수 있는 연산자
// &&(and), ||(or), !(not)
true && true
false || true
!true

// 삼항연산자
// 가장 앞 조건식이 참이면 ':' 앞의 값이 반환 반대일경우 뒤의 값이 반환
true ? 1 : 2 // 1
false ? 1 : 2 // 2

let myNumber = Math.PI > 4 ? 'Yeeeh' : 'Noooo'

```

### 조건문

if , else if, else

```javascript
if (day === 1) {
    console.log('월요일')
} else if (day === 2) {
    console.log('화요일')
} else if (day === 3) {
    console.log('수요일')
} else if (day === 4) {
    console.log('목요일')
} else if (day === 5) {
    console.log('금요일')
} else if (day === 6) {
    console.log('토요일')
} else {
    console.log('일요일')
}
```

switch

```javascript
switch(day) {
        case 1:{
        console.log('월요일')
        break
    }
        case 2:{
        console.log('화요일')
        break
    }
        case 3:{
        console.log('수요일')
        break
    }
        case 4:{
        console.log('목요일')
        break
    }
        case 5:{
        console.log('금요일')
        break
    }
        case 6:{
        console.log('토요일')
        break
    }
        case 7:{
        console.log('일요일')
        break
    }
        default:{
        console.log('날짜를 입력하세요')
        break
    }
}
```

### 반복문

while

```javascript
let num = 0
while (num>5){
    console.log(num)
    num++
}
```

for

```javascript
for (let i = 0; i < 6; i++){
    console.log(i)
}
```

for of

```javascript
const numbers = [0, 1, 2, 3, 4]
for (const number of numbers) {
    console.log(number)
}
```

for in

```javascript
for (const fruit in fruits) {
    console.log(fruit)
    console.log(fruits[key])
}
```

continue

```javascript
for (let i = 0; i < 10; i++){
    if (i === 3){
        continue
    }
    console.log(i)
}
```



### 함수

선언식

```javascript
function add(num1, num2){
    return num1 + num2
}
```

표현식

```javascript
const sub = function(num1, num2){
    return num1 - num2
}
```

기본값인자

```javascript
const myFunc = function(name='greeting'){
    console.log(`hi ${name}`)
}
```

화살표 함수

```javascript
let arrow = (name) => { return `hello ${name}`}
let arrow = name => { return `hello ${name}`}
let arrow = name => `hello ${name}`

// 인자가 없는 경우 `()` 또는 `_`
let arrow2 = _ => 'hello'

// object를 return 하는 경우 -1
let retunObject = () => { return { key: value}}

// object를 return 하는 경우 -2
// return과 {}(중괄호)를 생략한다면 반드시 ()로 감싸줘야 한다.
let returnObject = () => ({ key: value})
```



### 자료구조

배열

```javascript
let numbers = [1, 2, 3, 4]

//배열의 인덱스 접근
numbers[0]
numbers[-1]
numbers.length

//자주 쓰이는 배열 매서드
// push & pop
// 요소를 배열의 가장 뒤에 추가하거나 제거
numbers.push('a') // [1, 2, 3, 4, 'a']
numbers.pop() // 'a', 가장 마지막 요소 제거

// unshift & shift
// 요소를 배ㅕㅇㄹ의 가장 앞에 추가하거나 제거
numbers.unshift('a') // ['a', 1, 2, 3, 4]
numbers.shift('a') // 

// includes
numbers.includes(1) // true
numbers.includes(100) // false

// indexOf
// 배열에 특정요소가 있는지 여부를 확인 후 
// 가장 첫번째로 찾은 요소의 인덱스 값을 반환
// 요소가 없다면 -1을 반환
let numbers = [1, 2, 3, 4, 'a', 'a']
numbers.indexOf('a') // 4

// join
// 배열의 요소를 함수의 인자를 기준으로 이어서 문자열을 반환
// 함수의 인자가 없다면 ',' 기준으로 이어서 문자열을 반환
// [주의] 원본은 바뀌지 않는다.
numbers.join() // '1,2,3,4,a,a'
numbers.join('') //'1234aa'
numbers.join('-') // '1-2-3-4-a-a'
```

오브젝트

```javascript
//오브젝트 내 요소의 접근
const me = {
    name: '박현우', 
    'phone number' : '010-1111-1111',
    Product: {
        phone: 'galaxy10',
        labtop : 'gram15'
    }
}

me.name // 박현우
me['name'] // 박현우
me['phone number'] // 010-1111-1111
me.Product // { phone: 'galaxy10', labtop: 'gram15'}
me.Product.labtop // gram15

//오브젝트 -> 배열 반환 메서드
let box = {a: 'apple', b: 'banana'}
Object.keys(box) // ["a", "b"]

// Object.values
// Object의 value값을 배열로 반환
let box = {a: 'apple', b: 'banana'}
Object.values(box) // ['apple', 'banana']

// Object.entries
// Object의 key--value값 배열로 반환
Object.entries(box) // [["a", "apple"], ["b", "banana"]]

// 오브젝트 리터럴
// 객체의 key와 value의 이름이 같다면, 마치 배열을 정의하는 것처럼 한번만 작성 가능
let books = ['Learning Python', 'Learning JS']

let comics = {
    DC: ['WonderWoman', 'Aquaman'],
    Marvel: ['Black Widow', 'Avengers']
}

let bookshop = {
    books, 
    comics
}

console.log(bookshop)
// let bookshop = {
//     books: ['Learning Python', 'Learning JS'], 
//     comics: {
//      DC: ['WonderWoman', 'Aquaman'],
//      Marvel: ['Black Widow', 'Avengers']
//  }
// }
```

json <-> Object

```javascript
// JSON -> Object
let jsonData = JSON.stringify({
  coffee: "Starbucks",
  iceCream: "MinChoco"
});

console.log(jsonData); // {'coffee':'Starbucks', 'iceCream':'MinChoco'}
console.log(typeof jsonData); // string

// Object -> JSON
let parsedData = JSON.parse(jsonData);

console.log(parsedData); // {coffee:'Starbucks', 'iceCream': 'Mint Choco'}
console.log(typeof parsedData); // object
```

