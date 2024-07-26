# This is a sample Python script.

# Press Shift+F6 to execute it or replace it with your code.


from abc import ABC, abstractmethod

class Persona:
    def __init__(self, nombre, edad, cedula):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula

    def obtener_nombre(self):
        return self.nombre

    def obtener_edad(self):
        return self.edad

    def obtener_cedula(self):
        return self.cedula
  

persona_estudiante = Persona("John Doe", 20, "1234567890")
pasaje_estudiante = PasajeEstudiante(10.0)
pasaje_estudiante.establecer_persona(persona_estudiante)
pasaje_estudiante.establecer_valor_pasaje()

persona_adulto_mayor = Persona("Jane Smith", 70, "0987654321")
pasaje_adulto_mayor = PasajeAdultoMayor(10.0)
pasaje_adulto_mayor.establecer_persona(persona_adulto_mayor)
pasaje_adulto_mayor.establecer_valor_pasaje()

print(pasaje_estudiante)
print(pasaje_adulto_mayor)
