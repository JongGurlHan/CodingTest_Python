import sys
sys.stdin=open("input.txt", "rt")

n = input()
a =''
cnt =0
for i in range(len(n)):   
    if n[i].isdigit(): #0~9의 숫자가 맞는지
        a+=n[i]
a = int(a)

for i in range(1, a+1):
    if a % i == 0:
        cnt += 1

print(a)
print(cnt)