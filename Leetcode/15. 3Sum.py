'''
nums = [-1,0,1,2,-1,-4]
l = []
t = True

for i in range(len(nums)):
    t = True
    for y in range(i+1, len(nums)):
        t = True
        for j in range(y+1, len(nums)):
            t = True;
           # print(nums[i],nums[y],nums[j])
            if nums[i]+nums[y]+nums[j]==0:
                for k in l:
                    a = k[:]
                    if nums[i] in a:
                        a.remove(nums[i])
                        if nums[y]in a:
                            a.remove(nums[y])
                            if nums[j] in a:
                                t = False
                if t==True:
                    l.append([nums[i], nums[y], nums[j]])


l  = []
for i in range(len(nums)):
    for y in range(i+1, len(nums)):
        a = nums[:]
        a.remove(nums[i])
        a.remove(nums[y])
        if (nums[i]+nums[y])*-1 in a:
            if sorted([nums[i], nums[y], (nums[i]+nums[y])*-1]) not in l:
                l.append(sorted([nums[i], nums[y], (nums[i]+nums[y])*-1]))
      

print(l)

'''


book,bob={},[]
for i in range(len(nums)):
    if nums[i] in book:
        b=book[nums[i]]+1
        book.update({nums[i]:b})
    else:
        book.update({nums[i]:1})

for a in range(len(nums)-1):
    try:
        we=book[nums[a]]-1
        book.update({nums[a]:we})
    except:
        None
    
    for b in range(a+1,len(nums)):
        try:
            ge=book[nums[b]]-1
            book.update({nums[b]:ge})xx
        except:
            None
        
        if (nums[a]+nums[b])*-1 in book:
            if book[(nums[a]+nums[b])*-1]>0:
                hen=sorted([nums[a],nums[b],((nums[a]+nums[b])*-1)])                       
                if hen not in bob:
                    bob.append(hen)
        try:
            ge=book[nums[b]]+1
            book.update({nums[b]:ge})
        except:
            None
            
    try:
        we=book[nums[a]]+1
        book.update({nums[a]:we})
    except:
        None
        
return(bob)



