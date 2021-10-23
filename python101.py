# QUESTION 1
# Calculation of Area of Circle
# PI = 3.142
# raduis = int(input("Enter your raduis: "))
# print("Your raduis is "+ str(raduis))
# if(raduis, int):
#     Area = PI*raduis*raduis
#     print("Your Area is " + str(Area))
# else:
#     print("That number is not a number oh")

# Questions 2
# lenght = int(input("Enter the lenght of the rectangle: "))
# print("Your raduis is "+ str(lenght))
# width = int(input("Enter the width of the rectangle: "))
# print("Your raduis is "+ str(width))
# if(lenght, int and width, int):
#     Area = lenght*width
#     print("Your Area is " + str(Area))
# else:
#     print("That number is not a number oh")
    
# # Question 3
# side = int(input("Enter the lenght of a square: "))
# print("Your lenght is "+ str(side))
# if(side, int):
#     Area = side*side*side*side
#     print("Your Area is " + str(Area))
# else:
#     print("That number is not a number oh")
    
# Question 4
PI = 3.142
choice = input("spell out your choice of shape:'circle','square' or 'rectangle'")
print("Your choice shape is "+ str(choice))
if(choice == "circle"):
    raduis = int(input("Enter your raduis: "))
    print("Your raduis is "+ str(raduis))
    if(raduis, int):
       Area = PI*raduis*raduis
       print("Your Area is " + str(Area))
    else:
       print("That number is not a number oh")
       
elif (choice == "square"):
    side = int(input("Enter the lenght of a square: "))
    print("Your lenght is "+ str(side))
    if(side, int):
       Area = side*side*side*side
       print("Your Area is " + str(Area))
    else:
       print("That number is not a number oh")
       
       
elif  (choice == "rectangle"):
       lenght = int(input("Enter the lenght of the rectangle: "))
       print("Your raduis is "+ str(lenght))
       width = int(input("Enter the width of the rectangle: "))
       print("Your raduis is "+ str(width))
       if(lenght, int and width, int):
            Area = lenght*width
            print("Your Area is " + str(Area))
       else:
             print("That number is not a number oh")
else:
    print("Guy run the program again and make a choice while checking for any spelling errors maybe")