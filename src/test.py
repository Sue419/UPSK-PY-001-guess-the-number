import unittest
from main import generate_random_number, human_guess, computer_guess

class TestGuessTheNumber(unittest.TestCase):

    # Test para número aleatorio 
    def test_generate_random_number(self):
        random_number = generate_random_number()

        # Verifica que el número sea entre 1 y 100
        self.assertGreaterEqual(random_number, 1)
        self.assertLessEqual(random_number, 100)

    def test_human_guess(self):
        player_number = 20
        random_number = 20
        #Función devuelve el mensaje y el valor booleano esperados
        result, success = human_guess(player_number, random_number)
        self.assertEqual(result, "¡Número correcto! Adivinaste el número")
        self.assertTrue(success)

        #Prueba para un número mayor que el número secreto
        player_number = 50
        random_number = 20
        result, success = human_guess(player_number, random_number)
        self.assertEqual(result, "Tu número es muy alto.")
        self.assertFalse(success)

        #Prueba para un número menor que el número secreto
        player_number = 5
        random_number = 20
        result, success = human_guess(player_number, random_number)
        self.assertEqual(result, "Tu número es muy bajo.")
        self.assertFalse(success)

    def test_computer_guess(self):
        random_number = 40
        computer_number = 40
        result, success = computer_guess(computer_number, random_number)
        self.assertEqual(result, "El ordenador adivina: 40. ¡Número correcto! La computadora adivinó el número")
        self.assertTrue(success)

        random_number = 40
        computer_number = 50
        result, success = computer_guess(computer_number, random_number)
        self.assertEqual(result, "El ordenador adivina: 50. El número es muy alto")
        self.assertFalse(success)

        random_number = 40
        computer_number = 30
        result, success = computer_guess(computer_number, random_number)
        self.assertEqual(result, "El ordenador adivina: 30. El número es muy bajo")
        self.assertFalse(success)

if __name__ == "__main__":
    unittest.main()