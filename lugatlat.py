telefonlar = {
    'ali':'iphone xs-max',
    'vali':'galaxy s10+',
    'olim':'xiami redmi  note 10 ',
    'orif':'iphone 13pro max'
    }
for k, q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")

mahsulotlar = { 
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }

print(mahsulotlar.keys())
print('Do\'kondagi mahsulotlar:')
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())
    