n,m,k= map(int,input().split())
arr= list(map(int,input().split()))

arr.sort() #정렬하기 

max=arr[n-1]
sec_max=arr[n-2]


if m==k: 
    print(max*k)
else:
    x= m//(k+1) #(큰 수는 k번+ 두 번째 큰 수 1번) x번 반복해서 곱해준다
    y=m%(k+1) # x번 한 후 남은 수만큼 큰 수를 y번 더해준다
    result= x*(k*max+sec_max) + y*max
    print(result)
