import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from Biblioteca import Biblioteca
from RegistrarLibroWindow import RegistrarLibroWindow
from RegistrarUsuarioWindow import RegistrarUsuarioWindow
from RealizarPrestamoWindow import RealizarPrestamoWindow
from DevolverLibroWindow import DevolverLibroWindow
from Centrar import center_window

class BibliotecaGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Biblioteca")
        self.master.configure(bg="#C5CAE9")  
        center_window(self.master, 400, 570)

        self.font_title = ("Roboto", 18, "bold")
        self.font_button = ("Roboto", 12)

        self.create_widgets()
        self.biblioteca = Biblioteca()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Bienvenido a la biblioteca", font=self.font_title, bg="#C5CAE9", fg="#333333")
        self.label.pack(pady=20)

        try:
            self.imagen = Image.open("imagenes/biblioteca.png")
            self.imagen = self.imagen.resize((200, 200))
            self.imagen = ImageTk.PhotoImage(self.imagen)

            self.label_imagen = tk.Label(self.master, image=self.imagen, bg="#C5CAE9")
            self.label_imagen.pack()
        except FileNotFoundError:
            print("Error: Archivo de imagen no encontrado")

        buttons_data = [
            ("Registrar libro", self.registrar_libro),
            ("Registrar usuario", self.registrar_usuario),
            ("Realizar préstamo", self.realizar_prestamo),
            ("Devolver libro", self.devolver_libro),
            ("Mostrar libros disponibles", self.mostrar_libros),
            ("Salir", self.master.quit)
        ]

        for button_text, command_func in buttons_data:
            button = tk.Button(self.master, text=button_text, width=20, command=command_func, bg="#2196F3", fg="white", font=self.font_button, activebackground="#64B5F6", bd=0)
            button.pack(pady=10, padx=20)

    def mostrar_info(self, info):
        messagebox.showinfo("Información", info)

    def registrar_libro(self):
        RegistrarLibroWindow(self.master, self.biblioteca)

    def registrar_usuario(self):
        RegistrarUsuarioWindow(self.master, self.biblioteca)

    def realizar_prestamo(self):
        RealizarPrestamoWindow(self.master, self.biblioteca)

    def devolver_libro(self):
        DevolverLibroWindow(self.master, self.biblioteca)

    def mostrar_libros(self):
        lista_libros = "\n".join(libro.mostrar_info() for libro in self.biblioteca.libros)
        self.mostrar_info(lista_libros)

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaGUI(root)
    root.mainloop()

