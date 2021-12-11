import sys
import collections

#sys.stdin=open("input.txt", "rt")

n, m = map(int, input().split())
cnt = [0]*(n+m+3)
result = []

for i in range(1, n+1):
    for j in range(1, m+1):
        result.append(i+j)


for num in result:
    cnt[num] +=1

maxnum = max(cnt)

for i in range(len(cnt)):
    if cnt[i] == maxnum:
        print(i, end=' ')

# print(cnt)
# print(maxnum)