# 이진 탐색 (재귀 )

def binary_search(array,target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2

    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target, mid+1 , end)

# n과 target 을 입력받기
n, target = list(map(int,input().split()))
# 전체 원소 입력받기
array = list(map(int,input().split()))

# 이진 탐색 수행 결과 찾기
result = binary_search(array, target, 0, n-1)

if result == None:
    print("원소 존재하지 않음")
else:
    print(result+1)

'''

10 7
1 3 5 7 9 11 13 15 17 19
4

'''
