import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
for i in range(n):
    s = input().upper()
    size = len(s)

    for j in range(size//2):
        if s[j] != s[-1-j]:                       
            print('#%d NO' %(i+1))
            break
        print('#%d YES' %(i+1))

    
    