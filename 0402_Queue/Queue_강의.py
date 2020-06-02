#1, 2, 3을 넣는 Queue 코드

def enq(n):
    global rear
    if rear == len(q)-1:
        print('Full')
    else:
        rear += 1
        q[rear] = n


q = [0]*3
front = -1
rear = -1
