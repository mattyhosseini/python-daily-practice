def add (a,b):
    return a + b 

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b 

def divide(a,b):
    if b == 0:
        print("Error : Division by zero")
    return a / b



def main ():
    
    print("=== Simple Calculator ===")
    
    print("Choose an operation : ")
    print("1) Add")
    print("2) Subtract")
    print("3) Multipy")
    print("4) Divide")
    choose = int(input("Enter 1-4 : "))
    print("Ask for first and second number here")
    
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    
    if choose == 1 :
        result = add(num1,num2)
        print(f"result : {result}")
    elif choose == 2:
        result = subtract(num1,num2)
        print(f"result : {result}")
    elif choose == 3:
        result = multiply(num1,num2)
        print(f"result : {result}")
    elif choose == 4:
        result = divide(num1,num2)
        print(f"result : {result}")
    else:
        print("Invalid choice.")
    
    
if __name__ == "__main__":
    main()