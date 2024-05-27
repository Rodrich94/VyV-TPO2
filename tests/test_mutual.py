import unittest
from mutual.mutual import Mutual

class TestMutual(unittest.TestCase):

# INICIO tests para metodo constructor

    def test_constructor_mutual(self):
        mutual = Mutual()
        self.assertEqual(mutual.get_credito(), 400) 
        self.assertEqual(mutual.get_consumo(), 0)
        self.assertEqual(mutual.get_beneficiarios(), 0)
        self.assertEqual(mutual.get_titulares(), 0)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_GANANCIA)

    def test_constructor_mutual_no_valido(self):
        mutual = Mutual()
        self.assertEqual(mutual.get_credito(), -400, "El credito inicial deberia ser 400") 
        self.assertEqual(mutual.get_consumo(), 200, "El consumo inicial deberia ser 0")
        self.assertEqual(mutual.get_beneficiarios(), 10, "La cantidad de beneficiarios inicial deberia ser 0")
        self.assertEqual(mutual.get_titulares(), 5.6, "La cantidad de titulares inicial deberia ser 0")
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_BALANCEADO, "El estado inicial de la mutual deberia ser Ganancia")

# FIN tests para metodo constructor


# INICIO tests para metodo add_titular(categoria)

    def test_add_titular(self):
        mutual = Mutual()

        # Casos de tests para titulares con categorias validas
        mutual.add_titular(Mutual.TITULAR_A)
        self.assertEqual(mutual.get_titulares(), 1)
        self.assertEqual(mutual.get_credito(), 600)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_GANANCIA)

        mutual.add_titular(Mutual.TITULAR_B)
        self.assertEqual(mutual.get_titulares(), 2)
        self.assertEqual(mutual.get_credito(), 1000)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_GANANCIA)

        mutual.add_titular(Mutual.TITULAR_C)
        self.assertEqual(mutual.get_titulares(), 3)
        self.assertEqual(mutual.get_credito(), 1500)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_GANANCIA)

        # Realizamos la comprobacion sobre el resto de variables que no deberian sufran cambios 
        self.assertEqual(mutual.get_consumo(), 0)
        self.assertEqual(mutual.get_beneficiarios(), 0)

    def test_add_titular_categoria_incorrecta(self):
        mutual = Mutual()

        # Al probar los distintos valores no admitidos para una categoria de titular,
        # se pudo observar que en la implementacion inicial faltaban controlar dichos casos

        # Al agregar un titular con categoria de tipo float
        mutual.add_titular(0.5)
        # No deberia incrementarse cantidad de titulares, sin embargo la asercion falla 
        self.assertEqual(mutual.get_titulares(), 0) # Si se cambia el valor a 1, pasa la prueba
        self.assertEqual(mutual.get_credito(), 400)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_GANANCIA)

        # Al agregar un titular con categoria negativa
        mutual.add_titular(-1)
        # No deberia incrementarse cantidad de titulares, sin embargo la asercion falla
        self.assertEqual(mutual.get_titulares(), 0)  # Si se cambia el valor a 1, pasa la prueba
        self.assertEqual(mutual.get_credito(), 400)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_GANANCIA)

        # Al agregar un titular con una categoria inexistente
        mutual.add_titular(4)
        # No deberia incrementarse cantidad de titulares, sin embargo la asercion falla
        self.assertEqual(mutual.get_titulares(), 0)  # Si se cambia el valor a 1, pasa la prueba
        self.assertEqual(mutual.get_credito(), 400)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_GANANCIA)

    def test_add_titular_no_valido(self):
        mutual = Mutual()

        # Luego de corregir los errores encontrados, definimos este test final a validar

        # Caso categoria de tipo float
        self.assertRaises(TypeError, mutual.add_titular, 0.5)

        # Caso categoria negativa
        self.assertRaises(ValueError, mutual.add_titular, -1)

        # Caso categoria inexistente 
        self.assertRaises(ValueError, mutual.add_titular, 4)
        self.assertRaises(ValueError, mutual.add_titular, 9)

        # Caso categoria de tipo char
        self.assertRaises(TypeError, mutual.add_titular, 'a')

        # Comprobamos que las variables que modifica el metodo add_titular 
        # no hayan sido alteradas
        self.assertEqual(mutual.get_titulares(), 0) 
        self.assertEqual(mutual.get_credito(), 400)

# FIN tests para metodo add_titular(categoria)


# INICIO tests para metodo delete_titular(categoria)

    def test_delete_titular(self):
        mutual = Mutual()

        # Casos de tests para titulares con categorias validas
        mutual.add_titular(Mutual.TITULAR_A)
        mutual.add_titular(Mutual.TITULAR_B)
        mutual.add_titular(Mutual.TITULAR_C)
        self.assertEqual(mutual.get_titulares(), 3)
        self.assertEqual(mutual.get_credito(), 1500)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_GANANCIA)

        mutual.delete_titular(Mutual.TITULAR_A)
        self.assertEqual(mutual.get_titulares(), 2)
        self.assertEqual(mutual.get_credito(), 1300)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_GANANCIA)

        mutual.delete_titular(Mutual.TITULAR_B)
        self.assertEqual(mutual.get_titulares(), 1)
        self.assertEqual(mutual.get_credito(), 900)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_GANANCIA)

        mutual.delete_titular(Mutual.TITULAR_C)
        self.assertEqual(mutual.get_titulares(), 0)
        self.assertEqual(mutual.get_credito(), 400)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_GANANCIA)

        # Verificamos eliminar un titular de mas
        mutual.delete_titular(Mutual.TITULAR_A)
        self.assertEqual(mutual.get_titulares(), 0)
        self.assertEqual(mutual.get_credito(), 400)

        # Realizamos la comprobacion sobre el resto de variables que no deberian sufran cambios 
        self.assertEqual(mutual.get_consumo(), 0)
        self.assertEqual(mutual.get_beneficiarios(), 0)
    

# Los tres siguientes casos son analogos a lo ocurrido con add_titular:
# test_delete_titular_categoria_float, test_delete_titular_categoria_negativa y test_delete_titular_categoria_inexistente

    def test_delete_titular_categoria_float(self):
        # Caso de test para delete_titular no valido
        mutual = Mutual()
        mutual.add_titular(Mutual.TITULAR_A)

        # Categoria de titular de tipo float no es permitida
        mutual.delete_titular(0.5)

        # Deberia seguir existiendo el titular ingresado previamente
        # La asercion falla, dado que elimina al titular de igual manera, lo cual es un comportamiento erroneo 
        self.assertEqual(mutual.get_titulares(), 1) # Si se modifica el valor a 0, pasa la prueba

        # Esto quiere decir que disminuye la cantidad de titulares pero sin actualizar el credito y estado
        self.assertEqual(mutual.get_credito(), 600)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_GANANCIA)

    def test_delete_titular_categoria_negativa(self):
        # Caso de test para delete_titular no valido
        mutual = Mutual()
        mutual.add_titular(Mutual.TITULAR_A)

        # Categoria de titular negativa no es permitida
        mutual.delete_titular(-1)

        # Deberia seguir existiendo el titular ingresado previamente
        # La asercion falla, analogamente al caso anterior 
        self.assertEqual(mutual.get_titulares(), 1) # Si se modifica el valor a 0, pasa la prueba
        self.assertEqual(mutual.get_credito(), 600)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_GANANCIA)

    def test_delete_titular_categoria_inexistente(self):
        # Caso de test para delete_titular no valido
        mutual = Mutual()
        mutual.add_titular(Mutual.TITULAR_A)

        # Categoria de titular es inexistente, no es permitida
        mutual.delete_titular(4)

        # Deberia seguir existiendo el titular ingresado previamente
        # La asercion falla, analogamente al caso anterior 
        self.assertEqual(mutual.get_titulares(), 1) # Si se modifica el valor a 0, pasa la prueba
        self.assertEqual(mutual.get_credito(), 600)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_GANANCIA)

# FIN tests para metodo delete_titular(categoria)


# INICIO tests para metodo add_beneficiario(cantidad)

    def test_add_beneficiario_estado_balanceado(self): 
        mutual = Mutual()

        # Dado que no se encuentra en estado perdida, se pueden añadir hasta dos beneficiarios
        mutual.add_beneficiario(2)
        self.assertEqual(mutual.get_beneficiarios(), 2)
        self.assertEqual(mutual.get_consumo(), 400)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_BALANCEADO)

    def test_add_beneficiario_estado_pasivo(self):
        mutual = Mutual()

        mutual.add_titular(Mutual.TITULAR_A)
        mutual.add_titular(Mutual.TITULAR_B)
        self.assertEqual(mutual.get_credito(), 1000)

        # Al agregar seis beneficiarios, nos encontramos en estado pasivo
        # 100 - (1200 * 100 / 1000) = -20%
        
        # No esta permitido con cantidad > 3, por lo tanto, lo invocamos dos veces
        mutual.add_beneficiario(3)
        mutual.add_beneficiario(3)
        self.assertEqual(mutual.get_beneficiarios(), 6)
        self.assertEqual(mutual.get_consumo(), 1200)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_PASIVO)
    
    def test_add_beneficiario_estado_perdida(self):
        mutual = Mutual()
    
        mutual.add_titular(Mutual.TITULAR_A)
        mutual.add_beneficiario(2)
        mutual.add_beneficiario(2)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_PERDIDA)

        # Al estar en estado perdida, al ingresarse un nuevo beneficiario no deberia modificarse la cantidad
        mutual.add_beneficiario(1)
        # Deberian seguir siendo cuatro:
        self.assertEqual(mutual.get_beneficiarios(), 4)

    def test_add_beneficiario_cantidad_mayor_a_tres(self): 
        mutual = Mutual()
        
        # Una de las restricciones era que no se puede agregar mas de tres beneficiarios a la vez
        mutual.add_beneficiario(4)

        # Por lo tanto, no deberian haberse ingresado
        self.assertEqual(mutual.get_beneficiarios(), 0)

    def test_add_beneficiario_cantidad_negativa(self): 
        mutual = Mutual()
        
        # La cantidad no es valida
        mutual.add_beneficiario(-1)

        # Por lo tanto, no deberian haberse ingresado
        self.assertEqual(mutual.get_beneficiarios(), 0)    

    def test_add_beneficiario_tipo_cantidad(self):
        mutual = Mutual()

        with self.assertRaises(TypeError):
            mutual.add_beneficiario(1.5) # Falla. No produce una excepcion para float
        self.assertEqual(mutual.get_consumo(), 200)
        self.assertEqual(mutual.get_beneficiarios(), 1)

        with self.assertRaises(TypeError):
            mutual.add_beneficiario('a') # Falla. No produce una excepcion para no numerico

# FIN tests para metodo add_beneficiario(cantidad)


# INICIO tests para metodo delete_beneficiario(cantidad)

# Los siguientes tests para delete_beneficiario son analogos a add_beneficiario

    def test_delete_beneficiario(self): 
        mutual = Mutual()
        mutual.add_beneficiario(3)
        
        mutual.delete_beneficiario(1)
        self.assertEqual(mutual.get_beneficiarios(), 2)
        self.assertEqual(mutual.get_consumo(), 400)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_BALANCEADO)

    def test_delete_beneficiario_cantidad_mayor_a_beneficiarios(self): 
        mutual = Mutual()
        mutual.add_beneficiario(1)

        # Se quieren eliminar mas beneficiarios de los existentes
        mutual.delete_beneficiario(3)
        # Por lo tanto, no deberian eliminarse
        self.assertEqual(mutual.get_beneficiarios(), 1)

    def test_delete_beneficiario_cantidad_mayor_a_tres(self): 
        mutual = Mutual()
        mutual.add_beneficiario(3)

        # Una de las restricciones era que no se puede hacer la operacion con mas de tres beneficiarios a la vez
        mutual.delete_beneficiario(4)
        # Por lo tanto, no deberian haberse eliminado
        self.assertEqual(mutual.get_beneficiarios(), 3)

    def test_delete_beneficiario_cantidad_cero(self): 
        mutual = Mutual()
        mutual.add_beneficiario(3)

        # La cantidad no es valida
        mutual.delete_beneficiario(0)
        # Por lo tanto, no deberia haberse eliminado
        self.assertEqual(mutual.get_beneficiarios(), 3)    

    def test_delete_beneficiario_cantidad_negativa(self): 
        mutual = Mutual()
        mutual.add_beneficiario(1)

        # La cantidad no es valida
        mutual.delete_beneficiario(-1)
        # Por lo tanto, no deberia haberse eliminado
        self.assertEqual(mutual.get_beneficiarios(), 1)    

    def test_delete_beneficiario_tipo_cantidad(self):
        mutual = Mutual()

        with self.assertRaises(TypeError):
            mutual.delete_beneficiario(1.5) # Falla. No produce una excepcion para float
        self.assertEqual(mutual.get_consumo(), 200)
        self.assertEqual(mutual.get_beneficiarios(), 1)

        with self.assertRaises(TypeError):
            mutual.delete_beneficiario('a') # Falla. No produce una excepcion para no numerico

# FIN tests para metodo delete_beneficiario(cantidad)


# INICIO tests para metodo _calcular_estado()

    def test_calcular_estado_ganancia(self):
        mutual = Mutual()
        mutual.add_beneficiario(2)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_BALANCEADO)
        mutual.add_titular(Mutual.TITULAR_C)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_GANANCIA)

    def test_calcular_estado_balanceado(self):
        mutual = Mutual()
        mutual.add_titular(Mutual.TITULAR_A)
        self.assertEqual(mutual.get_titulares(), 1)
        mutual.add_beneficiario(3)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_BALANCEADO)

    def test_calcular_estado_pasivo(self):
        mutual = Mutual()
        mutual.add_titular(Mutual.TITULAR_A)
        mutual.add_titular(Mutual.TITULAR_B)
        mutual.add_beneficiario(3)
        mutual.add_beneficiario(3)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_PASIVO)
    
    def test_calcular_estado_perdida(self):
        mutual = Mutual()
        mutual.add_titular(Mutual.TITULAR_A)
        self.assertEqual(mutual.get_titulares(), 1)
        mutual.add_beneficiario(3)
        mutual.add_beneficiario(3)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_PERDIDA)

# FIN tests para metodo calcular_estado()


# INICIO tests derivados del Testing de Estados

    def test_todos_los_estados(self):
        mutual = Mutual()
        self.assertIsInstance(mutual, Mutual)

        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_GANANCIA, "El estado de la mutual deberia ser Ganancia")

        mutual.add_beneficiario(2)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_BALANCEADO, "El estado de la mutual deberia ser Balanceado")   

        mutual.add_beneficiario(1)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_PERDIDA, "El estado de la mutual deberia ser Perdida")

        mutual.add_titular(1)
        mutual.add_titular(0)
        mutual.add_beneficiario(3)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_PASIVO, "El estado de la mutual deberia ser Pasivo")
        
    def test_todos_los_eventos(self):
        mutual = Mutual()
        mutual.add_titular(1)
        mutual.get_credito()
        mutual.add_beneficiario(2)
        mutual.get_consumo()
        mutual.get_estado()
        mutual.delete_titular(2) # Estamos eliminando un titular cat 2 inexistente (reduce el credito de mas)
        mutual.get_titulares()
        mutual.delete_beneficiario(1)
        mutual.get_beneficiarios()
        mutual.get_estado_str()

    def test_todas_las_acciones(self):
        mutual = Mutual()
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_GANANCIA)

        mutual.add_beneficiario(0)
        mutual.add_beneficiario(1)
        mutual.add_beneficiario(2)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_PERDIDA)
        mutual.add_beneficiario(3)
        mutual.add_beneficiario(4)

        mutual.delete_beneficiario(0)
        mutual.delete_beneficiario(1)
        mutual.delete_beneficiario(2)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_GANANCIA)
        mutual.delete_beneficiario(3)
        mutual.delete_beneficiario(4)

        mutual.add_titular(Mutual.TITULAR_A)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_GANANCIA)   
        mutual.add_titular(Mutual.TITULAR_B)
        mutual.add_titular(Mutual.TITULAR_C)
        #mutual.add_titular(Mutual.TITULAR_D)
        
        mutual.delete_titular(Mutual.TITULAR_A)
        mutual.delete_titular(Mutual.TITULAR_B)
        mutual.delete_titular(Mutual.TITULAR_C)
        self.assertEqual(mutual.get_estado(), Mutual.ESTADO_GANANCIA)
# FIN tests derivados del Testing de Estados

if __name__ == '__main__':
    unittest.main()