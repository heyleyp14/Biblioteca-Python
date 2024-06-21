import tkinter as tk
from tkinter import simpledialog, messagebox
from Autor import Autor
from Categoria import Categoria
from Libro import Libro
from PIL import Image, ImageTk
from Centrar import center_window


class RegistrarLibroWindow:
    def __init__(self, master, biblioteca):
        self.master = master
        self.biblioteca = biblioteca
        self.window = tk.Toplevel(master)
        self.window.title("Registrar libro")
        center_window(self.window, 300, 500)
        self.window.configure(bg="#E8EAF6")

        self.imagen = Image.open("imagenes/registro.png")
        self.imagen = self.imagen.resize((100, 100))
        self.imagen = ImageTk.PhotoImage(self.imagen)
        self.label_imagen = tk.Label(self.window, image=self.imagen, bg="#E8EAF6")
        self.label_imagen.pack(pady=10)

        self.label_titulo = tk.Label(self.window, text="Título:", bg="#E8EAF6")
        self.label_titulo.pack(pady=5)
        self.entry_titulo = tk.Entry(self.window)
        self.entry_titulo.pack(pady=5)

        self.label_isbn = tk.Label(self.window, text="ISBN:", bg="#E8EAF6")
        self.label_isbn.pack(pady=5)
        self.entry_isbn = tk.Entry(self.window)
        self.entry_isbn.pack(pady=5)

        self.label_autor_nombre = tk.Label(self.window, text="Nombre del autor:", bg="#E8EAF6")
        self.label_autor_nombre.pack(pady=5)
        self.entry_autor_nombre = tk.Entry(self.window)
        self.entry_autor_nombre.pack(pady=5)

        self.label_autor_apellido = tk.Label(self.window, text="Apellido del autor:", bg="#E8EAF6")
        self.label_autor_apellido.pack(pady=5)
        self.entry_autor_apellido = tk.Entry(self.window)
        self.entry_autor_apellido.pack(pady=5)

        self.label_categoria = tk.Label(self.window, text="Categoría:", bg="#E8EAF6")
        self.label_categoria.pack(pady=5)
        self.entry_categoria = tk.Entry(self.window)
        self.entry_categoria.pack(pady=5)

        self.registrar_button = tk.Button(self.window, text="Registrar", command=self.registrar_libro, bg="#C5CAE9")
        self.registrar_button.pack(pady=20)

    def registrar_libro(self):
        titulo = self.entry_titulo.get()
        isbn = self.entry_isbn.get()
        autor_nombre = self.entry_autor_nombre.get()
        autor_apellido = self.entry_autor_apellido.get()
        categoria_nombre = self.entry_categoria.get()

        autor = Autor(autor_nombre, autor_apellido)
        categoria = Categoria(categoria_nombre)
        libro = Libro(titulo, isbn, autor, categoria)

        self.biblioteca.registrar_libro(libro)
        messagebox.showinfo("Información", "Libro registrado con éxito.")
        self.window.destroy()