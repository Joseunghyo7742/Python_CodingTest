#p.96 그리디- 숫자 카드 게임
#입력조건: 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 자연수로 주어진다.
#둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1 이상 10,000 이하의 자연수

#출력 조건: 행을 선택한 후, 행에서 가장 숫자가 낮은 카드를 뽑아야 한다. 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 한다.

n,m= map(int,input().split())

result= 0

for i in range(n):
    arr=list(map(int,input().split()))
    min_v=min(arr) #행에서 가장 작은 숫자 저장
    result= max(result , min_v) #result와 min_v 중 큰 값을 저장 
    
print(result)