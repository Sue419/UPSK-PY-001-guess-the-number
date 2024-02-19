import unittest
from main import generate_random_number, human_guess

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

if __name__ == "__main__":
    unittest.main()