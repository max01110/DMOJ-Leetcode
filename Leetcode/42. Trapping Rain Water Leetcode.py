height = [0,1,0,2,1,0,1,3,2,1,2,1]
# https://leetcode.com/problems/trapping-rain-water/
def checkWater(i):
    maxL = 0
    maxR = 0
    for y in range(i, -1, -1):
        if height[y] > maxL:
            maxL = height[y]
    for o in range(i+1, len(height)):
        if height[o] > maxR:
            maxR = height[o]

    w = min(maxL, maxR)
    w = w-height[i]
    return w

totalWater = 0
for m in range(len(height)):
    wat = checkWater(m)
    print(
    if wat != None and wat > 0:
        totalWater+= wat

print(totalWater)
