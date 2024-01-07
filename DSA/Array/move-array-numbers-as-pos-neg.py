n = int(input("Enter the size of the array: "))
arr = [int(input("Enter element: ")) for i in range(n)]
print("The array is:", arr)

def move(arr):
    positive_arr = []
    negative_arr = []

    for num in arr:
        if num >= 0:
            positive_arr.append(num)
        elif num < 0:
            negative_arr.append(num)

    custom_arr = positive_arr + negative_arr
    return custom_arr

result_arr = move(arr)
print(result_arr)