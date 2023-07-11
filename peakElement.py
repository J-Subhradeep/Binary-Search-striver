arr =  [ 1,2,3,9,4,3,3,3,3,2,2]
def peak(arr):
    low = 1
    high = len(arr)-2
    if(len(arr)==1): return arr[0]
    ''' search space is from 1 to n-2 '''
    '''manual check for 0 and n-1 indexes '''

    if(arr[0]>arr[1]): return arr[0]
    if(arr[len(arr)-1]>arr[len(arr)-2]): return arr[len(arr)-1]


    '''binary search'''
    while high>=low:
        '''take mid'''
        mid = low+(high-low)//2
        print(mid)
        '''check for mid-1 and mid-2 if both are smaller than mid it is the answer'''
        if(arr[mid-1]<=arr[mid] and arr[mid+1]<arr[mid]):
            return mid
        if(arr[mid]>arr[mid-1]):
            ''' then it is in the left half now we eliminate the left half'''
            low = mid+1
        else:
            ''' then it in in the right half now we eliminate the right half'''
            high = mid-1
    
    return -1
print(peak(arr))