arr = [7,8,9,1,2,3,4,5,6]
low = 0
high = len(arr)-1
target = 2
while(high>=low):
    mid = low + (high-low)//2
    if(arr[mid]==target): print("Element found at ",mid)
    ''' if the left half is sorted '''
    if(arr[mid]>=arr[low]):
        ''' check if target exist in the left half '''
        if(arr[low]<=target and arr[mid]>=target):
            ''' if true then eliminate the right half '''
            high = mid -1
        else:
            low = mid + 1
    else:
        ''' if the right half is sorted '''
        ''' check if target exist in the right half '''
        if(arr[high]>=target and arr[mid]<=target):
            ''' if true then eliminate the left half '''
            low = mid+1
        else:
            high = mid-1
