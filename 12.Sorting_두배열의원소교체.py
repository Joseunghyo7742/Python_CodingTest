'''
p.182 정렬_ 두 배열의 원소 교체
<입력조건>
- 첫 번째 줄에 n,k가 공백으로 구분되어 입력된다.
- 두 번째 줄에 배열 a의 원소들이 공백으로 구분되어 입력된다. 모든 원소는 10,000,000 보다 작은 자연수이다.
- 세 번째 줄에 배열 b의 원소들이 공백으로 구분되어 입력된다. 모든 원소는 10,000,000 보다 작은 자연수입니다.
<출력조건>
- 최대 k번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 a의 모든 원소의 합의 최댓값을 출력한다.
'''
n,k= map(int,(input().split()))
arr_A=list(map(int,input().split()))
arr_B=list(map(int,input().split()))

arr_A.sort()
arr_B.sort(reverse=True)

for i in range(k):
    if arr_A[i]<arr_B[i]:
        arr_A[i],arr_B[i]=arr_B[i],arr_A[i]
    else:
        break

print(sum(arr_A))