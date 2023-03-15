import re
password = input()

#your code goes here
pattern = r"\w*[A-Z]\w*[0-9]\w*" 
if re.match(pattern, password):                          
print("Password created")

else: 
 print("Wrong format")
