import sys
N = int(sys.stdin.readline())

arr = [[0] * 101 for _ in range(101)]

for _ in range(N):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            arr[i][j] = 1

num = 0
for i in arr:
    num += sum(i)

print(num)