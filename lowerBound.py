li  = [1,2,22,23,45,46,78,90]
''' lower bound means the smallest number in the array which is >= target'''
target = 24
lowerBound = len(li)
low = 0
high = len(li) -1
while(high>=low):
    mid = low + (high-low)//2
    if li[mid] >= target:
        lowerBound = mid
        high = mid -1
    else:
        low = mid+1
print(lowerBound)
