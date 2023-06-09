def computepay(hours_worked, rate):
    if hours_worked <= 40:
        return hours_worked * rate
    elif hours_worked > 40:
        overtime = hours_worked - 40
        overtime_rate = rate * 1.5
        return (40 * rate) + (overtime * overtime_rate)

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rates:")
r = float(rate)

print("Pay", computepay(h, r))

