#p.116 구현_ 왕실의 나이트
#나이트는 특정 위치에서 L자 형태로만 이동할 수 있다. (수직 2칸 수평 1한or 수직 1칸 수평2칸)
#<입력조건>
#- 첫째 줄에 8x8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다. 입력 문자는 a1처럼 열과 행으로 이뤄진다.
#<출력조건>
#- 첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오

move=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
point=input()


x=int(ord(point[0]))-int(ord('a'))+1
y=int(point[1])

result=0

for i in move:
    nx=x+i[0]
    ny=y+i[1]
    
    if(nx<1 or nx>8 or ny>8 or ny<1):
        continue
    result+=1

print(result)