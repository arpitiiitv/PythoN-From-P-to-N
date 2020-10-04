## printing statments
print("Hello world")
print("Arpit Tiwari ",end="")
print("Python Coder")
# by default end="\n" newline
print("Arpit Tiwari ",end=",")
print("Python Coder",end=" and ")
print("Good boy")
print("Arpit","tiwari")


#### printing special characters
print("special characters")
print("C:\network") # wrong
print("C:\\network") # right
print("\"Arpit\"")

######
print("typechecking")
var1 = 100
var2 = 100.12
var3 = "100" 
print(type(var2))
print(type(var2))
print(type(var3))

##### Typecasting
print("Typecasting")
x= 100
y= 200
print(x+y)
print(str(x)+str(y))
print(float(x)+float(y))
strng = "123"
print(int(strng))

### extra
print(10*"Arpit")

#output using .format
print("The value of var1 is: {}, val2 is: {} and var3 is: {}".format(var1,var2,var3))
#one more example:
print("Value of var4 is {} and var5 is {}".format(23,46))
