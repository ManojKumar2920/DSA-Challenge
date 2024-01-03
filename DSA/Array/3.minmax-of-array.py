def minmax(arr):
    min_val = arr[0]
    max_val = arr[-1]
    for num in arr:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    return min_val, max_val
if __name__ == "__main__":
    arr = [3,4,5,7,6,1,2]
    min_val, max_val = minmax(arr)
    print("Mininum of array: ",min_val)
    print("Maximum of array: ",max_val)
