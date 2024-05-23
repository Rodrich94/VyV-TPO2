import unittest
from mutual.mutual import Mutual

class TestMutual(unittest.TestCase):
    
    def test_constructor(self):
        mutual = Mutual()
        self.assertEqual(mutual.get_credito(), 400, "El credito inicial deberia ser 400") 
        self.assertEqual(mutual.get_consumo(), 0)
        self.assertEqual(mutual.get_beneficiarios(), 0)
        self.assertEqual(mutual.get_estado(), 3, "El estado de la mutual deberia ser Ganancia")

    def test_add_titular(self):
        mutual = Mutual()
        mutual.add_titular(Mutual.TITULAR_A)
        self.assertEqual(mutual.get_titulares(), 1)
        self.assertEqual(mutual.get_credito(), 600)

        #Ver para caso float
        #mutual.add_titular(int(0.9))
        #self.assertEqual(mutual.get_titulares(), 2)
        #self.assertEqual(mutual.get_credito(), 500)

    def test_add_titular_categoria_no_valida(self):
        mutual = Mutual()
        mutual.add_titular(4)
        self.assertEqual(mutual.get_titulares(), 1) # cantTitulares++
        self.assertEqual(mutual.get_credito(), 400) # credito no aumenta

    def test_delete_titular(self):
        mutual = Mutual()
        mutual.add_titular(Mutual.TITULAR_A)
        mutual.delete_titular(Mutual.TITULAR_A)
        self.assertEqual(mutual.get_titulares(), 0)

    def test_add_beneficiarios_estado(self):
        mutual = Mutual()
        mutual.add_titular(Mutual.TITULAR_A)
        mutual.add_beneficiario(2)
        mutual.add_beneficiario(2)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_PERDIDA)

    def test_balanceado_estado(self):
        mutual = Mutual()
        mutual.add_titular(Mutual.TITULAR_A)
        self.assertEqual(mutual.get_titulares(),1)
        mutual.add_beneficiario(3)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_BALANCEADO)

    def test_no_add_beneficiario(self):
        mutual = Mutual()

        with self.assertRaises(TypeError):
            mutual.add_beneficiario(1.5) # error. No produce una excepcion para float
        self.assertEqual(mutual.get_consumo(), 200)
        self.assertEqual(mutual.get_beneficiarios(), 1)

        with self.assertRaises(TypeError):
            mutual.add_beneficiario('a') # error. No produce una excepcion para no numerico

    def test_todos_los_estados(self):
        mutual = Mutual()
        self.assertIsInstance(mutual, Mutual)
        with self.subTest(attribute = "test_estado_inicial"):
            self.assertEqual(mutual.get_estado(), 3, "El estado de la mutual deberia ser Ganancia")

        mutual.add_beneficiario(2)
        self.assertEqual(mutual.get_estado(), 0, "El estado de la mutual deberia ser Balanceado")   

        mutual.add_beneficiario(1)
        self.assertEqual(mutual.get_estado(), 1, "El estado de la mutual deberia ser Perdida")

        mutual.add_titular(1)

        mutual.add_titular(0)
        mutual.add_beneficiario(3)
        self.assertEqual(mutual.get_estado(), 2, "El estado de la mutual deberia ser Pasivo")
        
    def test_todos_los_eventos(self):
        mutual = Mutual()
        mutual.add_beneficiario(2)
        self.assertEqual(mutual.get_beneficiarios(), 2)
        mutual.add_titular(1)

        mutual.delete_titular(2) #Estamos eliminando un titular cat 2 inexistente (reduce el credito de mas)
        mutual.delete_beneficiario(1)

if __name__ == '__main__':
    unittest.main()