print("A simple Calculator")

op1=int(input("Enter First Operand  "))
op2=int(input("Enter Second Operand "))
print("_____________________\n")
input_operator=input("What do you want to do?")
if input_operator== "+":
    print(op1+op2)
elif input_operator=="-":
    print(op1-op2)
elif input_operator=="*":
    print(op1*op2)
elif input_operator=="/":
    if(op2==0):
        print("not division by zero")
    else:
        print(op1/op2)
else:
    print("Invalid Input!") 




