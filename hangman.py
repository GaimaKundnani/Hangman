import random
# WordSets
animals= ["ant", "bat", "cat"]
shapes= ["square", "triangle", "circle"]
places= ["rajasthan", "punjab", "gujarat"]
# Start Game
def start(level, player):
    if level=="Easy":
        print("1. Aminal")
        print("2. Shapes")
        print("3. Places")
        set_ch= int(input("Enter your choice of word set:"))
        if set_ch==1:
           word_set= animals
        elif set_ch==2:
           word_set= shapes
        elif set_ch==3:
           word_set= places

    elif level== "Moderate":
        print("1. Aminal")
        print("2. Shapes")
        print("3. Places")
        set_ch= int(input("Enter your choice of word set:"))
        if set_ch==1:
           word_set= animals
        elif set_ch==2:
           word_set= shapes
        elif set_ch==3:
           word_set= places

    else:
        word_set = random.choice([animals, shapes, places])
    # Word to Guess
    secret_word = random.choice(word_set).lower()
    guessed_letters = set()
    remaining_lives = 6
    displayed_word = ["_"] * len(secret_word)

    while remaining_lives > 0:
        print(f"Word: {' '.join(displayed_word)}")
        print(f"Remaining lives: {remaining_lives}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print(f"You've already guessed {guess}")
            continue
        elif guess in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    displayed_word[i] = guess
        else:
            remaining_lives -= 1

        guessed_letters.add(guess)

        # Check if the word is completely guessed
        if "_" not in displayed_word:
            print(f"Congratulations, {player}! You've guessed the word: {secret_word}")
            return

    print(f"You've run out of lives! The word was: {secret_word}")


#Main Menu
def main():
    print("Welcome to Hangman");
    player=input("Enter your Name:")
    while True:
        print("Main Menu")
        print("1. Easy level")
        print("2. Moderate level")
        print("3. Hard level")
        print("4. About the game")
        ch=int(input("Enter your choice of Level:"))
        if ch==1:
            start("Easy", player)
        elif ch == 2:
            start("Moderate", player)
        elif ch== 3:
            start("Hard", player)
        elif ch==4:
            print("Easy : the user will be given the chance to select the list from which the random word will be selected (Animal, Shap, Place). This will make it easier to guess the secret word.")
            print("Moderate: similar to Easy, the user will be given the chance to select the set from which the random word will be selected (Animal, Plant, Place) but the number of trail will be reduced to 6.")
            print("Hard: The code will randomly select a set of words. From this set the code will randomly select a word. The uses will have no clue on the secret word. Also, the number of trails will remain at 6.")        else:
        else:
            print("Invalid choice. Please try again.")
            #continue
    
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break
# Run Game
if __name__ == "__main__":
    main()
