'''
p.149 DFS_음료수 얼려먹기
# N x M 크기의 얼음 틀이 있다. 구멍이 뚫린 부분은 0, 칸막이가 존재하는 부분은 1로 표시한다.
# 구멍이 뚫린 부분끼리 상,하,좌,우 붙어 있는 경우 연결된 걸로 간주한다.
# 이때 얼음 틀의 모양이 주어졌을 때, 생성되는 총 아이스크림의 개수를 구하는 프로그램 작성
<입력조건>
1. 첫 번째 줄에 얼음 틀의 세로 길이 n과 가로길이 m이 주어진다
2. 두 번째 줄부터 n+1 번째 줄까지 얼음 틀의 형태가 주어진다.
3. 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.

<출력조건>
1. 한 번에 만들 수 있는 아이스크림의 개수를 출력한다.
'''
n,m= map(int, input().split())

#얼음 틀 모양 입력받기
tray=[]
for i in range(n):
    tray.append(list(map(int,input())))

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if tray[x][y]==0:
        tray[x][y]=1 #방문처리
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result=0

for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1
print(result)
        
    
