from logica.instrumento import Instrumento
from logica.guitarra import Guitarra 
from logica.bajo import Bajo
from logica.tiple import Tiple


class Musico:

  def tocar(self):
    self.instrumento.tocar()
  
  def asignar_instrumento(self, instrumento):
    self.instrumento = instrumento