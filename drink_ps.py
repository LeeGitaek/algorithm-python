''' n*m 크기의 얼음틀 , 구멍이 뚫려 있는 부분은 0 , 칸막이가 존재하는 부분 1 , 상하좌우로 붙어있는 경우
서로 연결 되어 있는 것으로 간주한다. 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림 개수 구하는
프로그램이다.'''

n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x,y):
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        #해당 노드 방문 처리
        graph[x][y] = 1
        # 상하좌우 의 위치도 모두 재귀적으로 호출
        dfs(x - 1,y)
        dfs(x, y-1)
        dfs(x + 1,y)
        dfs(x, y+1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result += 1

print(result)
