def binaryRecursiveSearch(arr,item,low,high):
    if high>=low:
        mid = low+ (high-low)//2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            return binaryRecursiveSearch(arr,item,low,mid-1)
        else:
            return binaryRecursiveSearch(arr,item,mid+1,high)
    else:
        return -1

arrayX = ['asha','bap','lal','oppa']
x = 'lal'
n = len(arrayX)-1
def binaryRecursive_result():
    result = binaryRecursiveSearch(arrayX, x, 0, n)
    if (result != -1):
        print("Element found at index: ", result)
    else:
        print('Not found')

