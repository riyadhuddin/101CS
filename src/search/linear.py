
def linearSearch(array, n, x):
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1


arrayX = ['asha','bap','lal']
x = 'lal'
n = len(arrayX)
def linear_result():
    result = linearSearch(arrayX, n, x)
    if (result == -1):
        print("Element not found")
    else:
        print("Element found at index: ", result)