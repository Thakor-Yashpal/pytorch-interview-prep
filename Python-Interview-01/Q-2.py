# #Q 1


# class Animes:
#     def __init__(self,Anime_name,Rating,Episodes):
#         self.Anime_name=Anime_name
#         self.Rating=Rating
#         self.Episodes=Episodes
    
#     def Laanime(Self):
#         print(f'Which anime do you like {Self.Anime_name} ? that have rating of {Self.Rating}  adn howmany episodes {Self.Episodes}')

# anime_A = Animes("Naruto",8.5,100)
# anime_B = Animes('bluelock',7.5,21)

# anime_A.Laanime()
# anime_B.Laanime()   


# # Q 2

# class NumbersStr:
    
#     def check_numbers(self):
#         n = 0
#         for n in range(1,50):
#             if n % 2:
#                 print(f'This is an odd number: {n}')
#             else:
#                 print(f'This is an even number: {n}')

# # Create an instance of the class and call the method
# numbers = NumbersStr()
# numbers.check_numbers()



# # Q 3 

# with open('Test2.py','w') as file:
#     file.write("")


# # what is Binary Search  

# #  lest start from tomorow

# class user_input:
#     def __init__(self,Username,Password,Email):
#         self.Uswname = Username
#         self.Password = Password
#         self.Email = Email
        
#     def __init_subclass__(cls):
#         user_name = input("user_input")
#         return user_name


# # checking number 
i = 0
for i in range(0,10):

    if i % 2:
        print(f"You have odd number = {i}")
    else:
        print(f"You have even number = {i}")         