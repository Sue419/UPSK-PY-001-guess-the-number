"""
Modulo MAIN contiene funciones para el juego GUESS THE NUMBER.
"""
import random
import time
from colorama import Fore, Style, Back

#FUNCIONES PARA EL JUEGO GUESS THE NUMBER
def generate_random_number():
    return random.randint(1, 100)

def get_user_guess():
    while True:
        try:
            user_input = int(input('Ingrese un número entre 1 y 100: '))
            if user_input < 1 or user_input > 100:
                print("Por favor, ingrese un número válido entre 1 y 100.")
            else:
                return user_input
        except ValueError:
            print("Por favor, ingrese un número válido.")

def human_guess(player_number, random_number):
    if player_number == random_number:
        return f'¡Número correcto! Adivinaste el número', True
    elif player_number > random_number:
        return 'Tu número es muy alto.', False
    else:
        return 'Tu número es muy bajo.', False

def computer_guess(computer_number, random_number):
    if computer_number == random_number:
        return f'El ordenador adivina: {computer_number}.\n¡Número correcto! La computadora adivinó el número', True
    elif computer_number > random_number:
        return f'El ordenador adivina: {computer_number}.\nEl número es muy alto', False
    else:
        return f'El ordenador adivina: {computer_number}.\nEl número es muy bajo', False

def record_guess(guess, guess_list):
    guess_list.append(guess)

#LOGICA PARA EL JUEGO GUESS THE NUMBER
def guess_the_number():

    """
    Esta función ejecuta la lógica principal del juego. Genera un número aleatorio entre 1 y 100, 
    solicita al usuario que ingrese suposiciones, proporciona pistas sobre 
    si la suposición es demasiado alta o demasiado baja, y al final imprime los
    resultados del juego con los números que supuso el jugador y el computador.
    Retorna:
    bool: True si el jugador decide jugar de nuevo, False de lo contrario.
    """

    random_number = generate_random_number()
    print(f'\n {Fore.LIGHTBLUE_EX}{Style.BRIGHT}|------ ¡ADIVINA EL NÚMERO! -----|{Style.RESET_ALL}\n')

    player_guesses = []
    computer_guesses = []

    while True:
        time.sleep(1)
        player_number = get_user_guess()
        player_message, player_success = human_guess(player_number, random_number)
        print(f'{player_message}\n')
        record_guess(player_number, player_guesses)

        if player_success:
            break

        time.sleep(1)

        computer_number = random.randint(1, 100)
        computer_message, computer_success = computer_guess(computer_number, random_number)
        print(f'{computer_message}\n')
        record_guess(computer_number, computer_guesses)

        if computer_success:
            break

    print(f'\n{Fore.CYAN}{Style.BRIGHT}*** Resultados ***{Style.RESET_ALL}')
    print(f'{Style.DIM}Suposiciones del jugador: {player_guesses}')
    print(f'Suposiciones del computador: {computer_guesses}{Style.RESET_ALL}')

    play_again = input('\n¿Quieres jugar de nuevo? (si/no)? ')
    return play_again.lower() == 'si'

if __name__ == "__main__":
    while True:
        question_play_again = guess_the_number()
        if not question_play_again:
            break

    print(Style.BRIGHT +'\nGracias por jugar. ¡Hasta luego!\n' + Style.RESET_ALL )
