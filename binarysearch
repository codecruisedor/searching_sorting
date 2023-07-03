def binarySearch(arr,x,low,high):
    if len(arr) == 1 and arr[0] != x:
        return -1
    if len(arr) == 1 and arr[0] == x:
        return 0
    if high >= low:
        mid = low + (high - low)//2
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            return binarySearch(arr,x,mid+1,high)
        else:
            return binarySearch(arr,x,low,mid-1)
    else:
        return -1
    
arr = [1]
x = 1
res = binarySearch(arr,x,0,len(arr)-1)
if res!=-1:
    print("element present at index : " + str(res))
else:
    print("element not present..")
