
# 순차 탐색

def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일할 경우
        if array[i] == target:
            # 현재의 위치를 반환한다. 인덱스는 0 부터 시작하기 때문에 1을 더함
            return i+1


print("생성할 원소 개수르 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요")

input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력 하세요. 구분은 띄어쓰기 한 칸으로 합니다. ")
array = input().split()
print(sequential_search(n, target, array))


'''
입출력 :

생성할 원소 개수르 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요
5 Dongbin
앞서 적은 원소 개수만큼 문자열을 입력 하세요. 구분은 띄어쓰기 한 칸으로 합니다.
Hanul Jonggu Dongbin Taeil Sangwook
3
'''
