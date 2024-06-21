import tkinter as tk
from tkinter import simpledialog, messagebox
from Autor import Autor
from PIL import Image, ImageTk
from Centrar import center_window

class DevolverLibroWindow:
    def __init__(self, master, biblioteca):
        self.master = master
        self.biblioteca = biblioteca
        self.window = tk.Toplevel(master)
        self.window.title("Devolver libro")
        center_window(self.window, 300, 300)
        self.window.configure(bg="#E8EAF6")

        self.imagen = Image.open("imagenes/devolucion.png")
        self.imagen = self.imagen.resize((100, 100))
        self.imagen = ImageTk.PhotoImage(self.imagen)
        self.label_imagen = tk.Label(self.window, image=self.imagen, bg="#E8EAF6")
        self.label_imagen.pack(pady=10)

        self.label_isbn = tk.Label(self.window, text="ISBN del libro:", bg="#E8EAF6")
        self.label_isbn.pack(pady=5)
        self.entry_isbn = tk.Entry(self.window)
        self.entry_isbn.pack(pady=5)

        self.devolver_button = tk.Button(self.window, text="Devolver", command=self.devolver_libro, bg="#C5CAE9")
        self.devolver_button.pack(pady=20)

    def devolver_libro(self):
        id_libro = self.entry_isbn.get()
        libro_devuelto = self.biblioteca.devolver_libro(id_libro)
        if libro_devuelto:
            messagebox.showinfo("Información", "Libro devuelto con éxito.")
            self.window.destroy()
        else:
            messagebox.showinfo("Error", "El libro especificado no ha sido prestado.")