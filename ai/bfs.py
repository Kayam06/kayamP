graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}
visited = [] #list to keep track of visited nodes.

queue=[] #Initialize queue

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        s =  queue.pop(0)
        print (s, end = "")
        for neighbour in graph[s] :
            if neighbour not in visited:
                visited.append(neighbour)   
                queue.append(neighbour) 
print("Following is the Path using Breadth-First Search")
bfs(visited, graph, "A")