#https://leetcode.com/problems/4sum/

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



