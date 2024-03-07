# ''''''
# # Complete the square sum function so that it squares each number passed into it and then sums the results together.

# # For example, for [1, 2, 2] it should return 9 because 

# ''''''
# # def square_sum(numbers):
# #     # Initialize sum
# #     sum_squared = 0
    
# #     # Iterate through numbers in the list
# #     for num in numbers:
# #         # Square each number and add it to the sum
# #         sum_squared += num ** 2
    
# #     return sum_squared

# # # Test the function with example input
# # numbers = [1, 2, 2]
# # result = square_sum(numbers)
# # print("The square sum of", numbers, "is:", result)
# ''''''
# # Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.

# # Examples (input -> output)
# # def repeat_string(n, s):

# def repeat_string(n, s):
#     """
#     Function to repeat a string exactly n times.
    
#     Parameters:
#         n (int): Number of times to repeat the string.
#         s (str): String to be repeated.
    
#     Returns:
#         str: String s repeated exactly n times.
#     """
#     return s * n

# # Test the function with examples
# # print(repeat_string(3, "hello"))  # Output: "hellohellohello"
# # print(repeat_string(5, "world"))  # Output: "worldworldworldworldworld"

# ''''''''
# # Johnny is working as an intern for a publishing company, and was tasked with cleaning up old code. He is working on a program that determines how many digits are in all of the page numbers in a book with pages from 1 to n (inclusive).

# # For example, a book with 4 pages has 4 digits (one for each page), while a 12 page book has 15 (9 for 1-9, plus 2 each for 10, 11, 12).

# # Johnny's boss, looking to futureproof, demanded that the new program be able to handle books up to 400,000,000,000,000,000 pages.

# ''''''
# def count_digits(n):
#     """
#     # Function to count the total number of digits in all page numbers from 1 to n.
    
#     # Parameters:
#     #     n (int): The number of pages in the book.
    
#     # Returns:
#     #     int: The total number of digits in all page numbers.
#     # """
#     # total_digits = 0
    
#     # # Iterate through each page number from 1 to n
#     # for i in range(1, n + 1):
#     #     total_digits += len(str(i))  # Count the number of digits in the page number
    
#     # return total_digits

# # Test the function with a large number of pages
# n = 400000000000000000
# total_digits = count_digits(n)
# print("Total number of digits in all page numbers from 1 to", n, "is:", total_digits)
# # Set system username and password
# sys_username = 'admin'
# sys_password = 'password'

# # Initialize attempts counter
# attempts = 0

# # Loop for multiple attempts
# while True:
#     # Prompt the user to enter their username and password
#     user_username = input("Enter your username: ")
#     user_password = input("Enter your password: ")
    
#     # Check if username and password match
#     if user_username == sys_username and user_password == sys_password:
#         print("Login successful")
#         break  # Exit the loop if login successful
#     else:
#         print("Incorrect username or password")
#         attempts += 1
#         if attempts >= 3:
#             print("You have exceeded the maximum number of attempts.")
#             break  # Exit the loop if maximum attempts reach
''''''''

print(1*3)
print(3*8)