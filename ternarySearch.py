#A variant of binary search, bit faster
import math as mt
def ternarySearch(arr,start,end,key):
    if (end>=start):
        mid1 = start + (end-start) //3
        mid2 = end  -  (end-start) //3
        
        if (key == arr[mid1]):
            return mid1
        if (key == arr[mid2]):
            return mid2
            
        if (key > arr[mid1] and key < arr[mid2]):
            return ternarySearch(arr, mid1+1,mid2-1,key)
        elif (key < arr[mid1]):
            return ternarySearch(arr,start,mid1-1,key)
        else:
            return ternarySearch(arr,mid2+1,end,key)
    return -1
    
exarray = [1,3,46,222,422,32322]
s = 0
e = len(exarray) - 1
k = 46
res = ternarySearch(exarray,s,e,k)
print ("Key found at index : ",res)
