# This is a sample Python script.

# Press Shift+F6 to execute it or replace it with your code.

class PasajeUrbano(ABC):
    
    def __init__(self, pasaje_fijo):
        self.valor_fijo = pasaje_fijo
        self.usuario = None
        self.valor_pasaje = 0.0
    
    def establecer_persona(self, u, fijo=None):
        self.usuario = u
        if fijo is not None:
            self.valor_fijo = fijo

    def obtener_persona(self):
        return self.usuario
    
    def establecer_valor_fijo(self, p):
        self.valor_fijo = p
    
    def obtener_valor_fijo(self):
        return self.valor_fijo
    
    @abstractmethod
    def establecer_valor_pasaje(self):
        pass
    
    def obtener_valor_pasaje(self):
        return self.valor_pasaje
    
    def __str__(self):
        return (f"Pasajero: {self.obtener_persona().obtener_nombre()}\n"
                f"Edad: {self.obtener_persona().obtener_edad()}\n"
                f"Cédula: {self.obtener_persona().obtener_cedula()}\n"
                f"Valor Pasaje: {self.obtener_valor_pasaje():.2f}\n"
                "---------------------\n")


class PasajeEstudiante(PasajeUrbano):
    def establecer_valor_pasaje(self):
        self.valor_pasaje = self.valor_fijo * 0.5  

class PasajeAdultoMayor(PasajeUrbano):
    def establecer_valor_pasaje(self):
        self.valor_pasaje = self.valor_fijo * 0.3