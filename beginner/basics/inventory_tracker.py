def main ():
    print("=== Inventory Tracker ===")
    inventory = {}
    while True:
        print("""Options:
1. Add item
2. Remove item
3. View inventory
4. Quit""")
             
        
        choose = int(input("Choose an option (1-4) : "))
        
        if choose == 1:
             item = input("Enter Your item : ").strip().lower()
             qty = input("Enter quantity : ")
             
             if not qty.isdigit():
                 print("Quantity must be a number")
                 continue
             qty = int(qty)
             
             # add
             if item in inventory:
                 inventory[item] = qty
                 print(f"Updated {item} , new quantity : {inventory[item]}")
             else:
                 inventory[item] = qty
                 print(f"Added  {item} with quantity {qty}")
        elif choose == 2:
            item = input("Enter item name to remove : ").strip().lower()
            if item in inventory:
                del inventory[item]
                print(f"Removed {item} from inventory")
            else:
                print("Item not fount")
        elif choose == 3:
            if not inventory:
                print("Inventory is empty.")
            else:
                for item,qty in inventory.items():
                    print(f"-{item} : {qty}")
        elif choose == 4:
            print("Good Bye")
            break
        else:
             print("Invalid Choice")
             
             
if __name__ == "__main__":
    main()