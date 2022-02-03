n,m,k= map(int,input().split())
arr= list(map(int,input().split()))

arr.sort() #정렬하기 

max=arr[n-1]
sec_max=arr[n-2]


if m==k: 
    print(max*k)
else:
    x= m//(k+1) #큰 수는 k번 반
    y=m%(k+1)
    result=(k*max+sec_max)*x+y*max
    print(result)
