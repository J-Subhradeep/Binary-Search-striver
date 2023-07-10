arr = [3,4,5,1,2]
low = 0
high  = len(arr)-1

ans = 9999999999
while high>=low:
    mid = low + (high-low)//2
    
    '''if the search space is already sorted then the ans is arr[low]'''
    if(arr[low]<=arr[high]):
        ans = min(ans,arr[low])
        break

    ''' if left half is sorted '''

    if(arr[mid]>=arr[low]):
        ''' take the smallest element '''
        ans = min(ans,arr[low])
        ''' eliminate the left half'''
        low  = mid+1
    else:
        ''' if the right half is sorted'''
        ans = min(ans,arr[mid])
        high = mid-1
print(ans)