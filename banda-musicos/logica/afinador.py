from logica.instrumento import Instrumento

class Afinador():
  def __init__(self, musico):
      self.musico = musico
      self.instrumento = musico.instrumento

  def tocar(self):
    return self.instrumento.afinar()