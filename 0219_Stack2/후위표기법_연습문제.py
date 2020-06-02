pro = '(6+5*(2-8)/2)'
stack = []
result = []
top = -1
isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}

for i in range(len(pro)):
    if i == 0:
        if pro[i].isdecimal():
            result.append(pro[i])
        else:
            stack.append(pro[i])

    # if len(result) == 0:
    #     result.append(pro[i])
    else:

        if pro[i].isdecimal():
            result.append(pro[i])


        else:
            if pro[i] == ')':
                while stack[-1] != '(':
                    p = stack.pop(-1)
                    result.append(p)
                stack.pop(-1)

            else:
                if isp[pro[i]] > isp[stack[-1]]:
                    stack.append(pro[i])
                else:
                    if pro[i] =='(':
                        stack.append(pro[i])
                    else:
                        p = stack.pop(-1)
                        result.append(p)
                        stack.append(pro[i])

for i in range(len(stack)-1, -1, -1):
    result.append(stack[i])

print(''.join(result))
