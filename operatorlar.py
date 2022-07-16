mehmonlar=["ali","vali","jasur"]
for mehmon in mehmonlar:
        print("Salom",mehmon)
        print("Xayr",mehmon)
avtolar=["audi","bmw","volvo","kia","hyandai"]
for avto in avtolar:
        if avto == "bmw":
                print(avto.upper())
        else:
                print(avto.title())

yosh = int(input('Yoshingiz nechida? '))
if yosh<=4:
    print('Sizga kirish bepul.')
elif yosh<=12:
    print('Sizga kirish 5000 so\'m')
else:
    print('Sizga kirish 10000 so\'m')


kun = input("Bugun nima kun?>>>")
if kun.lower()=='shanba' or kun.lower()=='yakshanba':
    print('Bugun dam olish kuni.')
else:
    print('Bugun ish kuni.')


narh = 15000 
choy = True 
salat = False

if choy and salat: 
    narh = narh + 10000 
elif choy or salat: 
    narh = narh + 5000  
print(narh)    
