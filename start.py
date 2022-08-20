import numpy as np
import time
import random


file = open('english_words.txt', 'r')
file_content = file.read()
words_list = np.array(file_content.split('\n'))
print(" >> Welcome to the game of hangman! <<\nFor those who don't know what is hangman, it is a game where you guess letters for the word pre-decided by other player. Here, program will decide a word for you and you would have to guess that word. \nSounds fun, right? Play it and have fun!\n")


class game():
    def main():
        global word
        global hidden
        global list_for_hidden
        global used_letters

        word = words_list[random.randint(0, len(words_list))]
        hidden = len(list(word))*'O'
        list_for_hidden = np.array(list(hidden))
        used_letters = []
        game.hangman(5)

    def hangman(chances=5, used_letters=[]):

        hidden = "".join(list_for_hidden)
        while chances != 0:
            if hidden == word:
                print('\nOh hey, you won!')
                game.game_repeat()
                
            else:
                print("\n>> Alright, you have", chances,
                      "lives left. <<\n\n>> Your word:-", "".join(list_for_hidden), "<<")
                letter = input("Enter your letter :- ")
                word_np = np.array(list(word))
                if letter in used_letters:
                    print("Grr, try out new letters instead of reusing past ones.")
                    game.hangman(chances, used_letters)
                else:
                    used_letters.append(letter)
                    if letter in word_np:
                        indexes = np.argwhere(word_np == letter)
                        for i in indexes:
                            list_for_hidden[i] = letter
                        game.hangman(chances, used_letters)
                    else:
                        print(
                            ">> Grrr, wrong letter! You lost a life [ಠ╭╮ಠ] <<")
                        chances = chances - 1
                        game.hangman(chances, used_letters)
        else:
            print(">> Oh sad, you lost. [ಠ╭╮ಠ] << \n The word was", word)
            game.game_repeat()


    def game_repeat():
        play_again = input("Aye cool cool cool, wanna play the game again? Type 'y' to continue the game and 'n' to end the game: ")
        if (play_again == 'y'):
            print('Alrightey, restarting your game in 3 seconds...')
            time.sleep(3)
            game.main()
        else:
            print("Aye hope you enjoyed the game, see ya!")
            time.sleep(2)
            exit()

game.main()
