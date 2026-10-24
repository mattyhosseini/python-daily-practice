from datetime import date

def calculate_age():
    print("\n Age Calculator")
    try:
        year = int(input("Enter birth year (YYYY): "))
        month = int(input("Enter birth month(1-12): "))
        day = int(input("Enter birth day (1-31): "))

        birth_date = date(year , month , day)
        today = date.today()
        
        age = today.year - birth_date.year

        if (today.month, today.day) < (birth_date.month,birth_date.day):
            age -= 1
        
        print(f"\n You are {age} years old")

    except ValueError:
        print("Invalid date. Please enter a valid date.")
        

def main():
    while True:
        calculate_age()

        choice = input("\nCalculate again?(y/n): ").lower()
        if choice != "y":
            print("Goodbye")
            break




if __name__ == "__main__":
    main()