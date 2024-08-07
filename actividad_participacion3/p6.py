# Definimos las constantes para las pintas
PINTA_CORAZON = "Corazón"
PINTA_DIAMANTE = "Diamante"
PINTA_PICA = "Pica"
PINTA_TREBOL = "Trébol"

class Carta:
    def __init__(self, valor, pinta):
    
        self.valor = valor
        self.pinta = pinta

    def __str__(self):
        return f"{self.valor} de {self.pinta}"


carta = Carta("A", PINTA_CORAZON)
print(carta) 