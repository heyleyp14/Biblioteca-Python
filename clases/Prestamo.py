class Prestamo:
  def __init__(self,libro, usuario, fecha_prestamo, fecha_devolucion):
    self.libro= libro
    self.usuario= usuario
    self.fecha_prestamo= fecha_prestamo
    self.fecha_devolucion= fecha_devolucion

  def mostrar_info(self):
     return f"Libro: {self.libro.titulo}, Usuario: {self.usuario.mostrar_info()}, Fecha de préstamo: {self.fecha_prestamo}, Fecha de devolución: {self.fecha_devolucion}"