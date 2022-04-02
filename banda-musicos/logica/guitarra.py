from logica.instrumento import Instrumento

class Guitarra(Instrumento):
  def tocar(self):
    print(f"Tocando {self.__class__}")
  def afinar(self):
    print(f"Afinando {self.__class__}")