import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

avg = round(sum(a) / n)
minNum = 1000000

for idx, x in enumerate(a):
    gap = abs(x - avg)
    if  gap < minNum:
        minNum =  gap
        score = x   
        res = idx +1     
    elif minNum == gap:
        if score < x:
            res = idx+1
            break

print(avg, res)

            

