#p.113 구현_ 시각
#<입력조건>
#- 첫째 줄에 정수N이 입력된다.
#<출력조건>
#- 00시 00분 00초부터 N시 59분 59초까지의모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력

n=int(input()) #N시 59분 59초까지
result=0

for h in range(0,n+1):
    for m in range(0,60):
        for s in range(0,60):
            if('3' in str(h) or '3' in str(m) or '3' in str(s)):
                result+=1
            #if '3' in str(h)+str(m)+str(s) 도 가능
print(result)