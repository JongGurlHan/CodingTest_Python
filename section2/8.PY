import sys
sys.stdin=open("H:/Study/CodingTest_Python/input.txt", "rt")

n = int(input())
n_list = list(map(int, input().split()))

def reverse(x):
    x = str(x)[::-1]
    x = int(x)
    return x

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False        
    return True    
            
for i in n_list: 
    reNum = reverse(i)
    if isPrime(reNum) == True:
        print(reNum, end= ' ' )