initial = list(map(int, input().split(" ")))
final = list(map(int, input().split(" ")))


def children(pos):
    moves = []
    move1 = pos
    move1[0] += 2
    move1[1] += 1
    if move1[0] <= 8 and move1[1] <=8 and move1[0]>=1 and move1[1]>=1:
        moves.append(move1[:])
        
    move1[0] -= 2
    move1[1] -= 1
    move1[0] += 1
    move1[1] += 2
    if move1[0] <= 8 and move1[1] <=8 and move1[0]>=1 and move1[1]>=1:
        moves.append(move1[:])
    move1 = pos
    move1[0] -= 1
    move1[1] -= 2
    move1[0] += 2
    move1[1] -= 1

 
    if move1[0] <= 8 and move1[1] <=8 and move1[0]>=1 and move1[1]>=1:
        moves.append(move1[:])
    move1 = pos
   
    move1[0] -= 2
    move1[1] += 1
    move1[0] += 1
    move1[1] -= 2
    
    if move1[0] <= 8 and move1[1] <=8 and move1[0]>=1 and move1[1]>=1:
        moves.append(move1[:])
    move1 = pos
    move1[0] -= 1
    move1[1] += 2
    move1[0] -= 1
    move1[1] -= 2
    
    if move1[0] <= 8 and move1[1] <=8 and move1[0]>=1 and move1[1]>=1:
        moves.append(move1[:])
    move1 = pos
    move1[0] += 1
    move1[1] += 2
    move1[0] -= 2
    move1[1] -= 1
 
    if move1[0] <= 8 and move1[1] <=8 and move1[0]>=1 and move1[1]>=1:
        moves.append(move1[:])
    move1[0] += 2
    move1[1] += 1
    move1[0] -= 2
    move1[1] += 1
    

    if move1[0] <= 8 and move1[1] <=8 and move1[0]>=1 and move1[1]>=1:
        moves.append(move1[:])
    move1[0] += 2
    move1[1] -= 1
    move1[0] -= 1
    move1[1] += 2
    if move1[0] <= 8 and move1[1] <=8 and move1[0]>=1 and move1[1]>=1:
        moves.append(move1[:])
    return moves

q = [initial]
visited = []
rounds = []
steps=1
last = initial[:]
dont = False


count = 0
step = -1
if initial==final:
    
    print(0)
    dont = True
while q:
    if count==0:
       count = len(q)
       step+=1 
    count -=1
    pos = q[0]
    q.pop(0)
   
    if pos==final:
        if dont==False:  
           print(step)
        break
    else:
        
        if pos not in visited:
            add = children(pos)
            q = q + add
            visited.append(pos)
    

