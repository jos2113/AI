def bfs(start,goal,adj,nodes):
    buffer=list()
    visited=list()
    trace={
        start:0
    }
    buffer.insert(0,start)
    while len(buffer)!=0:
        curr=buffer.pop()
        if curr==goal:
            break
        visited.append(curr)
        for i in range(len(nodes)):
            if adj[curr][i]==1 and nodes[i] not in visited and nodes[i] not in buffer:
                trace[nodes[i]]=curr
                buffer.insert(0,nodes[i])
    route=list()
    route.append(goal)
    print(f"The path from {start} to {goal} is : ",end="")
    while goal!=0:
        goal=trace[goal]
        if goal!=0:
            route.append(goal)
    print(*route[::-1])

def dfs(adj,nodes,start,goal):
    visited=list()
    trace={
        start:0
    }
    trace=recursive_traverse(start,adj,nodes,visited,trace,goal)
    route=list()
    route.append(goal)
    print(f"The path from {start} to {goal} is : ",end="")
    while goal!=0:
        goal=trace[goal]
        if goal!=0:
            route.append(goal)
    print(*route[::-1])

def recursive_traverse(curr,adj,nodes,visited,trace,goal):
    visited.append(curr)
    for i in range(len(nodes)):
        if adj[curr][i]==1 and nodes[i] not in visited:
            trace[nodes[i]]=curr
            if nodes[i]==goal:
                return trace
            return recursive_traverse(nodes[i],adj,nodes,visited,trace,goal)
        
nodes=list(map(str,input("Enter the nodes: ").split()))
adj=dict()
for node in nodes:
    adj[node]=list(map(int,input(f"Enter the connecting values for {node}: ").split()))
start=input("Enter the start node : ")
goal=input("Enter the goal node : ")

while True:  
    print("1. BFS")  
    print("2. DFS")  
    print("3. Exit")  
    choice1 = int(input("Enter the Choice:")) 

    if choice1 == 1:  
            bfs(start,goal,adj,nodes)  
              
    elif choice1 == 2:  
            dfs(adj,nodes,start,goal)  
    
    elif choice1 == 3:  
        break  
      
    else:  
        print("Oops! Incorrect Choice.")  



#Enter the nodes: S A B C D G
# Enter the connecting values for S: 0 1 1 1 0 0
# Enter the connecting values for A: 1 0 0 0 1 0
# Enter the connecting values for B: 1 0 0 0 1 1
# Enter the connecting values for C: 1 0 0 0 0 1
# Enter the connecting values for D: 0 1 1 0 0 1
# Enter the connecting values for G: 0 0 1 1 1 0
# Enter the start node : S
# Enter the goal node : G