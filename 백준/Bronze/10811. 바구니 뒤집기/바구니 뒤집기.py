import sys
# 입력받은 2개의 숫자를 정수로 변환하기 위해 map 함수 사용
N, M = map(int, sys.stdin.readline().split())
# 1부터 N까지 순서대로 정렬된 리스트 생성
lst = list(range(1, N + 1))

for m in range(M):
  # for문으로 M번 동안 역순으로 바꿀 바구니의 범위 입력
  i, j = map(int, sys.stdin.readline().split())
  temp = lst[i-1:j]   # 입력받은 범위만큼 추출
  temp.reverse()      # 역순으로 정렬
  del lst[i-1:j]      # 기존 리스트의 원소 삭제
  lst[i-1:i-1] = temp

  # 기존코드
  # # for문으로 순서대로 원소 하나씩 추가
  # for n in range(len(temp)):
  #   lst.insert(i-1+n, temp[n])
  
# 최종 바구니 순서 출력
print(*lst)