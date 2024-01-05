def k_small_of_array(arr,k):
    arr.sort()
    return arr[k - 1]
    
if __name__ == "__main__":
    arr = [2,5,4,1,3,6]
    k = 3
    k_small = k_small_of_array(arr,k)
    print("Kth Small element is:",k_small)