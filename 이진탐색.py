"""             #백준 1920번 수 찾기
0. 문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 
이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

1. 아이디어
- N개의 숫자를 정렬
- M개를 for문 돌면서 이진탐색
- 이진탐색 안에서 마지막에 데이터를 찾으면 1출력 아니면 0출력

2. 시간복잡도
- N개 입력 값 정렬 = O(NlogN)
- M개를 N개 중에서 탐색 = O(M * logN)
- 총합 : O((N+M)logN) > 가능

3. 자료구조
- N개 숫자 : int[]
- M개 숫자 : int[]
"""

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
M = int(input())
target_list = list(map(int,input().split()))

nums.sort() # 이진탐색 가능

def search(st,en,target):
    if st == en:
        if nums[st]==target:
            print(1)
        else:
            print(0)
        return
    mid = (st+en)//2
    if nums[mid]<target:
        search(mid+1,en,target)
    else:
        search(st,mid,target)
        

for each_target in target_list:
    search(0,N-1,each_target)
