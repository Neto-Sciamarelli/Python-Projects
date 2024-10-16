#Código do jogo forca feito em Python
#Objetivo de estudos sobre a linguagem Python

import random

def hangman(word):
    wrong = 0
    stages = ["",
            "-------     ",
            "|           ",
            "|      |    ",
            "|      0    ",
            "|     /|\   ",
            "|     / \   ",
            "|           "
            ]
    
    rletters = list(word)
    board = ["--"] * len(word)
    win = False
    print("Welcome to hangman")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)

        if char in rletters:
            cind = rletters \
                .index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong+=1
        
        print(("".join(board)))
        e = wrong + 1
        print("\n"
            .join(stages[0: e]))
        
        if "--" not in board:
            print("You win!")
            print("".join(board))
            win = True
            break

    if not win:
        print("\n"
            .join(stages[0: \
            wrong]))
        print("You lose! It was {}."
            .format(word))

words = ["cat", "dog", "bird", "horse"]
num = random.randint(0, 3)
hangman(words[num])
        



