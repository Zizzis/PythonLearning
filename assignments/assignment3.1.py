hrs = input("Enter Hours:")
h = float(hrs)
rate = input ("Enter Rate:")
r = float(rate)
if h<=40 :
    print (h * r)
else :
    tulora = h - 40
    tulorarate = r*1.5
    print ((40 *r)+(tulora*tulorarate))