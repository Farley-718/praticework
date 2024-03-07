''''''
# Complete the square sum function so that it squares each number passed into it and then sums the results together.

# For example, for [1, 2, 2] it should return 9 because 

''''''
def square_sum(numbers):
    # Initialize sum
    sum_squared = 0
    
    # Iterate through numbers in the list
    for num in numbers:
        # Square each number and add it to the sum
        sum_squared += num ** 2
    
    return sum_squared

# Test the function with example input
numbers = [1, 2, 2]
result = square_sum(numbers)
print("The square sum of", numbers, "is:", result)