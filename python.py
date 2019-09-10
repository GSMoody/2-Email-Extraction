import re

file = open("sample.txt", 'r')
text=file.read()
output=[]

words=text.split()
for word in words:
    if "@softwire.com" in word:
        output.append(word)

output2=re.findall(r'\S+@softwire.com', text)

output3=re.findall(r'\S+@(\S+)', text)

domains={}

for email in output3:
    if email in domains.keys():
        domains[email] = domains[email] + 1
    else:
        domains[email] = 1

print("Searching manually for 'softwire.com' domain gives "+str(len(output))+" addresses: ")
print(output)
print("Searching with regex for 'softwire.com' domain gives "+str(len(output2))+" addresses: ")
print(output2)
print("Searching with regex for all email addresses gives "+str(len(output3))+" addresses: ")
print(output3)
print("The number of each unique email address is:")
print(domains)

