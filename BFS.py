"""             #백준 1926번 문제
1. 아이디어
- 2중 for => 값 1 && 방문X => BFS
- BFS 돌면서 그림 개수 +1, 최대값을 계산

2. 시간복잡도
세로 크기 n(1<=n<=500) 가로 크기 m(1<=m<=500)
BFS : O(V+E) = V + E = V + 4V = 5V = 5 * 250000 = 100만 < 2억 >> 가능!
V : m X n = 500 * 500       (버텍스 개수)
E : V X 4 = 500 * 500 * 4   (간선 개수)

3. 자료구조
- 그래프 전체 지도 : int[][]
- 방문 : bool[][]
- Queue(BFS)
"""

import sys
input = sys.stdin.readline

n,m= map(int ,input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False]*m for _ in range(n)]


dy = [0,1,0,-1]       # dy,dx = 0,1 -> 오른쪽 , 순서대로 아래 왼 위
dx = [1,0,-1,0]

def bfs(y,x):
    rs = 1
    q = [(y,x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if map[ny][nx] ==1 and chk[ny][nx] == False:
                    rs +=1
                    chk[ny][nx] = True
                    q.append((ny,nx))
    return rs

cnt = 0
maxv = 0

for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            #전체 그림 개수 +1
            cnt +=1
            #BFS > 그림 크기를 구해주고 최대값 갱신
            maxv = max(maxv,bfs(j,i))
            

print(cnt)
print(maxv)