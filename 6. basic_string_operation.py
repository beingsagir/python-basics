strVal = "Hello World"
print(strVal)

# This will print the length of the string
print(len(strVal))

# This will print the location of the O
print(strVal.index("o"))

# This will count and print a perticular string in the string
print(strVal.count("l"))

#this will find letters in the menssioned position
print(strVal[3:7])
print(strVal[-1 : -2])
print(strVal[: 10])
print(strVal[1: 10: 2])

#String Reverse
print(strVal[:: -1])

#uppercase
print(strVal.upper())
#Lowercase
print(strVal.lower())

#starts with and end with || Returns Boolean
print(strVal.startswith("Hello"))
print(strVal.endswith("abcd"))

splitedWords = strVal.split(" ")
for x in splitedWords :
    print(x)





