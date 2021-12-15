import sys
sys.stdin=open("input.txt", "rt")

n, m = map(int, input().split())
cnt = [0]*(n+m+3)
max = 0 

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1

#빈도회수의 최대값 찾기
for i in range(n+m+1):
    if cnt[i] > max:
        max = cnt[i]

for i in range(n+m+1):
    if cnt[i] == max:
        print(i, end=' ')

# for i in range(1, n+1):
#     for j in range(1, m+1):
#         result.append(i+j)


# for num in result:
#     cnt[num] +=1

# maxnum = max(cnt)

# for i in range(len(cnt)): 
#     if cnt[i] == maxnum:
#         print(i, end=' ')

