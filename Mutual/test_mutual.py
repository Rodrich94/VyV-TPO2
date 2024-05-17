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

    

if __name__ == '__main__':
    unittest.main()
