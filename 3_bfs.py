graph = {
  'A' : ['B','D'],
  'B' : ['A', 'C'],
  'C' : ['B'],
  'D' : ['A','E','F'],
  'E' : ['D','F','G'],
  'F' : ['D','E','H'],
  'G' : ['E','H'],
  'H' :['G','F']
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
    
        print (s, end = " ") 

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Driver Code
print("Traversal using BFS:")
bfs(visited, graph, 'A')