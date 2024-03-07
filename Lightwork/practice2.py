'''''Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.'''''''''
def calculate_average(nums):
    """
    Function to calculate the average of numbers in a given list.
    
    Parameters:
        nums (list): List of numbers.
    
    Returns:
        float: Average of the numbers in the list. Returns 0 if the list is empty.
    """
    # Check if the list is empty
    if not nums:
        return 0
    
    # Calculate the sum of numbers in the list
    total = sum(nums)
    
    # Calculate the average
    average = total / len(nums)
    
    return average

# Test the function with examples
print(calculate_average([1, 2, 3, 4, 5]))  # Output: 3.0
print(calculate_average([]))              # Output: 0