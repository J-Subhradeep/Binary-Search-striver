arr = [4,5,6,4,4,4,4,4,4]
low = 0
high = len(arr)-1
ans = 9999999999
while(high>=low):

    mid= low+(high-low)//2
    ''' if the search space is already sorted'''
    if(arr[low]<=arr[high]):
        ans = arr[low]
        break
    
    ''' if the left half is sorted'''
    if(arr[low]==arr[mid]==arr[high]):
        low+=1
        high-=1
        continue
    elif(arr[low]<=arr[mid]):
        ans = min(ans,arr[low])
        low = mid+1
    else:
        '''if right half is sorted'''
        ans = min(ans,arr[mid])
        high = mid-1
print(ans)