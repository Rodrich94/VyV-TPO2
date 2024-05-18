import unittest
from mutual import Mutual

class TestMutual(unittest.TestCase):
    
    def test_add_titular(self):
        mutual = Mutual()
        mutual.add_titular(Mutual.TITULAR_A)
        self.assertEqual(mutual.get_titulares(), 1)

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

    def test_add_titular(self):
        mutual = Mutual()
        mutual.add_titular(4)
        self.assertEqual(mutual.get_titulares(), 1) # cantTitulares++
        self.assertEqual(mutual.get_credito(), 400) # credito no aumenta

    def test_no_add_beneficiario(self):
        mutual = Mutual()
        with self.assertRaises(TypeError):
            mutual.add_beneficiario('a') # error. No produce una excepcion para no numerico

    
    def setUp(self): 
        self.mutual = Mutual()

    def test_todos_los_estados(self):
        mutual = Mutual()
        self.assertIsInstance(mutual, Mutual)
        with self.subTest(attribute = "test_constructor"):
            self.assertEqual(mutual.get_credito(), 400, "El credito inicial deberia ser 400") 
            self.assertEqual(mutual.get_consumo(), 0)
            self.assertEqual(mutual.get_beneficiarios(), 0)
            self.assertEqual(mutual.get_estado(), 3)

        mutual.add_beneficiario(2)
        self.assertEqual(mutual.get_estado(), 0, "El estado de la mutual deberia ser Balanceado")   

        mutual.add_beneficiario(1)
        self.assertEqual(mutual.get_estado(), 1, "El estado de la mutual deberia ser Perdida")

        mutual.add_titular(1)
        #self.assertEqual(mutual.get_credito(), 800)
        #self.assertEqual(mutual.get_titulares, 1)

        mutual.add_titular(0)
        mutual.add_beneficiario(3)
        self.assertEqual(mutual.get_estado(), 2, "El estado de la mutual deberia ser Pasivo")
        
    def test_constructor(self):
        self.assertEqual(self.mutual.get_credito(), 400) 
        self.assertEqual(self.mutual.get_consumo(), 0)
        self.assertEqual(self.mutual.get_beneficiarios(), 0)
        self.assertEqual(self.mutual.get_estado(), 3)                              
    
if __name__ == '__main__':
    unittest.main()