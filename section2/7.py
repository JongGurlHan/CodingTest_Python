import sys
sys.stdin=open("input.txt", "rt")

a = int(input())

def is_prime_number(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

prime_list =[]
for i in range(2, a+1):
    if is_prime_number(i) == True:
        prime_list.append(i)

print(prime_list)
print(len(prime_list))        
        
    

