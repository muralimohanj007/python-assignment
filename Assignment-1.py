#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 1. Write a Python program to reverse a string without using any built-in string reversal functions.

def reverse_string(string):
    reversed_string = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
    return reversed_string


input_string = input("Enter a string: ")
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)


# In[3]:


# 2. Implement a function to check if a given string is a palindrome.

def is_palindrome(string):
    # Remove whitespace and convert to lowercase
    string = string.replace(" ", "").lower()

    # Check if the string is equal to its reverse
    if string == string[::-1]:
        return True
    else:
        return False


input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# In[4]:


# 3. Write a program to find the largest element in a given list.

def find_largest_element(lst):
    if len(lst) == 0:
        print("Error: List is empty.")
        return None

    largest = lst[0]  # Assume the first element is the largest

    for i in range(1, len(lst)):
        if lst[i] > largest:
            largest = lst[i]

    return largest


input_list = input("Enter a list of numbers (space-separated): ")
input_list = input_list.split()  # Split the input string into a list of numbers
input_list = [int(num) for num in input_list]  # Convert each element to an integer

largest_element = find_largest_element(input_list)
print("Largest element:", largest_element)


# In[5]:


# 4. Implement a function to count the occurrence of each element in a list.
def count_occurrences(lst):
    occurrence_count = {}

    for element in lst:
        if element in occurrence_count:
            occurrence_count[element] += 1
        else:
            occurrence_count[element] = 1

    return occurrence_count


input_list = input("Enter a list of elements (space-separated): ")
input_list = input_list.split()  # Split the input string into a list

occurrence_count = count_occurrences(input_list)
print("Occurrence count:", occurrence_count)


# In[6]:


# 6. Implement a function to remove duplicate elements from a list.
def remove_duplicates(lst):
    unique_list = []

    for element in lst:
        if element not in unique_list:
            unique_list.append(element)

    return unique_list


input_list = input("Enter a list of elements (space-separated): ")
input_list = input_list.split()  # Split the input string into a list

unique_list = remove_duplicates(input_list)
print("List with duplicates removed:", unique_list)


# In[7]:


# 7. Write a program to calculate the factorial of a given number.
def factorial(n):
    if n < 0:
        print("Error: Factorial is not defined for negative numbers.")
        return None

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


input_num = int(input("Enter a number: "))

fact = factorial(input_num)
if fact is not None:
    print("Factorial of", input_num, "is", fact)


# In[10]:


#8. Implement a function to check if a given number is prime.
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


input_num = int(input("Enter a number: "))

if is_prime(input_num):
    print(input_num, "is a prime number.")
else:
    print(input_num, "is not a prime number.")


# In[11]:


# 9. Write a Python program to sort a list of integers in ascending order.
def sort_list_ascending(lst):
    lst.sort()
    return lst


input_list = input("Enter a list of integers (space-separated): ")
input_list = input_list.split()  # Split the input string into a list of strings
input_list = [int(num) for num in input_list]  # Convert each element to an integer

sorted_list = sort_list_ascending(input_list)
print("Sorted list in ascending order:", sorted_list)


# In[12]:


# 10. Implement a function to find the sum of all numbers in a list.
def find_sum(lst):
    total = 0

    for num in lst:
        total += num

    return total

# Test the function
input_list = input("Enter a list of numbers (space-separated): ")
input_list = input_list.split()  # Split the input string into a list of strings
input_list = [int(num) for num in input_list]  # Convert each element to an integer

sum_of_numbers = find_sum(input_list)
print("Sum of numbers:", sum_of_numbers)


# In[ ]:




