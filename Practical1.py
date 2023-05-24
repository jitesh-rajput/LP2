graph = {
 '5' : ['3','7'],
 '3' : ['2', '4'],
 '7' : ['8'],
 '2' : [],
 '4' : ['8'],
 '8' : []
}

def bfs(graph,node):
    visited = [] # List for visited nodes.
    queue = [] #Initialize a queue
    visited.append(node)
    queue.append(node)
    while queue:
        temp=queue.pop(0)
        print(temp,end=" ")
        for n in graph[temp]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

visited=set()

def dfs(graph,visited,node):
    if node not in visited:
        print(node,end=" ")
        for n in graph[node]:
            dfs(graph,visited,n)

bfs(graph,'5')
print()
dfs(graph,visited,'5')

