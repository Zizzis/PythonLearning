hrs = input("Enter Hours:")
h= float(hrs)
rate = input("Enter Rates:")
r= float(rate)
def computepay():
    if h<=40:
        return h*r
    elif h>40:
        h2= h-40
        r2= r*1.5
        return (40*r)+(h2*r2)
print("Pay", computepay())