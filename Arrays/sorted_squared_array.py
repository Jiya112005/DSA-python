# input 
def take_input():
    n = int(input("Enter the number of elements in array: "))
    arr = input("Enter the array elements separated by commas: ")
    if not arr:
        return []
    array = [int(x.strip()) for x in arr.split(",") if x.strip()]    
    return n,array

def sorted_squared_array(n:int,arr: list):
    i,j=0,n-1
    res = [0]*n
    for k in reversed(range(n)):
        leftsquare = arr[i]**2
        rightsquare = arr[j]**2
        if leftsquare > rightsquare:
            res[k] = leftsquare
            i+=1
        else:
            res[k] = rightsquare
            j-=1
    return res


inputs = take_input()
n = inputs[0]
array = sorted(inputs[1])
print("Input sorted array: ",array)
print("Sorted_squared_array: ",sorted_squared_array(n,array))