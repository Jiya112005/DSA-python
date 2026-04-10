"""
    MONOTONIC ARRAY:
    can be monotonic increasing : example:[1,2,3] ; [1,2,3,3] ; [1,2,4] ; [1,5,7]  All this are the example of monotonic increasing. output:True 
    can be monotonic decreasing : example: [3,2,1] ; [3,2,1,1] ; [4,2,1] ; [8,6,3] All this are example of monotonic decreasing array. output:True
    
    we just have to check that whether the given array is monotonic or not !
        Test cases:
            I/P          O/P
            [1,2,3]         True
            [3,2,1]         True
            [1,2,2]         True
            [3,3,3]         True
            [7]             True
            []              True (in the given question or ask the interviewer for clarification is empty array considered in monotonic or not?)

"""
def take_input():
    n = int(input("Enter the number of elements in array: "))
    arr = input("Enter the array elements separated by commas: ")
    if not arr:
        return []
    array = [int(x.strip()) for x in arr.split(",") if x.strip()]
    if len(array) != n:
        print("Error:not according to elements")
        return 0   
    return n,array

def is_monotonic(n,array):
    first = array[0]
    last = array[n-1]
    res = True 
    if first > last :  
        for i in range(n-1):
            if array[i] < array[i+1]: res=False   # checks if it is non-decreasing
    elif first == last :
        for i in range(n-1):
            if array[i] != array[i+1]: res=False  # checks if it is equal elements
    else:
        for i in range(n-1):
            if array[i] > array[i+1]: res =False  # checks if it is non-increasing 
    return res

inputs = take_input()
n = inputs[0]
array = inputs[1]
if n == 0:
    print(True)
else:
    print(is_monotonic(n,array))
