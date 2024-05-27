class Mutual:
    """
    Esta clase implementa una entidad Mutual.

    Ejemplo de uso:
    
    >>> mutual = Mutual()
    >>> mutual.get_credito()
    400
    >>> mutual.add_titular(Mutual.TITULAR_A)
    >>> mutual.get_credito()
    600
    >>> mutual.add_beneficiario(2)
    >>> mutual.get_consumo()
    400

    Al agregar un nuevo beneficiario 2 la empresa estaria en perdida.
    >>> mutual.add_beneficiario(2) 

    >>> mutual.get_estado_str()
    'Perdida'
    """

    # Variables de clase publicas 
    ESTADO_BALANCEADO = 0
    ESTADO_PERDIDA = 1
    ESTADO_PASIVO = 2
    ESTADO_GANANCIA = 3

    TITULAR_A = 0
    TITULAR_B = 1
    TITULAR_C = 2

    # Variables de clase privadas
    CONSUMO_BENEFICIARIO = 200.0
    MONTO_A = 200.0
    MONTO_B = 400.0
    MONTO_C = 500.0

    def __init__(self):
        self.credito = 400.0
        self.consumo = 0.0
        self.beneficiarios = 0
        self.titulares = 0
        self.estado = self.ESTADO_GANANCIA

    def add_titular(self, categoria):
        """
        Agrega un titular a la mutual.

        >>> mutual = Mutual()
        >>> mutual.add_titular(Mutual.TITULAR_A)
        >>> mutual.get_titulares()
        1
        >>> mutual.get_credito()
        600
        """
        
        if type(categoria) == int:  # Condicional agregada
            if categoria >= 0:      # Condicional agregada
                if categoria == self.TITULAR_A:
                    self.credito += self.MONTO_A
                elif categoria == self.TITULAR_B:
                    self.credito += self.MONTO_B
                elif categoria == self.TITULAR_C:
                    self.credito += self.MONTO_C
                else:
                    raise ValueError("Categoria inexistente")   # Excepcion agregada
            else:
                raise ValueError("Categoria no puede ser un numero negativo.")  # Excepcion agregada
        else:
            raise TypeError("Categoria tiene que ser de tipo int.") # Excepcion agregada
       
        self.titulares += 1
        self._calcular_estado()

    def delete_titular(self, categoria):
        if self.titulares > 0:
            if categoria == self.TITULAR_A:
                self.credito -= self.MONTO_A
            elif categoria == self.TITULAR_B:
                self.credito -= self.MONTO_B
            elif categoria == self.TITULAR_C:
                self.credito -= self.MONTO_C
            self.titulares -= 1
            self._calcular_estado()
        else:
            print("No hay titulares para eliminar.")

    def add_beneficiario(self, cantidad):
        if cantidad > 0:
            if self.estado != self.ESTADO_PERDIDA:
                if cantidad <= 3:
                    self.consumo += cantidad * self.CONSUMO_BENEFICIARIO
                    self.beneficiarios += cantidad
                    self._calcular_estado()
                else:
                    print("La cantidad debe ser <= a 3")
            else:
                print("Imposible agregar beneficiario: estado perdida")
        else:
            print("La cantidad debe ser mayor a 0")

    def delete_beneficiario(self, cantidad):
        if cantidad > 0:
            if cantidad <= 3:
                if self.beneficiarios >= cantidad:
                    self.consumo -= cantidad * self.CONSUMO_BENEFICIARIO
                    self.beneficiarios -= cantidad
                    self._calcular_estado()
                else:
                    print("La cantidad ingresada es mayor a la cantidad de beneficiarios.")
            else:
                print("La cantidad debe ser <= a 3")
        else:
            print("La cantidad debe ser mayor a 0")

    # Metodo privado
    def _calcular_estado(self):
        """
        Calcula el estado de la mutual.

        >>> mutual = Mutual()
        >>> mutual.add_titular(Mutual.TITULAR_A)
        >>> mutual._calcular_estado()
        >>> mutual.get_estado_str()
        'Ganancia'

        >>> mutual.add_beneficiario(3)
        >>> mutual.get_estado_str()
        'Balanceado'

        >>> mutual.add_beneficiario(3)
        >>> mutual.get_estado_str()
        'Perdida'
        """      

        porcentaje_consumo = self.consumo * 100 / self.credito
        diferencia_porcentual = 100 - porcentaje_consumo

        if diferencia_porcentual > 20:
            self.estado = self.ESTADO_GANANCIA
        elif 0 <= diferencia_porcentual <= 20:
            self.estado = self.ESTADO_BALANCEADO
        elif -20 <= diferencia_porcentual < 0:
            self.estado = self.ESTADO_PASIVO
        elif diferencia_porcentual < -20:
            self.estado = self.ESTADO_PERDIDA

    def get_titulares(self):
        return self.titulares

    def get_beneficiarios(self):
        return self.beneficiarios

    def get_credito(self):
        return self.credito
    
    def get_consumo(self):
        return self.consumo

    def get_estado(self):
        return self.estado
    
    def get_estado_str(self):
        if self.estado == self.ESTADO_PERDIDA:
            return "Perdida"
        elif self.estado == self.ESTADO_PASIVO:
            return "Pasivo"
        elif self.estado == self.ESTADO_BALANCEADO:
            return "Balanceado"
        elif self.estado == self.ESTADO_GANANCIA:
            return "Ganancia"
        else:
            return "Sin estado"   

    def imprimir_mutual(self):
        print("Cantidad titulares: ", self.get_titulares(), '\n'
            "Cantidad beneficiarios: ", self.get_beneficiarios(), '\n'
            "Credito: ", self.get_credito(), '\n'
            "Consumo: ", self.get_consumo(), '\n'
            "Estado actual mutual: ", self.get_estado_str(), '\n'
            )
        
