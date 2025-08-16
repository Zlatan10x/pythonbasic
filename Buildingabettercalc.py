num1 = float(input("Enter the first number :"))
op = input("Enter the operator :")
num2 = float(input("Enter the second number :"))

if op == "+":
    print(f"Sum is :{num1+num2}")
elif op == "-":
    print(f"Sub is :{num1-num2}")
elif op == "*":
    print(f"Multiplication is :{num1*num2}")
elif op == "%":
    print(f"Mod is :{num1%num2}")
else :
    print(f"Divided result is :{num1/num2}")