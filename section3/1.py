import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
for i in range(n):
    a = list(input().lower())
    
    lenA = len(a) #리스트 길이
    count =0
    for j in range(lenA // 2 ):
        if a[j] == a[lenA-1-j]:
            continue
        else:
            count+=1
    if count ==0:
        print('#',i+1, ' YES')
    else:
        print('#',i+1, ' NO')


    

    