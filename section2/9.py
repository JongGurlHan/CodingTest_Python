import sys
sys.stdin=open("input.txt", "rt")

n = int(input())

maxPrice = 0
price = 0

for _ in range(n):    
    a = list(map(int, input().split())) #주사위 눈 3개 가져오기  
    if a[0] == a[1] == a[2]:
        price = 10000 + a[0]*1000
    elif a[0] == a[1] != a[2]:
        price = 1000 + a[0]*100
    elif a[1] == a[2] != a[0]:
        price = 1000 + a[0]*100
    elif a[0] == a[2] != a[1]:
        price = 1000 + a[0]*100
    else:
        price = max(a)*100
        
    if price > maxPrice:
        maxPrice = price   
            
        
print(maxPrice)
