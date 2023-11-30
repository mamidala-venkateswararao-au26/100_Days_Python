# # # # # age=17
# # # # # if(age>=18):
# # # # #   print("You are eligibale for Vote")
# # # # # else:
# # # # #   print("You are not eligible for vote")

# # # # num =int(input("Enter Number:"))
# # # # N = 7

# # # # if(num%N==0):
# # # #   print(num,"is divisble by",N)
# # # # else:
# # # #   print(num,"not divisable by",N)  

# # # # num= int(input("enter the number:"))

# # # # if (num%5==0):
# # # #   print("Hello")
# # # # else:
# # # #   print("Bye")
# # # # city =input("Enter the city name:")
# # # # if(city=="Delhi"):
# # # #   print("redFort")
# # # # elif(city=="Agra"):
# # # #   print("Taj Mahal")
# # # # elif(city=="jaipur"):
# # # #   print("Jah Mahal")
# # # # else:
# # # #   print("Nothing")

# # # # Write a program to accept percentage from the user and display the grade according to the  following criteria.
# # # # Percentage	Grade
# # # # 91-100	O
# # # # 81-90	A
# # # # 71-80	B
# # # # 61-70	C
# # # # 51-60	D
# # # # 41-50	E
# # # # Below 40	Fail
# # # marks =int(input("Enter the marks:"))

# # # if (marks>=91 and marks<=100):
# # #   print("A+")
# # # elif(marks>=81 and marks<=90):
# # #   print("A")
# # # elif(marks>=71 and marks<=80):
# # #   print("B")
# # # elif(marks>=61 and marks<=70):
# # #   print("C")
# # # elif(marks>=51 and marks<=60):
# # #   print("D")
# # # elif(marks>=41 and marks<=50):
# # #   print("E")
# # # else:
# # #   print("Fail")



# # #write a program to accept the cost price of a bilke and display the road tax to be paid asccorading to the following criteria:
# # # Cost Price	Road Tax
# # # Upto Rs. 2500	No Tax
# # # From Rs. 2500 to Rs. 5000	5% Tax
# # # From Rs. 5000 to Rs. 10000	10% Tax
# # # More than Rs. 10000	15% Tax

# # #Ans)

# # # road_tax=int(input("Enter the cost :"))

# # # if (road_tax>10000):
# # #   print(road_tax,"15% Tax")
# # # elif(road_tax>2500 and road_tax<=5000):
# # #   print(road_tax,"5% Tax")
# # # elif(road_tax>5000 and road_tax<=10000):
# # #   print(road_tax,"10% Tax")
# # # else:  
# # #   print(road_tax,"No Tax")

# # # # # Write a program to accept a number from the user and display the cube of the number.

# # # number=int(input("Enter the number:"))
# # # cube =number **3

# # # print("The cube of ",number ,"is",cube)

# # #write a program to check whether an yearis leap year or not.
# # year =int(input("Enter the year :"))

# # if(year%4==0 and year%100!=0 or year%400==0):
# #   print(year,"is a leap year")
# # else:
# #   print(year,"is not a leap year")  

# # write a progamto acpect a number  from 1 to 7 and display the nae of the day like 1 for  sunday 2 for monday and so on..

# number =int(input("Enter the number:"))
# if (number==1):
#   print("Sunday")
# elif(number==2):
#   print("Monday")
# elif(number==3):
#   print("Tuesday")
# elif(number==4):
#   print("Wednsday")
# elif(number==5):
#   print("Thursday")
# elif(number==6):
#   print( "Friday")
# elif(number==7):
#   print("Saturday")
# else:
#   print("Invalid Input")  

#write a program to whethwr a number (accepted from user)is divisible by 2 and 3 both..
# number=(int(input("Enter the number:")))

# if (number%2==0 and number%3==0):
#   print("The number is divisible by 2 and 3")
# else:
#   print("The number is not divisible by 2 and 3")  

#write program to find the laragest number

# num4=int(input("Enter the number"))

# num1=int(input("Enter the number"))
# num2=int(input("Enter the number"))
# num3=int(input("Enter the number"))

# largest_number=max(num1,num2,num3,num4)


# print(largest_number)
