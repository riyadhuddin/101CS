def binaryIterativeSearch(arr,item,low,high):
    while low<=high:
        mid = low + (high-low)//2
        if arr[mid]== item:
            return mid
        elif arr[mid] < item:
            low = mid+1
        else:
            high = mid-1
    return -1

arrayX = ['asha','bap','lal']
x = 'lal'
n = len(arrayX)-1
def binaryIterative_result():
    result = binaryIterativeSearch(arrayX, x, 0, n)
    if (result == -1):
        print("Element not found")
    else:
        print("Element found at index: ", result)

