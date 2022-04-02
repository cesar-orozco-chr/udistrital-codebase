from logica.instrumento import Instrumento
from logica.guitarra import Guitarra
from logica.bandola import Bandola
from logica.bajo import Bajo
from logica.tiple import Tiple
from logica.afinador import Afinador
from logica.musico import Musico
from random import choice


class Banda:
  def __init__(self) -> None:
      self.musicos = []
  
  def generar_instrumento(self):
    return choice([Guitarra(), Bajo(), Tiple(), Bandola()])

  def crear_banda(self):
    for i in range(1,5):
      self.musicos.append(Musico())
    for musico in self.musicos:
      musico.asignar_instrumento(self.generar_instrumento())

  def afinar(self):
    for musico in self.musicos:
      afinador = Afinador(musico)
      afinador.tocar()

  def tocar(self):
    for musico in self.musicos:
      musico.tocar()


