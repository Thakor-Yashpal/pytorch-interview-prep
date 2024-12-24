# write a function that take  two integer and than multple thst number with 2

def two_numbers (num1,num2):
    
    return num1 *2, num2 * 2

result1,result2 =two_numbers(1,12)

print(result1,result2)


# what is __init__()in python ?

class bookshop:
    
    def __init__(self,title):
        self.title =title
    
    def book(Self):
        print("The Title Of The Book is",Self.title)

B = bookshop("Think like a monk")
B.book()