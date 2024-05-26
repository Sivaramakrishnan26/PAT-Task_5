import re

# a) Email Address (Eg: test@gmail.com, test@gmail.co.in)
Email = input("Enter an E-Mail ID: ")  # Get an input from the user
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+"  # Format of Email ID
match = re.search(pattern, Email)  # Check an input is matching the pattern
if match:
    print("Match Found")
else:
    print("No Match Found")

# b) Mobile Numbers of Bangladesh (Eg: +880-1234-567892 or 00880-1234-567892 or 01-1234-678932)
Bangladesh_Mobile_Number = input("Enter Bangladesh Mobile Number: ")  # Get an input from the user
pattern = r"^(?:(?:\+880|00880|01)-1)?\d{3}\-\d{6}$"  # Format of Bangladesh Mobile Number
match = re.search(pattern, Bangladesh_Mobile_Number)  # Check an input is matching the pattern
if match:
    print("Match Found")
else:
    print("No Match Found")

# c) Telephone Numbers of the USA (Eg: +1-123-456-7890 or 123-456-7890)
USA_Telephone_Number = input("Enter USA Telephone Number: ")  # Get an input from the user
pattern = r"^(?:\+1-)?\d{3}\-\d{3}\-\d{4}"  # Format of USA Telephone Number
match = re.search(pattern, USA_Telephone_Number)  # Check an input is matching the pattern
if match:
    print("Match Found")
else:
    print("No Match Found")

"""d) 16 character of Alpha-Numeric password composed of alphabets of Upper Case, Lower Case, Special Characters 
and Numbers (Eg: TesT@123+456/789)"""
Password = input("Enter a Password: ")  # Get an input from the user
pattern = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}'  # Format of password
match = re.search(pattern, Password)  # Check an input is matching the pattern
if match:
    print("Match Found")
else:
    print("No Match Found")