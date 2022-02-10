'''
p.180 정렬_ 성적이 낮은 순서로 학생 출력하기
<입력조건>
- 첫 번째 줄에 학생의 수 N이 입력된다.
- 두 번째 줄부터 N+1번째 줄에는 학생의 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가 공백으로 구분되어 입력된다.
문자열 A의 길이와 학생의 성적은 100이하의 자연수이다.

<출력조건>
- 모든 학생의 이름을 성적이 낮은 순서대로 출력한다. 성적이 동일한 학생들의 순서는 자유롭게 출력해도 괜찮다.
'''
n= int(input())
arr=[]

for i in range(n):
    data= input().split()
    arr.append((data[0], int(data[1])))

arr= sorted(arr, key= lambda student: student[1])
#lambda 매개변수: 표현식 
for student in arr:
    print(student[0],end=' ')
    
