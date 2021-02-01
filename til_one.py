# n 이 1이 될 때까지 , n - 1과 n/k 두 과정 중 하나를 반복적으로 수행한다. n/k 는 n이 k로 나누어 떨어질 때만 선택 / 1이 될때까지 최소횟수를 구하라
n,k = map(int,input().split())
result = 0

while True:
    target = ( n // k ) * k
    result += (n-target)
    n = target

    if n<k:
        break

    result += 1
    n //= k

result += (n-1)
print(result)
