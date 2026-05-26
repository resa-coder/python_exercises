#1-masala. Svetafor
# while True:
#     colour=input("Which colours are on a traffic light? ")
#     if colour=="red" or colour=="yellow" or colour=="green":
#         print("Thanks, it is suitable")
#     else:
#         print("it is the wrong colour")

#2-masala.Tasodifiy sonni topish o'yini:

# import random
#
# random_number=random.randint(1,10)
# while True:
#     guess=(input("Find the number(1-10): "))
#     if int(guess)==random_number:
#         print("Congratulations, you have  found")
#     else:
#         print("It is wrong, Try again!")

#3-masala.Do'stlar ro'yxatini yaratish
# friends_names=[]
# while True:
#     names = input("Enter the names of your friends: ")
#     if names=="stop":
#         break
#     else:
#         friends_names.append(names)
# print("list of your friends' names: ",friends_names)
#4-masala. Valyuta ayirboshlash kalkulyatori
# amount=input("Enter the amount of money that you want to exchange: ")
# kurs= 12600
# while True:
#     if amount == "exit":
#         break
#     else:
#         dollar=int(amount)/kurs
#         print(dollar)
#         break



#1-masala
i=1
while i<=5:
    print(str(i)*i)
    i+=1

# 2-masala
number=int(input("Enter the number: "))
yigindi=0
while number>0:
    qoldiq=number%10
    yigindi+=qoldiq
    number=number//10
print("raqamlar yigindisi:", yigindi)

# 3-masala
son=1
yigindi=0
while son<100:
    yigindi+=son
    son+=2
print(yigindi)

# 4-masala
numbers=[23,45,67,89,9,7,35,45,54,34,43,23,12]
max1=0 #eng katta son uchun
max2=0 #ikkinchi eng katta son uchun
i=0 #list ichidagi sonlar indeksi uchun
while i<len(numbers):
    hozirgi_son=numbers[i]

    if hozirgi_son>max1:
        max2=max1
        max1=hozirgi_son
    elif max2<hozirgi_son and max1!=hozirgi_son:
        max2=hozirgi_son

    i+=1
print(numbers)
print(max1)
print(max2)

# 5-masala
import random
random_number=random.randint(1,100)
while True:
    guess=input("Guess the number(1-100): ")
    if int(guess)>random_number:
        print("Very high. Try again")
    elif int(guess)<random_number:
        print("Very low. Try again")
    elif int(guess)==random_number:
        print("Congratulations, you have  found")
        break