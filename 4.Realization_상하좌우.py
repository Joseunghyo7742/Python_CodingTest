#p.111 구현_상하좌우
#<입력조건>
#- 첫째 줄에 공간의 크기를 나타내는 N이 주어진다(1<=N<=100)
#- 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다.(1<=이동횟수 <=100)
#<출력조건>
#- 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (x,y)를 공백으로 구분하여 출력한다.

n=int(input())
move_plan=input().split()

x,y=1,1
dx=[0,0,-1,1]
dy=[-1,1,0,0]
move=['L','R','U','D']

for i in move_plan:
    for j in range (len(move)):
        if(i == move[j]):
            nx=x+dx[j]
            ny=y+dy[j]
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    
    x,y= nx,ny

print(x,y)
