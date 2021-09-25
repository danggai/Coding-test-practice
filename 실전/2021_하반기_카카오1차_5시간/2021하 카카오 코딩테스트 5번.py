import copy

sheeps = 0
visited_sheeps = []

def solution(info, edges):
    answer = 0

    while(1):
        visited_old = copy.deepcopy(visited_sheeps)
        bfs(info, edges, [], 0, 0)

        if visited_old == visited_sheeps: break


    return answer

def bfs(info, edges, visited, now, wolves):
    global visited_sheeps
    global sheeps

    if sheeps <= wolves:
        return

    if now not in visited and now == 0:
        sheeps += 1
        visited.append(now)

    print(sheeps)
    
    for edge in edges:
        if edge[0] == now:
            if info[edge[1]] == 0:
                bfs(info, edges, edge[1], wolves)
            elif info[edge[1]] == 1 and edge[1] not in visited:
                bfs(info, edges, edge[1], wolves+1)
    




info = [0,0,1,1,1,0,1,0,1,0,1,1]	
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]	
print(solution(info, edges))
print("expect = 5")

info = [0,1,0,1,1,0,1,0,0,1,0]		
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]	
print(solution(info, edges))
print("expect = 5")