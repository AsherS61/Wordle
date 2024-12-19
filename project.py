import time,random,re,requests
from pyfiglet import Figlet
from collections import Counter

def main():

    #Intro
    f = Figlet(font='slant')
    print (f.renderText("Welcome To Wordle!"))
    time.sleep(1)
    print("\033[0;37;40mYou will have a chosen amount of chances to guess a 5 letter word\033[0;37;40m")
    time.sleep(1)
    print("If the letter turns \033[1;32;40mGreen\033[0;37;40m, it is in the correct position.\nIf a letter of your word is included in the answer,but in the wrong position, it will turn \033[1;33;40mYellow\033[0;37;40m.\nOtherwise,it will turn \033[1;31;40mRed\033[0;37;40m.")
    time.sleep(2)

    score = 0
    while True:
        tries = input("How many tries do you want? ")
        if tries.isnumeric():
            break

    while True:
        #Variables
        word = get_word().lower()
        format = "_____"
        ban_list = set()

        #Game Functions
        try:
            i = 0
            while i < int(tries):
                if i > 5:
                    print("Press Ctrl+D to Give up")

                while True:
                    user_input = input("\nEnter a word: ").lower()
                    if check_input(user_input) == True:
                        break
                    else:
                        print(check_input(user_input))

                answer = check_answer(word, user_input, format)
                format = format_validated_answer(answer,format)
                ban_list = update_ban(word, user_input, ban_list)


                #Output After Gussed
                if answer.lower() == word:
                    score += 1
                    print(f"\nYou guessed correctly! \nScore: {score}")
                    break
                print(f"\nFOUND: \033[2;37;40m{format}\033[0;37;40m \nBANNED: \033[1;31;40m{sorted(ban_list)}\033[0;37;40m")
                i += 1

            else:
                print(f"\nRan out of tries, the answer was {word}. \nYour final score is {score}.")
                exit()

        #User gives up
        except EOFError:
            print(f"\nThe Answer was {word}. Your Final Score is {score}.")
            exit()


        #One more round
        while True:
            one_more = input("\nDo you wish to play one more round? \nEnter: Yes or No \n")
            if one_more.lower() in ('no','n'):
                print(f"Your Final Score is {score}")
                exit()
            elif one_more.lower() in ('y','yes'):
                break
            else:
                print("Invalid")


def get_word():

    #Choosing the word

    word_list = requests.get("https://gist.github.com/shmookey/b28e342e1b1756c4700f42f17102c2ff")
    list = re.findall(r'class=\"blob-code blob-code-inner js-file-line\">(\w+)<\/td>', word_list.text)

    return random.choice(list)



def check_input(x):

    #aalidate input
    if x.isalpha() == False:
        return "Only alphabets are allowed"
    elif len(x) != 5:
        return "Must be five letters"
    else:
        return True


def check_answer(word, input, format):

    #Split strings into a list of containing each character
    word_split,input_split,format_split  = [*word],[*input],[*format]
    counter_word = Counter(word)
    counter_inputed = Counter()
    for i in range(0,5):


        #Capitalize First Letter
        if i == 0:
            input_split[i] = input_split[i].upper()
            word_split[i] = word_split[i].upper()

        #Coloring Answers
        if input_split[i] == word_split[i]:
            format_split[i] = input_split[i]
            print(f"\033[1;32;40m{input_split[i]}\033[0;37;40m",end=" ")
            counter_inputed.update(input_split[i])
        elif (input_split[i].lower() in word) and (counter_inputed[input_split[i]] <= counter_word[input_split[i]]):
            print(f"\033[1;33;40m{input_split[i]}\033[0;37;40m",end=" ")
            counter_inputed.update(input_split[i])
        else:
            print(f"\033[1;31;40m{input_split[i]}\033[0;37;40m",end=" ")
            counter_inputed.update(input_split[i])


    ans = "".join(format_split)
    return ans


def format_validated_answer(ans,format):

    #Formating known letters
    ans_split,format_split = [*ans], [*format]
    for i in range(0,5):
        if format_split[i] == "_":
            format_split[i] = ans_split[i]
    format = "".join(format_split)

    return format


def update_ban(word, user_input, ban):

    for i in range(0,5):

        #Get Banned Words
        if user_input[i] not in word:
            ban.add(user_input[i])

    return ban


if __name__ == "__main__":
    main()
