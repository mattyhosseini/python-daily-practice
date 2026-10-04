def main ():
    print("=== Shopping List Cleaner ===")

    text = input("Enter your shopping list item separated by commas : \n")
    
    # Split by commas , strip spaces , and lowercase 
    items = [item.strip().lower() for item in text.split(",") if item.strip()]
    
    # use set() to remove duplicates
    unique_item = sorted(set(item))

    print("\n  --- Cleaned Shopping List --- ")
    print("Total items entered : ",len(items))
    print("Unique items : " , len(unique_item))
    
    print("Your cleaned list")
    
    for item in unique_item:
        print("- ",item)
        


if __name__ == "__main__":
    main()  