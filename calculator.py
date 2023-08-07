def sum(a,b):
    return a+b
def product(a,b):
    return a*b
def sub(a,b):
    return a-b
def division(a,b):
    return a/b


num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
operator = input("Select +,-,*,/ :") 

if operator =="+":
    result = sum(num1,num2)
    print(">>>",result)
elif operator =="-":
    result = sub(num1,num2)
    print(">>>",result)
elif operator =="*":
    result = product(num1,num2)
    print(">>>",result)
elif operator =="/":
    result = division(num1,num2)
    print(">>>",result)
else:
    print("select valid Operator")
