#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

handle = open("mbox-short.txt")
hourscount = dict()
hourslist = list() 
for line in handle:
    if line.startswith("From "):
        lines = line.split()
        hour = lines[5].split(":")
        hourslist.append(hour[0])
for hour in hourslist:
    if hour not in hourscount:
        hourscount[hour] = 1
    else:
         hourscount[hour] =  hourscount[hour] + 1 
for key, val in sorted(hourscount.items()):
    print(key, val)



