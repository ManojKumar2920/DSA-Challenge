def reverseString(string):
    reversed_string =""
    for i in string:
        reversed_string = i +reversed_string
    return reversed_string

if __name__ == "__main__":
    word = input()
    reversed_string = reverseString(word)
    print("Reversed_String:",reversed_string)
    
