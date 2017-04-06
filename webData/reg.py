import re

x = 'From: Using the : character'
k = 'From: Using the character'
y = re.findall('^F.+:', x)
print y

print re.findall('^F.+:', k)