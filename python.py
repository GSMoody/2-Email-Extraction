import re

file = open("sample.txt", 'r')
text=file.read()
output=[]

text=text.split()
for word in text:
    if "@softwire.com" in word:
        output.append(word)

print(text)
print(output)

