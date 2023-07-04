#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


handle = open("mbox-short.txt")
senders = dict()
emails = list() 
for line in handle:
    if line.startswith("From "):
        lines = line.split()
        emails.append(lines[1])
for email in emails:
    if email not in senders:
        senders[email] = 1
    else:
        senders[email] = senders[email] + 1 
bigsender = None
bigemail = None
for email, count in senders.items():
    if bigsender is None or count > bigsender:
        bigemail = email
        bigsender = count
print(bigemail, bigsender)

