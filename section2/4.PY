import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

avg = round(sum(a) / n)
min = 100000

for i, v in enumerate(a):
    gap = abs(avg-v)
    if gap < min:
        min = gap
        score = v
        loca = i +1
    elif gap == min:
        if score < v:
            score =v
            loca = i+1

print(avg , loca)


