def floor(arr,start,end,target):
    '''
    floor means the largest number in the search space of array <= target
    '''
    low = start
    high = end - 1
    ans = arr[high]
    while(high>=low):
        mid = low + (high - low)//2
        if(arr[mid]<=target):
            ans = arr[mid]
            low = mid+1
        else:
            high = mid -1
    return ans

def ceil(arr,start,end,target):
    '''
    smallest number in the search space of array >= target
    '''
    low= start

    high = end - 1
    ans = arr[low]
    while(high>=low):
        mid = low + (high - low)//2
        if(arr[mid]>=target):
            ans = arr[mid]
            high = mid-1
        else:
            low = mid+1
    return ans

arr = [1,2,22,23,45,46,78,90]
print(floor(arr,0,len(arr),23))
print(ceil(arr,0,len(arr),23))
