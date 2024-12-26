# write a function that take  two integer and than multple thst number with 2

def two_numbers (num1,num2):
    
    return num1 *2, num2 * 2

result1,result2 =two_numbers(5,10)

print(result1,result2)




# what is __init__()in python ?

class book1shop:
    
    def __init__(self,title):
        self.title = title

    def book(self):
        print("The title of the book",self.title)
        
A = book1shop(title="Think like a monk")
X = book1shop(title="Think like a SANDMAN")
X.book()
A.book() 




# what is a difference between a mutable data type and an immutable data type ?

# mutable data type
a_list = [1,2,3,4]
a_list.append(5)
print(a_list)

# dictironary 
a_dcit = {"a":1,"b":2,"c":3}
a_dcit["d"] = 4

print(a_dcit)

# An immutable data type 

# Numeric Example
a_num = 10
a_num = 20  # Creates a new integer object
print(a_num)  # Output: 20

# String Example
a_str = "hello"
a_str = "world"  # Creates a new string object
print(a_str)  # Output: world

# Tuple Example
a_tuple = (1, 2, 3)
# a_tuple[0] = 4  # This will raise a TypeError
print(a_tuple)  # Output: (1, 2, 3)