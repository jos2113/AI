rooms=[str(i) for i in range(1, int(input("Enter number of rooms: "))+1)]
status=dict()
for r in rooms:
  status[r]=None
for i in range(len(rooms)):
  status[rooms[i]]=input(f"Enter the status of room {rooms[i]} [C/D]:")
vc=int(input("Enter the position of vaccum cleaner: "))
inx=vc-1
cost=0
while "D" in list(set(status.values())):
  if status[rooms[inx]]=="D":
    status[rooms[inx]]="C"
    cost+=1
  if len(list(set(status.values())))==1:
    break
  if inx==len(rooms)-1:
    inx=0
  else:
    inx+=1
  cost+=1
print(f"The cost for cleaning all rooms is {cost}")

