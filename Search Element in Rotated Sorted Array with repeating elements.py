arr = [4,5,6,4,4,4,4,4,4,4]
low  = 0
high = len(arr)-1
target = 4
while(high>=low):
    mid = low + (high-low)//2
    if(arr[mid]==target):print(arr[mid])

    if(arr[mid]==arr[high]==arr[low]):
        low = low+1
        high = high-1
        continue
    
    ''' check if the left half is sorted '''
    if(arr[low]<=arr[mid]):
        ''' check if target exists in the left half'''
        if(arr[low]<=target and arr[mid]>=target):
            ''' eliminate the right half '''
            high = mid-1
        else:
            ''' eliminate the left half'''
            low = mid+1
    else:
        ''' when right half is sorted'''
        ''' check if target exists in the right half'''
        if(arr[high]>=target and target>=arr[mid]):
            low = mid+1
        else:
            high = mid -1

