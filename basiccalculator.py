print("----------python calculator----------")

print("1-Sum")
print("2-Substact")
print("3-Multiply")
print("4-divide")
print("5-Mod")

def sum(x,y) :
    
    return x+y

def minus(x,y) :
    
    return x-y

def multi(x,y) :
    
    return x*y

def div(x,y) :
    
    return x/y

def mod(x,y) :
    
    return x%y

choice = input("choose what you want to do(1-5) :")

x = float(input("enter first num : "))
y = float(input("enter second num :"))

if choice == '1' :
   print(sum(x,y))
    

elif choice == '2':
    
    print(minus(x,y))
    

elif choice == '3':
    print(multi(x,y))

elif choice == '4':
  
    print(div(x,y))
    

elif choice == '5':
    print(mod(x,y))
    