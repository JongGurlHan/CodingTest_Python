import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
x = list(map(int, input().split()))


def digit_sum(x):
    for i in x:
        new = str(i) #숫자를 문자열로 변환 123 => '123'
        add = 0
        for j in range(len(new)):
            add += int(new[j])
    return add

max =0
if add > max:
    max = add
    
   

