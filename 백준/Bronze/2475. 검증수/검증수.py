import sys
#정수형으로 입력받기 위해 map 함수 사용
num = list(map(int, sys.stdin.readline().split()))
#좀 더 빠른 입력을 위해 input이 아닌 sys.stdin.readline()을 사용
sum = 0
#입력받은 수들을 제곱하여 sum에 추가
for i in num:
    sum += i**2
#sum을 10으로 나눈 나머지인 검증수를 출력
print(sum % 10)
