# String

문자입력을 숫자로 바꿔주는 (int함수) 함수 직접 짜주기

```python
str = '12345'
val = 0
for i in range(len(str)):
    if ord('0') <= ord(str[i]) <= ord('9'):
        digit = ord(str[i]) - ord('0')
    else:
        print('error')
        break
    val = val*10 + digit
print(type(val), val)
```

숫자를 문자로 바꿔주는 (str함수) 함수 직접 짜기

```python
def myitoa(x):
    sr = ''
    while True:
        r = x%10
        sr = sr + chr(r+ord('0'))
        x//=10
        if x == 0:
            break

    s = ''
    for i in range(len(sr) - 1, -1, -1):
        s=s+sr[i]

    return sr
print(type(123))
print(type(myitoa(123)))
```



고지식한 패턴검색 알고리즘

```python
p = 'is'        #찾을 패턴
t = 'this is a book'  #전체 텍스트
M = len(p)  #찾을 패턴 길이
N = len(t)  #전체 텍스트 길이


def BruteForce(p, t):
    i = 0  #t의 인덱스
    j = 0  #p의 인덱스
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M:
        return i-M  #검색 성공
    else:
        return -1  #검색 성공
    
print(BruteForce(p, t))
```



보이어-무어 알고리즘