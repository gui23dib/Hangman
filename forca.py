import random
import os

def clear():
    os.system('CLS')

def character():
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

    for i in range(8):
        print(hangman[i])


print("BEM VINDO AO JOGO DA FORCA")
print("CATEGORIA: ANIMAIS")

word_bank = ["macaco", "elefante", "tigre", "urso", "lobo", "cachorro", "gato"]
chosen_word = random.choice(word_bank)
chosen_word_length = len(chosen_word)
completion_progress = [" "] * chosen_word_length

player_life = 5

for i in range(chosen_word_length):
    completion_progress[i] = "_ "
    print(completion_progress[i], end='')

completion = False

checklist_chosen_word = list(chosen_word)
wrong_letter_list = ['_'] * (26 - len(checklist_chosen_word))
wrong_letter_index = 0

while completion is False:
    #clear()
    print("\n")
    character()
    c_type = input("\ndigite uma letra: ")
    c_type = c_type.lower()
    if c_type in checklist_chosen_word:
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
        
        print(completion_progress)
    
    else:
        player_life -= 1

        wrong_letter_list[wrong_letter_index] = c_type
        wrong_letter_index += 1

        print("letras erradas: ", end='')
        for i in range(wrong_letter_index):
            print(wrong_letter_list[i], end=' ')

    
    if player_life <= 0:
        print("ACABARAM AS CHANCES, VOCE PERDEU")
        completion = True

    if completion_progress == list(chosen_word):
        completion = True
        print("VOCE ADIVINHOU A PALAVRA!!!")
    
    #teste = input() #evitar limpeza automatica da tela
