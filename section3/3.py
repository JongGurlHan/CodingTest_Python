import sys
sys.stdin=open("input.txt", "rt")

a=list(range(21))

for _ in range(10):
    s, e = map(int, input().split())
    for i in range(e-s+1//2):