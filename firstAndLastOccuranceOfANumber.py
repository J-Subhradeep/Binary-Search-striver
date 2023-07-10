arr = [1,2,22,23,45,45,46,78,90]

def lowerBound(arr,target):
    low = 0
    high = len(arr) - 1
    ans = len(arr)
    while high >= low:
        mid = low + (high - low)//2
        if arr[mid]>=target:
            ans = mid
            high = mid -1
        else:
            low = mid+1
    return ans
def upperBound(arr,target):
    low = 0
    high = len(arr) - 1
    ans = len(arr)
    while high >= low:
        mid = low + (high - low)//2
        if arr[mid]>target:
            ans = mid
            high = mid -1
        else:
            low = mid+1
    return ans    

ans = [-1,-1]
x = 90
if lowerBound(arr,x)>=len(arr) or arr[lowerBound(arr,x)]!=x:
    print(ans)
else:
    ans = [lowerBound(arr,x),upperBound(arr,x)-1]
    print(ans)



'approach 2'
'simple binary search without lower and upper bound'

