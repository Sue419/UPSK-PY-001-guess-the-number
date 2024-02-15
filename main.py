import random

#función randit de random. Esta función me da un número aleatorio entre 1 a 100
random_number = random.randint(1, 100)
print(random_number)

#número que ingresa el jugador
player_number = int(input('Ingrese un número: '))

while player_number != random_number:
    player_number = int(input('Número incorrecto. Ingrese nuevamente un número: '))

    if player_number == random_number:
        print('Número correcto!')

