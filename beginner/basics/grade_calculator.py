def main ():
    print("=== Grade Calculator ===")

    score = float(input("Enter your score (0-100) : "))

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >=70:
        grade = "C"
    elif score >=60:
        grade = "D"
    else:
        grade = "F"
    
    print(f"Your grade is {grade}")



if __name__ == "__main__":
    main()