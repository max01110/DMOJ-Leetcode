nums = [1,0,-1,0,-2,2]

target = 0

#https://leetcode.com/problems/4sum/
book = {}
solutions = []
for num in nums:
    if num in book:
        book[num] += 1
    else:
        book.update({num:1})

for i in range(len(nums)):
    book[nums[i]] -= 1
    for j in range(i+1, len(nums)):
        book[nums[j]] -= 1
        for y in range(j+1,len(nums)):
            book[nums[y]] -= 1
            s = nums[i]+nums[j]+nums[y]
            t = target-s
            if t in book:
                if book[t] > 0 and sorted([nums[i],nums[j],nums[y],t]) not in solutions:
                    solutions.append(sorted([nums[i],nums[j],nums[y],t]))

            book[nums[y]] += 1
        book[nums[j]] += 1
    book[nums[i]] += 1
