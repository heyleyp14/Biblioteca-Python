class Autor:
  def __init__(self,nombre, apellido):
    self.nombre= nombre
    self.apellido= apellido

  def mostrar_info(self):
        return f"{self.nombre} {self.apellido}"