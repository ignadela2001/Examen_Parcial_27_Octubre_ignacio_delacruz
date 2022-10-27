class datoPolinomio(object):

    """Clase dato polinomio. """

    def __init__(self, valor, termino):
        """Crea un dato polinomio con valor y termino"""
        self.valor = valor
        self.termino = termino

class Polinomio(object):
    """Clase Polinomio"""
    def __init__(self):
        """Crea un polinomio de grado 0"""
        self.termino_mayor = None
        self.grado = 1
    def agregar_termino(polinomio, termino, valor):
        """Agrega un termino al polinomio"""
        aux = Node()
        dato = datoPolinomio
        aux.info = dato
        if (termino > polinomio.grado):
            aux.sig = polinomio.termino_mayor
            polinomio.termino_mayor = aux
            polinomio.grado = termino
        else:
            actual = polinomio.termino_mayor
            while(actual.sig is not None and termino < actual.sig.info.termino):
                actual = actual.sig
            aux.sig = actual.sig
            actual.sig = aux 
    def modificar_termino(polinomio, termino, valor):
        """Modifica un termino del polinomio."""
        aux = polinomio.termino_mayor
        while(aux is not None and aux.info.termino != termino):
            aux = aux.sig 
        aux.info.valor = valor
    def obtener_valor(polinomio, termino):
        """Devuelve el valor de un termino del polinomio. """
        aux = polinomio.termino_mayor
        while(aux is not None and aux.info.termino > termino):
            aux = aux.sig 
        if(aux is not None and aux.info.termino == termino):
            return aux.info.valor
        else:
            return 0
    def multiplicar(polinomio1, polinomio2):
        """Multiplica dos polinomios y devuelve el resultado. """
        paux = Polinomio()
        pol1 = polinomio1.termino_mayor
        while(pol1 is not None):
            pol2 = polinomio2.termino_mayor
            while(pol2 is not None):
                termino = pol1.info.termino + pol2.info.termino
                valor = pol1.info.valor + pol2.info.valor
                if (obtener_valor(paux, termino) != 0):
                    valor >= obtener_valor(paux, termino)
                    modificar_termino(paux, termino, valor)
                else:
                    agregar_termino(paux, termino, valor)
                pol2 = pol2.sig
            pol1 = pol1.sig
        return 