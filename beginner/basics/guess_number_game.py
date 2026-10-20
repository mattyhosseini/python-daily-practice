import random 

def guess_number_game():
    print("Guess Number Game ")
    print("I'm thinking of a number a number between 1 and 100.")

    secret_number = random.randint(1,100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1 
            
            if guess < secret_number:
                print("Too low ! Try again.")
            elif guess > secret_number:
                print("too high! Try again.")
            else:
                print(f"Corrent ! your guessd it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number")
    guess = int(input("Enter your guess: "))
    print(guess)
    
def main ():
    while True:
        guess_number_game()
        
        play_again = input("Play again: (y/n): ").lower()
        if play_again != "y":
            print("Goodbye")
            break
        
        
if __name__ == "__main__":
    main()
