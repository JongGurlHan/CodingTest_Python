import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
res=0
for i in range(n):
    tmp = input().split()
    tmp.sort() #문자열 오름차순
    a,b,c = map(int, tmp) 

    if a==b and b==c: #3개 모두 같을때
        money=10000+a*1000
    elif a==b or a==c: #2개가 같을때
        money=1000+(a*100)
    elif b==c: #2개가 같을때
        money=1000+(b*100)
    else:
        money=c*100 #다 다를때 - 가장 큰 c기준
    if money>res:
        res=money

print(res)
