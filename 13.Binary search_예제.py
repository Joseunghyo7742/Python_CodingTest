'''
p.186 이진탐색_ 순차탐색
- 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법.
- 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용한다.
'''
def sequential_search(n, target, array):
    #각 원소를 하나씩 확인하며
    for i in range(n):
        #현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i]== target:
            return i+1 #현재의 위치 반환
        
print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요")
input_data= input().split()
n= int(input_data[0]) #원소의 개수
target= input_data[1] #찾고자 하는 문자열

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array= input().split()

print(sequential_search(n,target,array))

'''
p.188 이진탐색_이진탐색
- 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘
- 위치를 나타내는 변수 3개 사용: 시작점, 끝점, 중간점
- 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 과정
'''
#재귀 함수로 구현한 이진탐색
def binary_search(array, target, start, end):
    if start> end:
        return None
    mid= (start+end)//2
    
    # 찾은 경우 중간점 인덱스 반환
    if array[mid]== target:
        return mid
    #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    
    #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)
    
    
    n,target= list(map(int, input().split()))
    array=list(map(int,input().split()))
    
    result= binary_search(array, target, 0, n-1)
    if result ==None:
        print("원소가 존재하지 않습니다")
    else:
        print(result+1)