#kerj be ket szamot, mondd meg melyik a nagyobb, egyenlőségre figyelve

a = input('Add meg az első számot:')
szam1 = int(a)
b = input ('Add meg a második számot:')
szam2 = int(b)
print(szam1,',' , szam2)
if szam1 > szam2: 
    print ('Az első szám a nagyobb.')
elif szam1 == szam2:
    print ('A két szám megegyezik.')
else:
    print ('A második szám a nagyobb.')