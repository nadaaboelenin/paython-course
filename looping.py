# list=[12,75,150,180,145,525,50]
# for num in list:
#     if num>500:
#         break
#     if num>150:
#         continue
#     if num%5==0:
#         print(num)

# number = 2344213
# count = 0
# while number !=0:
#     number //= 10
#     count+= 1
# print(str(count))

# num = 2344213
# print(len(str(num)))

# list=[10,20,30,40,50]
# list.reverse()
# for digit in list:
#     print(digit)

# list=[10,20,30,40,50]
# new_list= list[::-1]
# for value in new_list:
#     print(value)


# for i in range(-10, 0, 1):
#     print(i)

# num = (int(input('enter your number:')))
# for tabel in range(1,11):
#     print(tabel*num)

n = 10
num1 = (int(input('enter your number:')))
num2 = (int(input('enter your number:')))
next_number = num2  
count = 1
 
while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
    


