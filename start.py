import numpy as np
import time, random


file = open('english_words.txt', 'r')
file_content = file.read()
words_list = np.array(file_content.split('\n'))



class game():
    
    def checkup():
        global lives
        
        lives = 5      
        if lives == 0:
            print('Oh sad, you lost.')
            game.loop()
        else:
            if hidden == word:
                print('Oh hey, you won!')
                game.loop()
            else:
                letter = input("Enter your letter: ")
                word_np = np.array(list(word))
                if letter in word_np:
                    indexes = np.argwhere(word_np==letter)
                    for i in indexes:
                        hidden[i,0] = letter
                    game.checkup()
                else:
                    print("Grrr, wrong letter! You lost a life :(")
                    lives -= 1
                    game.checkup()

    def hangman():
        global word
        global hidden
          
        word = words_list[random.randint(0,len(words_list))]
        hidden = len(list(word))*'_ '
        print("Alright, you have",lives,"lives left. \n\nYour word:-",hidden)
        game.checkup()
        
        
    def main():      
        print("Welcome to the game of hangman! \nFor those who don't know what is hangman, it is a game where you guess letters for the word pre-decided by other player. Here, program will decide a word for you and you would have to guess that word. \nSounds fun, right? Play it and have fun!")
        
        game.hangman()
    
    def loop():
        
        play_again = input("Aye cool cool cool, wanna play the game again? Type 'y' to continue the game and 'n' to end the game: ")
        if (play_again=='y'):
            print('Alrightey, restarting your game in 3 seconds...')
            time.sleep(3)
            game.main()
        else:
            print('Aye hope you enjoyed the game, see ya!')
            pass
            
game.main()

    
