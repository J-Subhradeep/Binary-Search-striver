arr = [1,1,2,2,3,3,4,4,5,6,6]
def singleEl(arr,n):
    low = 1
    high = len(arr) - 2
    ''' because there is no left element in the 0 index and no element in the right of 1 element'''

    ''' if the size of arr is 1'''
    if len(arr)==1: return arr[0]

    ''' lets have a check for 0th and n-1th index if they are single element or not'''
    ''' for 0 th index 1th index should not be the same'''
    if(arr[0]!=arr[1]): return arr[0]
    '''for n-1th index n-2th index should not be the same'''
    if(arr[len(arr)-1]!=arr[len(arr)-2]): return arr[len(arr)-1]

    ''' now binary search in the search space 1 to n-2'''
    while high>=low:
        mid = low+(high-low)//2
        ''' check the left and right of the mid index if both are different it is the ans'''
        if(arr[mid-1]!=arr[mid] and arr[mid+1]!=arr[mid]): return arr[mid]
        ''' check if we are standing in the left half
        for left half if we stand at the even index we will check for the mid+1 or right element
        if it is equal then we will eliminate the left half

        if we are standing in the odd index we will check for the mid-1 or left element if 
        it is equal then we will eliminate the left half

        because both cases states (even,odd) position is same value which is condition for left half
        as u can see (0,1),(2,3),(4,5) are in the left half and (7,8),(9,10) are in the right half of the 
        single element
        
        '''

        '''checking for left half if we are in `even` or `odd` index'''
        if((mid%2==0) and (arr[mid]==arr[mid+1])) or ((mid%2!=0) and (arr[mid]==arr[mid-1])):
            low = mid+1
        else:
            high = mid-1
    return -1
print(singleEl(arr,len(arr)))