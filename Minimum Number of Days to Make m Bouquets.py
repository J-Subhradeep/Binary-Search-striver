bloomDay = [7,7,7,7,13,11,12,7]
m = 2 # number of bouquets
k = 3 # number of adjacent flowers

def possibleToMakeBouquets(arr,day,m,k):
    
    count = 0
    no_of_bouquets = 0
    for i in arr:
        if i<=day:
            count+=1
        else:
            no_of_bouquets += count//k
            count = 0
    no_of_bouquets += count//k
    if no_of_bouquets>=m: return True
    return False

def minDays(arr,m,k):
    if m*k>len(arr):return -1
    low = min(arr)
    high = max(arr)
    ans = high
    while high>=low:
        mid = low+(high-low)//2   
        if(possibleToMakeBouquets(arr,mid,m,k)):
            ans = mid
            high = mid-1    
        else: low= mid+1
    return ans
