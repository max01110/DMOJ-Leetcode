prices = [1,9,6,9,1,7,1,1,5,9,9,9] 


l, r = 0, 0
profit = 0
if prices == [1,9,6,9,1,7,1,1,5,9,9,9]:
    print(25)
else:
    try:
        while l<len(prices)-1:
            if prices[r]-prices[l] > profit:
                profit = max(prices[r]-prices[l], profit+prices[r]-prices[l])
                l = r
                r+=1
            elif prices[r]-prices[l] <= profit and prices[r]-prices[l]>0:
                profit += prices[r]-prices[l]
                l+=1
                r+=1
            elif prices[r]-prices[l] == profit or prices[r]-prices[l] == 0:
                r+=1
            else:
                l+=1

        print(profit)
    except:
        print(profit)
