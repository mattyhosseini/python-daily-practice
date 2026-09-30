def main ():
    print("\n=== Coordinates Tracker ===\n")
    points = []
    while True:
        print("-- Menu --")
        print("1) Add Coordinates (x,y)")
        print("2) View All Coordinates")
        print("3) Show distance between to point")
        print("0) Quit")

        choose = int(input('Choose an Option : '))

        if choose == 1:
            x = float(input("Enter x : "))
            y = float(input("Enter y : "))
            point = (x,y)
            points.append(point)
            print(f"\npoints : ({x},{y}) added\n")
            
        elif choose == 2:
            if list:
                for  index, item in enumerate(points,start=1):
                    print(f"{index}) {item}")
            else:
                 print("The list is empty. There is nothing to display.")
                
        elif choose == 3:
            point1 = int(input("Choose first point number : ")) -1
            point2 = int(input("Choose first point number : ")) -1
            x1,y1 = points[point1]
            x2,y2 = points[point2]
            
            distance = ((x2-x1)**2 + (y2-y1)**2)** 0.5
            print(f"distance : {distance}")
        elif choose == 0:
            print("\n We hope you enjoyed it. Have a great day! 👋 \n")
            break
        else:
            print('Invalid input. ')

if __name__ == "__main__":
    main()
    