import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

sum = 0 
cnt =0
for x in a:
    if x == 1:     #i번째 수가 1이라면  
        cnt += 1       # 점수에 1점 더하기
        sum += cnt 
    else:
        cnt = 0
        
     

print(sum)