"""             #백준 11047 동전 0
0. 문제
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 
이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. 
(1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

1. 아이디어
- 동전을 저장한 뒤 반대로 뒤집음
- 동전 for >
    - 동전 사용 개수 추가
    - 동전 사용한만큼 K값 갱신

2. 시간복잡도
- O(N)

3. 자료구조
- 동전 금액 : int[]
- 동전 사용 cnt : int
- 남은 금액 : int
"""

import sys
input = sys.stdin.readline

N,K = map(int,input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()
cnt = 0

for each_coin in coins:
    cnt += K // each_coin
    K = K % each_coin

print(cnt)