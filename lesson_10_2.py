#1-masala
pochtalar=["user1@gmail.com", "user2yahoo.com","user@3outlook.com"]

for email in pochtalar:
    if "@" in email:
        print(True)
    else:
        print("notugri email manzili")
#2-masala
parollar=["password123","Qwerty","admin","StrongPass1!"]

for element in parollar:
    if len(element)<8:
        print("juda qisqa")
    elif not any(c.isdigit() for c in element) or all(c.isalnum() for c in element):
        print("kuchsiz parol")
    else:
        print("kuchli parol")
#3-masala
list=[20,22,19,24,25,23,21]
jami=0
for temperature in list:
    jami+=int(temperature)
    kunlar_soni = len(list)
    ortacha_harorat = jami/kunlar_soni
print(ortacha_harorat)
for temperature in list:
    jami+=1
    if temperature>=22:
        print("iliq kun")
    else:
        print("salqin kun")
#4-masala
taomlar_ruyxati=["osh","shashlik","manti","lag'mon"]
a=input("buyurtma: ")
topildi=False
for taom in taomlar_ruyxati:
    if a==taom:
        topildi=True
        break
if a==taom:
        print("buyurtmangiz qabul qilindi")
else:
        print("kechirasiz, bunday taom yo'q")
#5-masala
yoshlar_ruyxati=[16,21,17,30,25]
yoshi=0
for yosh in yoshlar_ruyxati:
    yoshi+=yosh
    if yosh<18:
        print("yosh chegarasiga yetmagan")
    else:
        print("xush kelibsiz")
#6-masala
habarlar=["yangi xabar","batareya past","yangilanish mavjud"]
for habar in habarlar:
    if habar=="batareya past":
        print("telefoningizni quvvatlang")
    else:
        print("hammasi ajoyib")
#7-masala
fayllar=["kitob.jpg","ko_jiguli.mp3","tabiat.jpg","malohat.mp3","iphone16.jpg"]
musiqalar=[]
rasmlar=[]
for fayl in fayllar:
    if fayl.endswith(".jpg"):
        rasmlar.append(fayl)
    else:
        musiqalar.append(fayl)
print(rasmlar)
print(musiqalar)


