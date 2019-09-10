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

domains = {}

#output4=re.findall(r'\S+@corndel.com', text)
#for x in output4:
#    print(x)
#print(len(output4))

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
print("There are "+str(len(domains))+" unique domains. The types and occurance of each domain is:")
print(domains)

domains=sorted(domains.items(),key = lambda x : x[1], reverse=True)
print("The 10 most common domains are:")
for x in range(0,10):
    print(domains[x])

f=input("Enter the minimum number of occurrences you wish to search domains for:")
domains_subset=[]

for email in domains:
    if email[1] >= int(f):
        domains_subset.append(email)
print("The domains that occur more than "+f+" times are:")
print(domains_subset)
