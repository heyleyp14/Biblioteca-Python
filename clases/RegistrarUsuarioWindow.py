import tkinter as tk
from tkinter import simpledialog, messagebox
from Usuario import Usuario
from PIL import Image, ImageTk
from Centrar import center_window

class RegistrarUsuarioWindow:
    def __init__(self, master, biblioteca):
        self.master = master
        self.biblioteca = biblioteca
        self.window = tk.Toplevel(master)
        self.window.title("Registrar usuario")
        center_window(self.window, 300, 400)
        self.window.configure(bg="#E8EAF6")

        self.imagen = Image.open("imagenes/usuario.png")
        self.imagen = self.imagen.resize((100, 100))
        self.imagen = ImageTk.PhotoImage(self.imagen)
        self.label_imagen = tk.Label(self.window, image=self.imagen, bg="#E8EAF6")
        self.label_imagen.pack(pady=10)

        self.label_nombre = tk.Label(self.window, text="Nombre:", bg="#E8EAF6")
        self.label_nombre.pack(pady=5)
        self.entry_nombre = tk.Entry(self.window)
        self.entry_nombre.pack(pady=5)

        self.label_apellido = tk.Label(self.window, text="Apellido:", bg="#E8EAF6")
        self.label_apellido.pack(pady=5)
        self.entry_apellido = tk.Entry(self.window)
        self.entry_apellido.pack(pady=5)

        self.label_id = tk.Label(self.window, text="ID del usuario:", bg="#E8EAF6")
        self.label_id.pack(pady=5)
        self.entry_id = tk.Entry(self.window)
        self.entry_id.pack(pady=5)

        self.registrar_button = tk.Button(self.window, text="Registrar", command=self.registrar_usuario, bg="#C5CAE9")
        self.registrar_button.pack(pady=20)

    def registrar_usuario(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        id_usuario = self.entry_id.get()

        usuario = Usuario(nombre, apellido, id_usuario)
        self.biblioteca.registrar_usuario(usuario)
        messagebox.showinfo("Información", "Usuario registrado con éxito.")
        self.window.destroy()