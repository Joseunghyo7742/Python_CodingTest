'''
p.201 이진탐색_ 떡볶이 떡 만들기
<입력조건>
- 첫째 줄에 떡의 개수 n과 요청한 떡의 길이 m이 주어진다.
- 둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 m이상이므로, 손님은 필요한 양만큼 떡을 사갈 수 있다.
높이는 10억보다 작거나 같은 양의 정수 또는 0이다.
<출력조건>
- 적어도 m만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.
'''
def slice_cake(arr,height):
    result=0
    for i in arr:
        if(i-height >=0):
            result+=(i-height)
    return result


n,m= map(int,(input().split()))
length=list(map(int,input().split())) #떡의 개별 높이

start=0
end=max(length)
result=0
while(start<=end):
    mid= (start+end)//2
    if slice_cake(length,mid)==m:
        result=mid
        break
    elif slice_cake(length,mid)<=m:
         end=mid-1
    else:
        start= mid+1

print(result)