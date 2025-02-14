from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)

    while q:
        x = q.popleft()
        cnt = 0

        for i in q:
            if x <= i:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
    return answer


#전체 다 탐색하면 O(n^2)이라서 큐로 풀어서 O(n)
