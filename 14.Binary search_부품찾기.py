'''
p.197 이진탐색- 부품찾기
<입력조건>
- 첫째 줄에 정수 n이 주어진다.
- 둘째 줄에는 공백으로 구분하여 n개의 정수가 주어진다. 이때 정수 1보다 크고 1,000,000이하이다.
- 셋째 줄에는 정수 M이 주어진다.
- 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000이하이다.
<출력조건>
- 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를 , 없으면 no를 출력한다. 
'''
def binary_search(array, target, start, end):
    while start<= end:
        mid= (start+end)//2
        
        if array[mid]==target:
            return  mid
        elif array[mid]>target:
            end= mid-1
        else:
            start=mid+1
    return None
n= int(input())
arr= list(map(int, input().split()))
arr.sort()

m= int(input())
m_arr=list(map(int,input().split()))

for i in m_arr:
    result= binary_search(arr,i,0,n-1)
    if result != None:
        print('yes',end=' ')
    else:
        print('no',end=' ')