#p.118 구현_게임개발
#<입력조건>
#- 첫째 줄에 맵의 세로 크기 N과 가로 크기 M을 공백으로 구분하여 입력한다(3<=N, M<=50)
#- 둘째 줄에 게임 캐릭터가 있는 칸의 좌표(A,B)와 바라보는 방향 d가 각각 서로 공백으로 구분하여 주어진다. 방향 d의 값으로는 다음과 같이 4가지 존재한다.
#- 0: 북쪽, 1: 동쪽 , 2: 남쪽 , 3: 서쪽
#- 셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어진다. N개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로, 각 줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다. 맵의 외곽은 항상 바다로 되어 있다.
#- 0:육지 1: 바다
#- 처음에 게임 캐럭티가 위치한 칸의 상태는 항상 육지이다
#<출력조건>
#- 첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력한다.

dx=[-1,0,1,0]
dy=[0,1,0,-1]

n,m= map(int,input().split())
a,b,d=map(int,input().split())

arr_map=[]
for i in range(n):
    arr_map.append(list(map(int, input().split()))) # 맵 정보 입력받기

#왼쪽으로 회전
def turn_left():
     global d
     d-=1
     if d==-1:
         d=3
 
#바다 1 육지 0 가본 곳 2
result=1 #방문횟수 카운트
arr_map[a][b]=2 #시작 위치는 방문함
while(1):
    change=False
    for _ in range(4): #왼쪽으로 돌면서 방문 가능한 곳 확인
        turn_left()
        na=a+dx[d]
        nb=b+dy[d]
        if(arr_map[na][nb]==0): #방문하지 않은 육지가 존재하는 경우
            result+=1
            a=na
            b=nb
            arr_map[a][b]=2 #이동
            change=True
            break
            
    if(change==False): #회전한 후 모두 방문한 칸이거나 바다인 경우
        na=a+dx[(d+2)%4]
        nb=b+dy[(d+2)%4]
        if(arr_map[na][nb]!=1):
            a=na
            b=nb
        else: #뒤가 바다로 막힌경우
            break
print(result)            
  
    
