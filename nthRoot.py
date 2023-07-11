n = 1953125
r = 9
low = 1
high = n
ans = 1
while high>=low:
    mid = low+(high-low)//2

    if mid**r <= n:
        ans = max(ans,mid)
        low = mid+1
    else:
        high = mid-1
print(ans)