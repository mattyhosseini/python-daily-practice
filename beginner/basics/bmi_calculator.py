def calculater_bmi():
    print("\n ---BMI Calculator---")
    
    try:
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))

        bmi = weight / (height**2)
        print(f"\n Your BMI is: {bmi:.2f}")
    
        if bmi < 18.5:
            print("Category : Underweight")
        elif bmi < 25:
            print("Category : Normal")
        elif bmi < 30:
            print("Category : Overweight")
        else:
            print("Category:Obese")
    except ValueError as e:
        print(f"ValueError : {e}")
    except ZeroDivisionError:
        print("ZeroDivisionError : height cannot be zero")
        


def main():
    while True:
        calculater_bmi()

        choice = input("\n Calculater again? (y/n): ").lower()
        if choice != "y":
            print("Goodbye")
            break
        

if __name__ == "__main__":
    main()