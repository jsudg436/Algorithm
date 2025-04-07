import sys
N = int(sys.stdin.readline())

for i in range(-N + 1, N):
    print(' ' * abs(i) + '*' * (2 * (N - abs(i)) - 1))

# 기존 코드
# for i in range(1, 2 * N):
#     M = abs(N - i)
#     print(' ' * M + '*' * ((2*N-1)-2*M))