# # 1 write a function that take  two integer and than multple thst number with 2

# def two_numbers (num1,num2):
    
#     return num1 *2, num2 * 2

# result1,result2 =two_numbers(5,10)

# print(result1,result2)




# # 2  what is __init__()in python ?

# class book1shop:
    
#     def __init__(self,title):
#         self.title = title

#     def book(self):
#         print("The title of the book",self.title)
        
# A = book1shop(title="Think like a monk")
# X = book1shop(title="Think like a SANDMAN")
# X.book()
# A.book() 




# # 3 what is a difference between a mutable data type and an immutable data type ?

# # mutable data type
# a_list = [1,2,3,4]
# a_list.append(5)
# print(a_list)

# # dictironary 
# a_dcit = {"a":1,"b":2,"c":3}
# a_dcit["d"] = 4

# print(a_dcit)

# # An immutable data type 

# # Numeric Example
# a_num = 10
# a_num = 20  # Creates a new integer object
# print(a_num)  # Output: 20

# # String Example
# a_str = "hello"
# a_str = "world"  # Creates a new string object
# print(a_str)  # Output: world

# # Tuple Example
# a_tuple = (1, 2, 3)
# # a_tuple[0] = 4  # This will raise a TypeError
# print(a_tuple)  # Output: (1, 2, 3)




# # 4 Explain list, dictionary, and tuple comprehension with an example 

# my_list = [i for i in range(1,10)]
# print(my_list)

# # Dictionary
# my_dict = {i: i**2 for i in range(1,10)}
# print(my_dict)

# # Tuple
# my_tuple = tuple(i for i in range(1,10))
# print(my_tuple)


class Anime_Name:
    
    def __init__(self, Anime_name, Rating, Do_you_like_it):
        self.Anime_name = Anime_name
        self.Rating = Rating
        self.Do_you_like_it = Do_you_like_it
        
    def LAnime(self):
        print(f"Do you like this anime: {self.Anime_name}?") # Added a question mark
        
# Create instances of the class
anime_a = Anime_Name('Cowboy Bebop', 5, 'Yes')  
anime_b = Anime_Name('Steins:Gate', 6, 'Yes')

# Call the method on the instances
anime_a.LAnime()
anime_b.LAnime() 
