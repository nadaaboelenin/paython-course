# names=['mohamed','ail','taha','farida','hassan','mahoud','khalid']
# for name in names:
#     print(name.upper())

# user=[name.upper() for name in names]
# print(user)

# user=lambda names: [name.upper() for name in names]
# print(user(names))

# -------------------------------------------------------------------------------------------------------   
# names = ['mohamed','ail','taha','farida','hassan','mahoud','khalid']
# letters ='a'
# final_list=[]
# for word in names:
#     for letter in word:
#         if letter in letters:
#          print(word)


# data = ['mohamed','ail','taha','farida','hassan','mahoud','khalid']
# letters = 't'
# def checkletter():
#     for letter in data:
#         if letter.startswith(letters):
#             print(letter)
# checkletter()        

names=['mohamed','ail','taha','farida','hassan','mahoud','khalid']
letter='t'
final_list=[name.startswith(letter) for name in names]
print(final_list)







