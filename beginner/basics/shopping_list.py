def main ():
    print("=== Shopping List App ===")
    shop = []
    
    while True:
        print("--- menu ---")
        print("1) Add item")
        print("2) View list")
        print("0) Quit")
        
        choose = int(input("Choose an Option : "))
        
        if choose == 1:
            item = input("Enter Your item : ").strip()
            if item :
                shop.append(item)
                print(shop)
            else:
                print("Invalid Item")
        elif choose == 2 :
            for index,item in enumerate(shop,start=1):
                print(f"{index}. {item}\n")
        elif choose == 0:
            break
        else:
            print("Invalid Choice")
        
        
if __name__ == "__main__":
    main()
