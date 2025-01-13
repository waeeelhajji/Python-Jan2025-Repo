from class_pkg.shape import  Shape
from class_pkg.square import Square

# print(my_int)
# say_hello()
# print(my_new_var)

#shape_1=Shape("shape_1","white")
#shape_1.print_info()
square_1=Square("square_1","Red",5)
# square_1.print_info() #inherited method with overriding
# square_1.print_square_info() #imported instance method
square_1.calculate_area()
square_1.identification=4
# print(square_1.identification)

# print(square_1.get_id())

# print("Hello there Im' an output")
# potato=input("Please imput a comment")
# print(f"your comment was {potato}")
# list_of_squares=[]
# print("************Menu of Options***********************")
# print("1)Add a square to your list of squares")
# print("2) List all your squares")
# print("0) Terminate the program")
# option=input("please make a choice")
# while option !="0":
#     if option=="1":
#         square_name=input("Please enter the square name")
#         square_color=input(f"please enter the color of {square_name}")
#         square_side=input(f"please enter the side of {square_name}")
#         new_square=Square(square_name,square_color,square_side)
#         list_of_squares.append(new_square)
#         new_square.print_info()
        
#     elif option=="2":
#         for element in list_of_squares:
#             element.print_info()
#             print("*"*10)
    
#     option=input("please make a choice")
        