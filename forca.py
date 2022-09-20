import random
import os

def clear():
    os.system('CLS')

def character(hangman):
    for i in range(8):
        for j in range(1):
            print(str(hangman[i][j]))

def showmenu(chosen_word_length, completion_progress, wrong_letter_index, wrong_letter_list):
    for i in range(chosen_word_length):
            print(completion_progress[i], end=' ')

    print("\nletras erradas: ", end='')
    for i in range(wrong_letter_index):
        print(wrong_letter_list[i], end=' ')

print("BEM VINDO AO JOGO DA FORCA")
print("CATEGORIA: ANIMAIS")

hangman = [
        ["------    "],
        ["|    |    "],
        ["|         "],
        ["|         "],
        ["|         "],
        ["|         "],
        ["|         "],
        ["--        "]
]

word_bank = open("animais.txt", "r").read().splitlines()
chosen_word = random.choice(word_bank)
chosen_word_length = len(chosen_word)
completion_progress = [" "] * chosen_word_length

player_life = 7

for i in range(chosen_word_length):
    completion_progress[i] = "_"
    print(completion_progress[i], end=' ')

completion = False
total_tries = 0

checklist_chosen_word = list(chosen_word)
wrong_letter_list = ['_'] * (26 - len(checklist_chosen_word))
wrong_letter_index = 0

while completion is False:
    clear()

    showmenu(chosen_word_length, completion_progress, wrong_letter_index, wrong_letter_list)

    total_tries += 1
    print("\n")
    character(hangman)
    c_type = input("\ndigite uma letra: ").lower()

    if c_type in completion_progress or c_type in wrong_letter_list:
            print("ESSA LETRA JA FOI DIGITADA!!!")
    elif c_type in checklist_chosen_word:
        print("acertou!")

        character_repetitions = 0
        for i in range(len(checklist_chosen_word)):
            if c_type == checklist_chosen_word[i]:
                character_repetitions += 1

        if character_repetitions > 1:

            repeated_characters_position = ['-'] * character_repetitions
            character_repetitions_check = 0

            for i in range(len(checklist_chosen_word)):
                if c_type == checklist_chosen_word[i]:
                    repeated_characters_position[character_repetitions_check] = i
                    character_repetitions_check += 1
    
            for i in range(character_repetitions):
                var_index = repeated_characters_position[i]
                completion_progress[var_index] = c_type 
                checklist_chosen_word[var_index] = ' '

        else:

            x = int(chosen_word.find(c_type))
            completion_progress[x] = c_type
            checklist_chosen_word[x] = ' '
        
        for i in range(chosen_word_length):
            print(completion_progress[i], end=' ')
    
    else:
        player_life -= 1

        wrong_letter_list[wrong_letter_index] = c_type
        wrong_letter_index += 1

        if wrong_letter_index == 1:
            hangman[2] = ["|    0    "]
        elif wrong_letter_index == 2:
            hangman[3] =  ["|    |    "]
        elif wrong_letter_index == 3:
            hangman[3] = ["|   /|    "]
        elif wrong_letter_index == 4:
            hangman[3] = ["|   /|\  "]
        elif wrong_letter_index == 5:
            hangman[4] = ["|   /     "]
        elif wrong_letter_index == 6:
            hangman[4] = ["|   / \  "]
        
        showmenu(chosen_word_length, completion_progress, wrong_letter_index, wrong_letter_list)


    if player_life <= 0:
        print("\nACABARAM AS CHANCES, VOCE PERDEU")
        print("A PALAVRA ERA:", chosen_word)
        completion = True

    if completion_progress == list(chosen_word):
        completion = True
        print("VOCE ADIVINHOU EM", total_tries, "TENTATIVAS, A PALAVRA ERA:", chosen_word.upper() + "!!!")
    
    print("\n\nClique para continuar...", end='')
    teste = input() #evitar limpeza automatica da tela
