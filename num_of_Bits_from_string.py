# initializing string  
test_str = "GeeksforGeeks"

# printing original string  
print("The original string is : " + str(test_str))

# using join() + ord() + format() 
# Converting String to binary 
res = ''.join(format(ord(i), 'b') for i in test_str)

print(res)