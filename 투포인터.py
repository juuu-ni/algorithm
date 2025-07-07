"""             #백준 2559번 수열   
0. 문제
첫째 줄에는 두 개의 정수 N과 K가 한 개의 공백을 사이에 두고 순서대로 주어진다. 
첫 번째 정수 N은 온도를 측정한 전체 날짜의 수이다. 
N은 2 이상 100,000 이하이다. 
두 번째 정수 K는 합을 구하기 위한 연속적인 날짜의 수이다. K는 1과 N 사이의 정수이다. 
둘째 줄에는 매일 측정한 온도를 나타내는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 수들은 모두 -100 이상 100 이하이다.

1. 아이디어
- 투포인터를 활용
- for문으로 처음에 K개 값을 저장
- 다음 인덱스 더해주고, 이전 인덱스 빼줌
- 이때마다 최대값 갱신
2. 시간복잡도
- O(N) = 10000 = 1e5 > 가능

3. 자료구조
- 각 숫자들 N개 저장 배열 : int[]
    - 숫자들 최대 100 > INT 가능
- K개의 값을 저장 할 변수 : int
    - 최대 : K * 100 = 1e5 * 100 = 1e7 > INT 가능
- 최대값 : int 

"""

import sys
input = sys.stdin.readline

N,K = map(int,input().split())
nums = list(map(int,input().split()))
each = 0

# K개를 더해주기
for i in range(K):
    each += nums[i]
maxv = each

# 다음인덱스 더해주고 , 이전인덱스 빼주기
for i in range(K,N):
    each += nums[i]
    each -= nums[i-K]
    maxv = max(maxv, each)

print(maxv)


