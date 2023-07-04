#kerj be egy számot, dontse el a program páros-e vagy páratlan
a = input('Add meg a számot:')
szam = int(a)
if szam % 2 == 0:
    print (szam,'A szám páros')
else:
    print (szam, 'A szám páratlan')