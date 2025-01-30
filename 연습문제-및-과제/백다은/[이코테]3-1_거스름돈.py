# 이코테 87p 거스름돈 문제
# 거스름돈 500원, 100원, 50원, 10원
# 큰 단위부터 사용해서 최적의 해를 찾는다(그리디 사용)

# 값 입력 받기
n = int(input())
count = 0

# 거스름돈이 0원이 될 때까지 반복
while n > 0:
    # 거스름돈이 500원보다 많을 경우
    if n >= 500:
        count += n // 500 # 거슬러준 화폐 갯수 더해주기
        n %= 500 # 거스름돈 남은 금액 계산
    elif n >= 100:
        count += n // 100
        n %= 100
    elif n >= 50:
        count += n // 50
        n %= 50
    else:
        count += n // 10
        n %= 10

# 값 출력
print(count)


# # 개선점
# # for문을 사용하면 더 간결한 코드 작성이 가능하다
# # 거스름돈 최소 개수 구하기 (그리디)
# n = int(input())
# count = 0
#
# # 동전 단위를 큰 것부터 리스트로 저장
# coins = [500, 100, 50, 10]
#
# for coin in coins:
#     count += n // coin  # 해당 동전으로 줄 수 있는 개수 추가
#     n %= coin           # 남은 거스름돈 계산
#
# print(count)
