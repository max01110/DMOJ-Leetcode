
#https://leetcode.com/problems/maximal-square/

matrix = [["1"]]
visited = []
val = []
areaT = 0
for i in range(len(matrix)):
    for y in range(len(matrix[i])):
        if matrix[i][y]=="1"and i<len(matrix) and y<len(matrix[i]):
            areaT = max(areaT, 1)
            a = [[i, y]]
            c = 0
            area = 1
            while a:
                cur = a.pop(0)

                if cur not in visited:
                    visited.append(
                if cur[0]<len(matrix)-1 and cur[1]<len(matrix[i])-1:
                    if matrix[cur[0]+1][cur[1]+1]=="1" and matrix[cur[0]+1][cur[1]] == "1" and matrix[cur[0]][cur[1]+1]=="1":
                        a.append([cur[0]+1, cur[1]+1])
                        a.append([cur[0], cur[1]+1])
                        a.append([cur[0]+1, cur[1]])
                    else:

                        areaT = max(areaT,area)

                        break
                else:
                    areaT = max(areaT,area)
                    break
                if c<=0:
                    c = len(a)
                    area += 1
                c-=1

print(areaT*areaT)
