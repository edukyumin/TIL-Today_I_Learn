# ##완전검색 Baby-gin game   -- 미해결
# ```규민이 짜던코드`````````````````````````````````````````````````
# import random
# card = range(0,10)
# result = []

# for i in range(6):
#     result.append(random.choice(card))
#     result.sort()
# print(result)

# for i in range(4):
#     if result[i] + 1 == result[i+1]:
#         if result[i+1] + 1 == result[i+2]:
#             print('run')
#     else: print('nothing')
# ``````````````````````````````````````````````````````````````````````````````````

##선생님 코드( 교재 page 32)``````````````````````````````````````````````````````````
##탐욕(Greedy)알고리즘
# num = 459789 # Baby Gin 확인할 6자리 수
# c = [0] * 12  # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트

# for i in range(6):
#     c[num % 10] += 1  #해당 원소 있으면 카운트 해주기
#     num //= 10    # 뒤에부터 하나씩 짜르는거

# i=0
# tri = run = 0
# while i < 10:
#     if c[i] >= 3 : #triplete 조사 후 데이터 삭제
#         c[i] -= 3
#         tri += 1
#         continue
#     if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >=1 :  #run 조사 후 데이터 삭제
#         c[i] -= 1
#         c[i+1] -= 1
#         c[i+2] -= 1
#         run += 1
#         continue
#     i += 1

# if run + tri == 2:
#     print('Baby Gin')
# else:
#     print('Lose')
##``````````````````````````````````````````````````````````````````````````````````````````````