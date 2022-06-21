# create Hello World program
print("Hello World!")

# Creating Variables
wish = "Hello World!"      # x is of type "string" , string always declare in double quotes ("")
number = 10      # x is of type *integer*
dec_number = 30.33   # x is of type "float"
this_list = ["red", "green", "yellow"]  # x is a type of "list" ,  to declare a list use [] brackets
this_tuple = ("red", "green", "yellow")  # x is a type of "tuple" ,  to declare a tuple use () brackets
this_set = {"red", "green", "yellow"}  # x is a type of "set" ,  to declare a set use {} brackets
this_dict = {"name" : "mahesh", "age" : 22}  # x is a type of "dict" ,  to declare a dict use {} brackets
                                     # stores the data in key : value format
bool_value = True    # boolen values ,its returns only True or false
x = None    # x is of type of noneType (null reference)

# ________________formatting strings____________

First = "Mahesh"
Last = "Papolu"
message = First + ' [' + Last + '] is a coder'      # formal procedure
print(message)
msg = f'{First} [{Last}] is a coder'  # formatting the strings
print(msg)

# _____________String Methods___________

wish = "Hello World!"   # creating variable
print(len(wish))    # len() function , returns the length of the string #12
print(wish.upper())     # return the string in upper case
print(wish.lower())     # return thr string in lower case
