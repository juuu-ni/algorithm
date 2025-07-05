"""             #백준 15649번 문제
0. 문제
자연수 N과 M이 주어졌을 때, 
아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열  (1 ≤ M ≤ N ≤ 8)

1. 아이디어
- 백트래킹 재귀함수 안에서 , for문 돌면서 숫자 선택 (이때 방문여부 확인)
- 재귀함수에서 M개를 선택 할 경우 print

2. 시간복잡도
N^N : 중복이 가능 , N=8까지 가능 < 2억
N!  : 중복이 불가 , N=10까지 가능
- N! > 가능

3. 자료구조
- 결과값 저장 int[]
- 방문여부 체크 bool[]
"""

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
rs = []
chk = [False] * (N+1)

def recur(num):
    if num == M :
        print(' '.join(map(str,rs)))
        return
    for i in  range(1,N+1):
        if chk[i]==False:

            chk[i]=True
            rs.append(i)
            recur(num+1)

            chk[i]=False
            rs.pop()

recur(0)
