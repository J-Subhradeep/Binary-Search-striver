arr = [3,6,7,11]
h = 8
import math


def calculateTotalHour(arr,hourly):
    totalH = 0
    for i in arr:
        totalH += math.ceil(i/hourly)
    return totalH
def minEatingSpeed(piles,h):
    low = 1
    high = max(piles)
    ans = max(piles)
    while high>=low:
        mid = low+(high-low)//2
        if(calculateTotalHour(piles,mid)<=h):
            ans = min(ans,mid)
            high = mid-1
        else:
            low = mid+1
    return ans
print(minEatingSpeed(arr,8))