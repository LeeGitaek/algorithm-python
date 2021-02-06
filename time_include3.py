# 시각 - 브루트 포스 ( 00시 00분 00초부터 n 시 59분 59초까지 3이 포함된 시각 경우의 수 출력

h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1


print(count)
