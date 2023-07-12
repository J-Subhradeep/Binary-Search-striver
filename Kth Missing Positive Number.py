arr = [2,3,4,7,11,12]
k = 5

low = 0
high = len(arr)-1
while high>=low:
    mid = low+(high-low)//2

    if (arr[mid]-(mid+1)<k):
        low = mid+1
    else:
        high = mid-1
'''
missing  = arr[high] - (high+1)
ans = arr[high] + how more
ans = arr[high] + (k-missing)
ans = arr[high] + (k - arr[high] + (high+1))
ans = k+high+1
'''
ans = k+high+1
print(low,high)
print(ans)