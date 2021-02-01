# n 이 1이 될 때까지 , n - 1과 n/k 두 과정 중 하나를 반복적으로 수행한다. n/k 는 n이 k로 나누어 떨어질 때만 선택 / 1이 될때까지 최소횟수를 구하라
n,k = map(int,input().split())
result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)
