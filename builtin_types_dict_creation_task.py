#Crate dict based on given string and list:
# output - {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7'}

keys = 'abcdefg'
values = [1,2,3,4,5,6,7]

my_dict = dict(zip(keys,values))
print(my_dict)

