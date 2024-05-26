list1 = [10, 501, "22", 37, 100, 999, 87, 351, "A", "D"]  # Input List
Integer = filter(lambda x:isinstance(x,int) , list1)  # Check each element is an Integer using lambda function and filter the list
String = filter(lambda x:isinstance(x,str) , list1)  # Check each element is a String using lambda function and filter the list
print(list(Integer))  # Print the Integer List
print(list(String))  # Print the String List
