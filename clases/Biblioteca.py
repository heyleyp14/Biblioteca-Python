class Biblioteca:
  def __init__(self):
    self.libros= []
    self.usuarios= []
    self.prestamos= []


  def registrar_libro(self, libro):
    self.libros.append(libro)

  def registrar_usuario(self, usuario):
    self.usuarios.append(usuario)

  def realizar_prestamo(self, prestamo):
    self.prestamos.append(prestamo)

  def devolver_libro(self, prestamo):
    self.prestamos.remove(prestamo)

  def mostrar_libros(self):
    for libro in self.libros:
        print(libro.mostrar_info())

  def buscar_libro_por_isbn(self, isbn):
    for libro in self.libros:
        if libro.isbn == isbn:
            return libro
    return None
  
  def buscar_usuario_por_id(self, id_usuario):
      for usuario in self.usuarios:
          if usuario.id_usuario == id_usuario:
              return usuario
      return None
  
  def devolver_libro(self, id_libro):
        prestamo_devuelto = False
        for prestamo in self.prestamos:
            if prestamo.libro.isbn == id_libro:
                self.prestamos.remove(prestamo)
                prestamo_devuelto = True
                break
        return prestamo_devuelto
