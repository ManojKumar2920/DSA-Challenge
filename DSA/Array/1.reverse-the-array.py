def reverseArray(arr, first, last):
    # Write your code here.
    while(first<last):
        arr[first],arr[last] = arr[last],arr[first]
        first +=1
        last-= 1
    pass

if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    reverseArray(arr,0,5)

    print("Reversed_array: ",arr)