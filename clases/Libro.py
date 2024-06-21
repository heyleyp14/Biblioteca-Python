class Libro:
  def __init__(self,titulo, isbn, autor, categoria):
    self.titulo= titulo
    self.isbn= isbn
    self.autor= autor
    self.categoria= categoria

  def mostrar_info(self):
    return f"Título: {self.titulo}, ISBN: {self.isbn}, Autor: {self.autor.mostrar_info()}, Categoría: {self.categoria.mostrar_info()}"