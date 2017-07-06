x = 2
print(x == 2)
print(x==3)
print(x<3)

# if with and

if x == 2 and x < 3 :
    print("You are on the right track")


if x == 1 or x < 3 :
    print("You too are on the right track")

#If the array contains

name = "John"
if name in ["John", "Doe"] :
    print("Your name is either john or Doe")


#The if and else
x=3
if x==2:
    print("x is fine !")
else:
    print("x has some issue")


# The example of '==' means equal and 'is' means same instance
x = [1, 3, 5]
y = [1, 3, 5]
print(x == y)
print(x is y)


#not operator
k = 5
if k != 6 :
    print("k not equal to 6")
if not k==7:
    print("k not equal to 7")
print(not(k==9))
