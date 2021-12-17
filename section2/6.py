import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
x = list(map(int, input().split()))

#각 자연수의 자릿수의 합을 구하는 함수
def digit_sum(num):    
    str_num = str(num) #숫자를 문자열로 변환 123 => '123'
    add = 0
    for i in range(len(str_num)):
        add += int(str_num[i])
    return add

max = 0
result = 0

for i in range(len(x)):
    if digit_sum(x[i]) > max:
        max = digit_sum(x[i])
        result = x[i]

print(result)


   

