import random
import csv
import datetime
import mysql.connector as sqltor


mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = 'tama123', auth_plugin='mysql_native_password')
cur = mycon.cursor(buffered = True)

if mycon.is_connected():
    print("Successfully connected to MySQL Database...")
else:
    print("Error!!! Not connected to MySQL Database...")
try:
    cur.execute("create database if not exists games")
except sqltor.Error as err:
    print("Already Exists database: {}".format(err))
try:       
    cur.execute("use games")
except sqltor.Error as err:
    print("Already Used database: {}".format(err))
try:
    cur.execute("create table if not exists players(p_id varchar(10) primary key, p_name varchar(50) not null, gender char, registered_date datetime, wins int(4) default 0, loses int(4) default 0)")
except sqltor.Error as err:
    print("Error creating tables_1 : {}".format(err))
try:
    cur.execute("create table if not exists records(p_id varchar(10), team varchar(10), board_type varchar(15), result varchar(10), last_played datetime)")
except sqltor.Error as err:
    print("Error creating tables_2 : {}".format(err))
    

hangman1 = [
    [" __________"],
    ["||        |"],
    ["||        |"],
    ["||         "],
    ["||        "],
    ["||        "],
    ["||        "],
    ["||"],
    ["||____________"]
    ]

hangman2 = [
    [" __________"],
    ["||        |"],
    ["||        |"],
    ["||        O"],
    ["||        "],
    ["||         "],
    ["||        "],
    ["||"],
    ["||____________"]
    ]

hangman3 = [
    [" __________"],
    ["||        |"],
    ["||        |"],
    ["||        O"],
    ["||        |"],
    ["||        "],
    ["||        "],
    ["||"],
    ["||____________"]
    ]

hangman4 = [
    [" __________"],
    ["||        |"],
    ["||        |"],
    ["||        O"],
    ["||        |"],
    ["||        |"],
    ["||       "],
    ["||"],
    ["||____________"]
    ]

hangman5 = [
    [" __________"],
    ["||        |"],
    ["||        |"],
    ["||        O"],
    ["||        |"],
    ["||        |"],
    ["||       / "],
    ["||"],
    ["||____________"]
    ]

hangman6 = [
    [" __________"],
    ["||        |"],
    ["||        |"],
    ["||        O"],
    ["||        |"],
    ["||        |"],
    ["||       / \\"],
    ["||"],
    ["||____________"]
    ]

hangman7 = [
    [" __________"],
    ["||        |"],
    ["||        |"],
    ["||        O"],
    ["||       /|\\"],
    ["||        |"],
    ["||       / \\"],
    ["||"],
    ["||____________"]
    ]

hangman8 = [
    [" __________"],
    ["||        |"],
    ["||        |"],
    ["||       \O"],
    ["||        |"],
    ["||        |"],
    ["||       / \\"],
    ["||"],
    ["||____________"]
    ]

hangman9 = [
    [" __________"],
    ["||        |"],
    ["||        |"],
    ["||       \O/"],
    ["||        |"],
    ["||        |"],
    ["||       / \\"],
    ["||"],
    ["||____________"]
    ]

hangman10 = [
    [" __________"],
    ["||        |"],
    ["||        |"],
    ["||       \O"],
    ["||        |\\"],
    ["||        |"],
    ["||       / \\"],
    ["||"],
    ["||____________"]
    ]

hangman11 = [
    [" __________"],
    ["||        |"],
    ["||        |"],
    ["||        O"],
    ["||       /|"],
    ["||        |"],
    ["||       / \\"],
    ["||"],
    ["||____________"]
    ]


id_name1 = ""
words = []
f = open(r"C:\Users\deyta\Desktop\pokemon.csv", "r", encoding='utf-8')
csvreader = csv.reader(f)
for rec in csvreader:
    words.append([rec[30], "[ "+rec[36]+" ]"+" and "+"[ "+rec[37]+" ]"+" type"])
f.close()
words.pop(0)


amtGuesses = 7
guess_easy = [hangman1, hangman2, hangman3, hangman4, hangman5, hangman6, hangman8, hangman9, hangman10, hangman7]
guess_medium = [hangman1, hangman2, hangman3, hangman4, hangman5, hangman6, hangman11, hangman7]
guess_hard = [hangman1, hangman2, hangman4, hangman6, hangman7]
illustration_guess = guess_medium

    
def game_code(illustration_guess, amtGuesses):
    word_play, hint = random.choice(words)
    word_play = word_play.upper()
    n1, n2 = random.randint(0,len(word_play)-1), random.randint(0, len(word_play)-1)
    if n1 == n2:
        n1 = n2 + 1
    letter_flag = 0
    flag = 0
    j = 0
    list1 = []
    list2_with_clue = []
    miss_guess = []
    for i in word_play:
        if i == ' ':
            list1.append(" ")
            list2_with_clue.append(" ")
        else:
            list1.append("__")
            if (word_play[n1] == i or word_play[n2] == i) and letter_flag != 2:
                letter_flag += 1
                list2_with_clue.append(i)
            else:
                list2_with_clue.append("__")

    while True:
        choice = int(input("Do you want : 1) A clue    2) Two alphabets\nYour choice : "))
        print()
        if choice == 1:
            break
        elif choice == 2:
            list1 = list2_with_clue
            hint = "You wouldn't need a clue it seems!"
            break
        else:
            print("Give a valid choice...")
              
    while j <= amtGuesses:
        print_game(illustration_guess[j], list1, miss_guess, amtGuesses, hint)
        guess = input("\nGuess a letter or a word (Enter ! for final guess): ").upper()
        print()
        if guess == '!':
            final_word(word_play)
            flag = 1
            break
        if guess != word_play:
            if check_hangman(guess, list1, word_play, miss_guess):
                continue
            else:
                j = j+1
    if flag == 0:
        final_word(word_play)  


def final_word(word_play):
    final_guess = input("\nAny guess? (Enter N/n if you cannot guess) : ").upper()
    win = ""
    bt = ""

    if amtGuesses == 4:
        bt = "DIFFICULT"
    elif amtGuesses == 7:
        bt = "MEDIUM"
    else:
        bt = "EASY"

    print(id_name1)
        
    if final_guess == word_play:
        print("\nNice work! The word you've guessed is correct!")
        print("\n\n________H A N G M A N________\n\n")
        cur.execute("update players set wins=wins+1 where p_id = '%s'"%(id_name1,))
        cur.execute("insert into records (p_id, board_type, result, last_played) values ('%s', '%s', 'WON', now())"%(id_name1, bt))
        mycon.commit()     
    else:
        print("\nOops! The word was", word_play, ". Try again next time! Good Luck!")
        print("\n\n________H A N G M A N________\n\n")
        cur.execute("update players set loses=loses+1 where p_id = '%s'"%(id_name1,))
        cur.execute("insert into records (p_id, board_type, result, last_played) values ('%s', '%s', 'WON', now())"%(id_name1, bt))
        mycon.commit()
        

def print_game(hangman_pic, list1, miss_guess, amtGuesses, hint):
    for i, value in enumerate(hangman_pic):
        print(value[0])
    print()
    if hint == "You wouldn't need a clue it seems!":
        print("Hint : ", hint)
    else:
        print("Hint : It is a", hint, "pokemon")
    print("Word :     ",*list1)
    print("Miss :     ",', '.join(miss_guess))
    print("No. of chance(s) left is(are) : ", amtGuesses-len(miss_guess))


def check_hangman(guess, list1, word_play, miss_guess):
    c=0
    for k in range (0,len(word_play)):
        if guess == word_play[k]:
            c += 1
            print("Good! This letter is present!")
            list1[k] = guess
        else:
            continue
    if c == 0:
        print("Oops! You missed your chance!")
        miss_guess.append(guess)
        return False
    else:
        return True

for i in hangman7:
    print(*i)
print(" H A N G M A N")

while True:
    print("\n\n\nMain Menu :\n[1] Start Game\n[2] Settings\n[3] Exit")
    menu_choice = int(input("Enter a choice : "))
    print()
    if menu_choice == 1:

        br_loop1, br_loop2 = True, True
        ans1 = "proceed"
        ct = 0
        
        while br_loop1 == True or br_loop2 == True:
            player1 = input("Enter name : ")
            g1 = input("Enter gender (M/F) : ")
            g1 = g1.upper()
        
            cur.execute("select p_id, p_name from players where p_id like '%HGM%'")
            data = cur.fetchall()

            print(data)
            
            cnt = cur.rowcount

            print(cnt)
            
            for row in data:
                if player1 == row[1]:
                    print("Are you %s with player ID : %s ? (Y/N)"%(row[1], row[0]))
                    ans1 = input("Answer : ")
                    temp_id = row[0]

                    print(temp_id)
                    
                    if ans1 in "Yy":
                        br_loop1 = False
                    else:
                        br_loop1 = True
                else:
                    ct += 1
            if ct >= 0:
                br_loop1 = False

            if player1 == "":
                print("Error!!! Please enter the names again...")
                br_loop2 = True
            else:
                br_loop2 = False

        id_name1 = player1[:4].upper()+"HGM"+str(cnt)
        print(id_name1)

        if ans1 in "Yy":
            print(988887)
            id_name1 = temp_id
            print(id_name1)
        else:
            print(966664)
            cur.execute("insert into players (p_id, p_name, gender, registered_date) values ('{}','{}','{}', now())".format(id_name1, player1, g1))
            mycon.commit()
            
        game_code(illustration_guess, amtGuesses)
        
    elif menu_choice == 2:
        print("\n\n\nSettings :\nWhat would you like to set the difficulty to? :")
        print("[1] Easy\n[2] Medium\n[3] Hard\n[4] Return to Main Menu")
        difficulty = int(input("Enter a choice : "))
        if difficulty == 1:
            amtGuesses = 9
            illustration_guess = guess_easy
        elif difficulty == 2:
            amtGuesses = 7
            illustration_guess = guess_medium
        elif difficulty == 3:
            amtGuesses = 4
            illustration_guess = guess_hard
        elif difficulty == 4:
            continue
        else:
            print("\nPlease enter a valid choice")
    elif menu_choice == 3:
        break
    else: 
        print("\nPlease enter a valid choice")






    

