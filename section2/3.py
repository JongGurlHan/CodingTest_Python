import sys
sys.stdin=open("input.txt", "rt")
#n: 카드수, k:번째수
N, K = map(int, input().split())
a = list(map(int, input().split()))

res =set()

for i in range(N):
    for j in range(i+1, N):
        for m in range(j+1, N):
            res.add(a[i]+a[j]+a[m])

#set()에는 sort가 없어서 다시 리스트로 변환한다.
res = list(res)
res.sort(reverse=True)
print(res[K-1])




