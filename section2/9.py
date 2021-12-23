import sys
sys.stdin=open("H:/Study/CodingTest_Python/input.txt", "rt")

n = int(input())

max = 0
price = 0

for _ in range(n):
    
    a = list(map(int, input().split())) #주사위 눈 3개 가져오기  
    if a[0] == a[1] == a[2]:
        price = 10000 + a[0]*1000
        print(price)
        
    if price > max:
        max = price       
            
        
print(max)

# testlist = [1 , 2, 2]
# print(set(testlist))
# print(stats.mode(testlist))


# def prizeMoney(a):
#     res = 0
#     if len(set(a)) == 1: #3개 값이 모두 같을때
#         res = 10000 + a[0]*1000
#     elif len(set(a)) == 2: #2개 값이 같을때
#         ma
