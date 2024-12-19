# Wordle 

#### Description: A word guessing game

## How the game works

This project is of a word guessing game based on a real internet game of the same name "Wordle". It will randomly generate 5 letter word as the word you have to guess. The player then has to input their own 5 letter word and the program will tell you which of the letters are right or wrong. The number of guesses will be determined by the user's input. If they run out of guesses before they can answer correctly, the game will tell the answer to the player and end. Alternatively, the player can press Ctrl + D to end the game prematurely. Once the player inputs their guess, it will note down any correct answer and banned letters. This process will go on until either the player runs out of tries or guesses the word correctly. When the player is correct, it will add a point to their score and asks them if they wish to continue for another round. If they answer yes, then the aforementioned process will repeat again. Otherwise, the program will print their final score and exit.


## How it was coded

In project.py, the program will use the time,random,re,requests,Figlet,and Counter modules. When the program first starts, it will open with a welcome message in a special text style using the pyfiglet module. Then, it will explain the rules of the game to the player along side asking them to input and validating their desired amount of tries. After that, it uses the get_word() to both randomly return a word from a dictionary. Next, it goes into a while loop for the number of tries and asks the player for their guess. If their guess is invalid, it will be caught by the check_input(). Everything then gets put into the check_answer(). This function will check, print, color every letter accordingly, Green, if it is correct, Yellow, if it is only in the word, Red, if it is incorrect. Then, it returns a string that includes which letter was correctly gussed. If this string is the same with the generated word, it will up the user's score by 1 and asks if they will play again. Answering "Yes" will continue the loop again. Otherwise, the system will exit. Alternatively, if the string is wrong then it goes into the format_validated_answer() that notes down which letter has been found and will carry over between the user's guesses, and another function called update_ban() which will take any letter in the guess that isn't included in the word into the banned list. And then, the loop will continue. Whenever the user wants to give up, there is an exception for an EOSError that will print the current score, and end the program the same way as if they were to run out of tries.

## How it was tested

In test_project.py, the program tests the return values of the functions used in project.py by importing them over as functions. The first test is for get_word(), which is simply tested by seeing if the return value matches a word in the online word list. Second, testing check_input(), this will test to see if the function is returning the right values when we input an invalid string into it. Next, testing check_answer() will check if the return values are properly replaced with letters when they are correct. Lastly, checking the format_validated_answer() will check if the function adds new letters to the string while not overriding the string entirely in the process.

