'''
p.152 BFS_ 미로탈출
<입력조건>
- 첫째 줄에 두 정수 N,M(4<=N, M<=200)이 주어집니다. 다음 N개의 줄에는 각각 M개의 정수(0 혹은 1)로 미로의 정보가 주어집니다.
각각의 수들은 공백 없이 붙어서 입력으로 제시된다. 또한 시작 칸과 마지막 칸은 항상 1이다.
- 이때 괴물이 있는부분은 0, 괴물 없는 부분은 1이다.
<출력조건>
- 첫째 줄에 최소 이동 칸의 개수를 출력한다.
'''
from collections import deque
n,m= map(int, input().split())
map=[]

for i in range(n):
    map.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    while q:
        x,y= q.popleft()
        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]
            
            if nx<0 or ny<0 or nx>=n or ny >= m or map[nx][ny]==0:
                continue
            
            if map[nx][ny]==1:
                map[nx][ny]= map[x][y]+1
                q.append((nx,ny))
        return map[n-1][m-1]

print(bfs(0,0))
