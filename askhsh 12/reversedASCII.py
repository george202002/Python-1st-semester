import string
file = open("textdoc2.txt", "r")

content = file.read()

content = content.translate(str.maketrans('', '', string.punctuation))

code = [ord(count) for count in content]


for count in range(len(code)):
    if code[count] != 32:
        code[count] = 128 - code[count]

code.reverse()

text = [chr(i) for i in code]
finaltext = ''.join([str(x) for x in text])
print(finaltext)
file.close()
