# sanoq=0
# while sanoq<=5:
#     sanoq+=1
#     print('hello world')

# while True:
#     ism=input('ism kiriting: ')
#     print(f"hello {ism}")
#     if ism=="safiya":
#         print("welcome safiya")
#         break

# i=1
# while i<6:
#     i+=1
#     print(i,end="-")

#while siklidan foydalanib birdan ongacha sonlarni print qilish
# i=0
# while i<=10:
#     i+=1
#     print(i,end="^")

#foydalanuvchidan tugri parol kiritishini sorang agar u togri parol bumasa qayta kiritidhini surayvering
# while True:
#     parol=int(input("parolni kiriting: "))
#     if parol==2007:
#         print("welcome")
#         break
#     else:
#         print("notugri parol qayta urining")

# m=0
# while m<9 and False:
#     print(m,end="-")
#     m+=1

# a=[1,2,3,4,5,6,7,8,9]
# while True:
#     print(f"""
#             {a[0]}   {a[1]}  {a[2]}
#             {a[3]}   {a[4]}  {a[5]}
#             {a[6]}   {a[7]}  {a[8]}
#     """)
#     x = int(input("x: "))
#     a[x - 1] = "x"
#     if a[0]==a[4]==a[8] or a[0]==a[3]==a[6] or a[0]==a[1]==a[2] or a[2]==a[5]==a[8] or a[2]==a[4]==a[6] or a[6]==a[7]==a[8] or a[1]==a[4]==a[7] or a[3]==a[4]==a[5]:
#         print("x is winner")
#     print(f"""
#                 {a[0]}   {a[1]}  {a[2]}
#                 {a[3]}   {a[4]}  {a[5]}
#                 {a[6]}   {a[7]}  {a[8]}
#     """)
#     nol = int(input("0: "))
#     a[nol - 1] = "0"
#     if a[0]==a[4]==a[8] or a[0]==a[3]==a[6] or a[0]==a[1]==a[2] or a[2]==a[5]==a[8] or a[2]==a[4]==a[6] or a[6]==a[7]==a[8] or a[1]==a[4]==a[7] or a[3]==a[4]==a[5]:
#         print("0 is winner")
import random
fruit_list=['apple','grapes','pear','peach','apricot','cherry','banana','orange']
fruit = random.choice(fruit_list)


guesses=set()
while True:
    display=""
    for letter in fruit:
        if letter in guesses:
            display+=letter
        else:
            display+="_"
    print(display)
    if "_" not in display:
        print("you are winner")
    break

guess=input("guess the letter: ")
guesses.add(guess)
if guess not in fruit:
    print("try again")
else:
    print("you are right")
if len(guess)==10:
    print("your tries are over")