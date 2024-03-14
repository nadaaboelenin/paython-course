# Q8

# bill=int(input('Enter your bill amoumt:'))

# if 0< bill and 100 > bill <200:
#     print('nocharge')
# elif 100 < bill <=200:
#     print((bill-100)*5)
# elif 200 < bill:
#     print((bill*10)-1500)
# else:
#     print('enter vaild number')

# ----------------------------------------------    


# Q1
# mark=int(input('Enter your Mark:'))

# if mark > 90:
#     print('Grade:A')
# elif 90 > mark >=80:
#     print('Grade:B')
# elif 80 > mark >=60:
#     print('Grade:C')
# else:
#     print('Grade:D')
# ---------------------------------------------------
# Q2
# Price = int(input('Eenter Your Price:'))

# if Price > 100000 :
#     print((Price*15)/100)

# elif Price > 50000 and Price <= 100000 :
#     print((Price*10)/100) 

# elif Price<= 50000:
#     print((Price*5)/100)
# else:
#     print('enter a vaild price')
# --------------------------------------------------------
# Q5

# num1 = int(input("Enter your first number:"))
# num2 = int(input("Enter your scounde number"))

# print(num1) if num1>num2 else print(num2)

# --------------------------------------------------------------
# Q6
# num3 = int(input('enter your number:'))
# print("positve") if num3>0 else print('negaive')
# ---------------------------------------------------------------
# Q7

# num4 = int(input('enter your number:'))
# print("even") if num4%2 == 0 else print('ood')
# --------------------------------------------------------------
# Q9
# num5 = int(input("Enter the first number:"))
# num6 = int(input("Enter the second number:"))
# num7 = int(input("Enter the third number:"))

# if num5 > num6 and num5 > num7:
#     print(num5)
# elif num6 > num5 and num6 > num7:
#     print(num6)    
# else:
#     print(num7)
# ---------------------------------------------------------------
                                    # part two

# -------------------------------------------------------------------------------------------------------------

# workingdays= int(input("Eentr Your Working Days:"))
# absentdays= int(input('Enter Your absent days:'))
# persetage= workingdays - absentdays
# print ( "you can't enter your exam ") if (workingdays*persetage)/100 <75 else print('ok')
# -----------------------------------------------------------------------------------------------------
# Q2
grade= int(input('Eentr your grade:'))

if grade<= 25:
    print('D')
elif grade> 25 and grade<=45:
    print("C")  
elif grade> 45 and grade<= 50:
    print('B')     
elif grade> 50 and grade<=60:
    print('B+')    
elif grade> 60 and grade<=80:
    print("A") 
else:
    print("A+")       

    

 

 

