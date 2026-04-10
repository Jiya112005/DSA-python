""" 
    I have given array in prices where prices[i] is the price of the given stock on the ith day.
    Input: 
        prices = [7,1,5,3,6,4]
    Expected output:
        Output=5
    You have to select a single day to buy one stock and choosing a different day to sell that stock 
    means selecting the max profit.
    let's see 
    you will not buy when price is 7
    you will buy when price is lowest = 1
    and when you calculated profit ast each day 
    storing the previous profits to compare 
    day     profit    prev. profit   selected profit is max(prev,profit)
    day 1 = 1-1 = 0       0                   0
    day 2 = 5-1 = 4       0                   4
    day 3 = 3-1 = 2       4                   4 (max of (2,4) = 4)
    day 4 = 6-1 = 5       4                   5 (max of (5,4) = 5)
    day 5 = 4-1 = 3       5                   5 (max of (3,5) = 5) 
    
    Hence, the max profit to be achieved is 5 
    Brute force approach: take a i to number of elements and subtracting i from another element j which also iterate from i+1 to n 
    and compare prices at each step.
    
    Taking the above mentioned table approach.
"""
def take_input():
    arr = input("Enter the array elements separated by commas: ")
    if not arr:
        return []
    array = [float(x.strip()) for x in arr.split(",") if x.strip()]
    n = len(array)    
    return n,array

def buy_sell_stock(array):
    min_price = float('inf')
    max_profit = 0
    for price in array:
        if price < min_price:  # it compares first element with +infinity and then temper the min_price to find the minimum going from left to right 
            min_price = price 
        else:
            profit = price - min_price   # calculates profit at each iteration
            if profit > max_profit:    # compare it with previous profit 
                max_profit = profit  # set the max profit here 
    return max_profit

inputs = take_input()
# n = inputs[0]
array = inputs[1]
print(f"The maximum profit to be attained is: {buy_sell_stock(array)} ")