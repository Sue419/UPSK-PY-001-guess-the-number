import random

def generate_random_number():
    return random.randint(1, 100)

def human_guess(player_number, random_number):
    if player_number == random_number:
        return '¡Número correcto! Adivinaste el número', True
    elif player_number > random_number:
        return 'Tu número es muy alto.', False
    else:
        return 'Tu número es muy bajo.', False

def computer_guess(computer_number, random_number):
    if computer_number == random_number:
        return f'El ordenador adivina: {computer_number}. ¡Número correcto! La computadora adivinó el número', True
    elif computer_number > random_number:
        return f'El ordenador adivina: {computer_number}. El número es muy alto', False
    else:
        return f'El ordenador adivina: {computer_number}. El número es muy bajo', False

def guess_the_number():

    random_number = generate_random_number()
    print("¡Adivina el número!")

    while True:
        player_number = int(input('Ingrese un número: '))
        player_message, player_success = human_guess(player_number, random_number)
        print(player_message)

        if player_success:
            break

        computer_number = random.randint(1, 100)
        computer_message, computer_success = computer_guess(computer_number, random_number)
        print(computer_message)

        if computer_success:
            break

    play_again = input('¿Quieres jugar de nuevo? (si/no)? ')
    return play_again.lower() == 'si'

#Para ejecutar el juego
if __name__ == "__main__":
  while True:
    # Jugar una partida
    play_again = guess_the_number()

    # Salir del bucle si el usuario no quiere jugar de nuevo
    if not play_again:
      break

  print("Gracias por jugar. ¡Hasta luego!")
