

array = [16, 17, 4, 3, 5, 2]

for i in range(0, len(array)):
    print(array[i])
    for j in range(i, len(array)):
        if array[j] > array[i]:
            break
        if j == len(array)-1:
            print(array[i])

# Question 1:

#     Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K = 5

# For the first 5 numbers(subarray from index 0-4), the average is: (1+3+2+6−1)/5 = >2.2
# The average of next 5 numbers(subarray from index 1-5) is: (3+2+6−1+4)/5 = >2.8
# For the next 5 numbers(subarray from index 2-6), the average is: (2+6−1+4+1)/5 = >2.4

# Output: [2.2, 2.8, 2.4, 3.6, 2.8]


# Question 2: Problem Statement

# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space
# after removing the duplicates in-place return the new length of the array.

# Example:

# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be[2, 3, 6, 9].


# Question 3:
# Write a custom decorator which print the function name the args and kwargs of the decorated function.

# Example:
# @your_function
# def dummy(a, b, c=10)


# pass


# Example:
# @your_function
# def say_hello(name)


# pass


# dummy(10, 12, c=30)


# Output
# dummy
# 10 12 30


# Question 4.
# Write a program to print all the LEADERS in the array.
# An element is leader if it is greater than all the elements to its right side. And the rightmost element is always a leader.
# For example int the array {16, 17, 4, 3, 5, 2}
# ,leaders are 17, 5 and 2.

# Let the input array be arr[] and size of the array be size.
