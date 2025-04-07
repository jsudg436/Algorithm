import sys
N = int(sys.stdin.readline())

#범위를 -N+1 부터 N-1까지 돌게하면서 abs 함수를 같이 사용해 증감하는 패턴을 절댓값을 사용해 하나의 반복문으로 표현
for i in range(-N + 1, N):
    print(' ' * abs(i) + '*' * (2 * (N - abs(i)) - 1))

# 기존 코드
# for i in range(1, 2 * N):
#     M = abs(N - i)
#     print(' ' * M + '*' * ((2*N-1)-2*M))
