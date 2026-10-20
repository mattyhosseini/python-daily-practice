FILE_NAME = "notes.txt"

def viwe_notes():
    print("\n --- Your Notes ---")
    try:
        with open(FILE_NAME,'r') as file:
            content = file.read()
            if content.strip() == "":
                print("No notes yet.")
            else:
                print(content)
    except FileExistsError:
        print("No notes file found. Add a note first.")

def add_notes():
    note = input("\n Enter your note: ")
    if note.strip() == "":
        print("Note Cannot be empty.")
        return
    
    with open(FILE_NAME,"a") as file:
        file.write(note + "\n")

    print("Note savad successfuly.")

def main():
    while True:
        print("\n ====================")
        print("Simple Notes App")
        print("\n ====================")
        print("1. View notes")
        print("2. Add note")
        print("Exit")

        choice = ("Choose an option (1-3): ")

        if choice == "1":
            viwe_notes()
        elif choice == "2":
            add_notes()
        elif choice == "3":
            print("Good bye")
        else:
            print("Invalid choice.")
            
            
if __name__ == "__main__":
    main()