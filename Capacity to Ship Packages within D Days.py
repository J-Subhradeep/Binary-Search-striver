weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

def requiredDays(weights,capacity):
    res= 1
    weight = 0
    for i in weights:
        weight+=i
        if weight>capacity:
            res+=1
            weight=i
    return res

class Solution:
    def shipWithinDays(self, weights, days: int) -> int:
        low = max(weights)
        high = sum(weights)
        ans = high

        while high>=low:
            mid = low+(high-low)//2

            if(requiredDays(weights,mid)<=days):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
print(Solution().shipWithinDays(weights,days))