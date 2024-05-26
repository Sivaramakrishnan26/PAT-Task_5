list1 = [10, 501, 22, 37, 100, 999, 87, 351]  # Input List
result = filter(lambda x: x > 4, list1)  # Check each element is greater than 4 using lambda function and filter the list
print(list(result))  # Print the output

"""
Answer:
All the elements are greater than 4. So the output is [10, 501, 22, 37, 100, 999, 87, 351]
"""
