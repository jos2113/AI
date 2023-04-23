#BFS

#graph generation

numNodes = int(input("Enter the no. of nodes :"))
graphs = {}

for i in range(numNodes):
    node = input("enter the node :")
    values = input("enter the adj nodes :")
    graphs[node] = values.split(' ')[::-1]
    
# print(graphs)


#array to track

start = input("Start Node : ") 
end = input("Final Node : ")

visited = [list(graphs.keys())[0]]
stack = [start]


#implementation iterative
while len(stack):
    print("-> ",end='')
    print(stack[0],end= ' ')
    if stack[0] not in visited:
        visited.append(stack[0])
    poppedItem = stack.pop(0)
    for item in graphs[poppedItem]:
        #print(item,'x')
        if item not in visited :
            stack.append(item)
            visited.append(item)


