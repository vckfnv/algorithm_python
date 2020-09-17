def binary_search(values, target):
    length = len(values)
    mid = len(values)//2
    while mid >0:
        if values[mid] == target:
            return mid
        else:
            if values[mid]<target:
                mid = (mid + length)//2
                
            else:
                mid = mid//2
                
def main(): 
    li = [ 2, 3, 10, 50, 70 ] 
    x = 70
    result = binary_search(li, x)
    print("value", x, "is at index", result)
    
main()
