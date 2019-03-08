import sys

def BuyLowSellHi(S):
    n = len(S)
    maxProfit = -sys.maxsize
    buy = -1
    sell = -1
    for i in range(n):
        for j in range(i, n):
            profit = S[j] - S[i]
            if(profit > maxProfit):
                maxProfit = profit
                buy = i
                sell = j
    
    return (buy, sell)

def argmin(S, i, j):
    if(S[i]<S[j]):
        return i
    else:
        return j

def argmax(S, i, j):
    if(S[i]>S[j]):
        return i
    else:
        return j

def BlSh(S, start, end):
    n = end - start
    if n == 0:
        return (0, start, start, start, start)
    else:
        profitL, buyL, sellL, minL, maxL = BlSh(S, start, start + int(n/2))
        profitR, buyR, sellR, minR, maxR = BlSh(S, start + int(n/2)+1, end)
        
        amin = argmin(S, minL, minR)
        amax = argmax(S, maxL, maxR)
        profit = S[maxR] - S[minL]

        if(profit > profitL and profit > profitR):
            return (profit, minL, maxR, amin, amax)
        elif(profitL > profit and profitL > profitR):
            return (profitL, buyL, sellL, amin, amax)
        else:
            return (profitR, buyR, sellR, amin, amax)

S = [5,10,3,4,9,21,13,1,12,20,15,17,4]
# (buy, sell) = BuyLowSellHi(S)
(profit, buy, sell, amin, amax) = BlSh(S, 1, len(S)-1)
print("Buy {} on {}, Sell {} on {}, to win {}".format(S[buy], buy+1, S[sell], sell+1, S[sell]-S[buy]))