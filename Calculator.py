#Interface for taking input from user
a=int(input("Enter first number  : "))
b=int(input("Enter second number : "))

#adding addition feature 
def addition(x,y):
 return(x+y) 

print(a,"+",b,"=",addition(a,b))


#adding substraction feature 
def substraction(x,y):
 return(x-y) 

print(a,"-",b,"=",substraction(a,b))


#adding multiplication feature 
def multiplication(x,y):
 return(x*y) 

print(a,"*",b,"=",multiplication(a,b))


#adding division feature 
def division(x,y):
 return(x/y) 
print(a,"/",b,"=",division(a,b))