import tkinter as tk
from tkinter import simpledialog, messagebox
from Autor import Autor
from Prestamo import Prestamo
from PIL import Image, ImageTk
from Centrar import center_window

class RealizarPrestamoWindow:
    def __init__(self, master, biblioteca):
        self.master = master
        self.biblioteca = biblioteca
        self.window = tk.Toplevel(master)
        self.window.title("Realizar préstamo")
        center_window(self.window, 300, 500)
        self.window.configure(bg="#E8EAF6")

        self.imagen = Image.open("imagenes/prestamo.png")
        self.imagen = self.imagen.resize((100, 100))
        self.imagen = ImageTk.PhotoImage(self.imagen)
        self.label_imagen = tk.Label(self.window, image=self.imagen, bg="#E8EAF6")
        self.label_imagen.pack(pady=10)

        self.label_isbn = tk.Label(self.window, text="ISBN del libro:", bg="#E8EAF6")
        self.label_isbn.pack(pady=5)
        self.entry_isbn = tk.Entry(self.window)
        self.entry_isbn.pack(pady=5)

        self.label_id_usuario = tk.Label(self.window, text="ID del usuario:", bg="#E8EAF6")
        self.label_id_usuario.pack(pady=5)
        self.entry_id_usuario = tk.Entry(self.window)
        self.entry_id_usuario.pack(pady=5)

        self.label_fecha_prestamo = tk.Label(self.window, text="Fecha de préstamo (Dia/Mes/Año):", bg="#E8EAF6")
        self.label_fecha_prestamo.pack(pady=5)
        self.entry_fecha_prestamo = tk.Entry(self.window)
        self.entry_fecha_prestamo.pack(pady=5)

        self.label_fecha_devolucion = tk.Label(self.window, text="Fecha de devolución (Dia/Mes/Año):", bg="#E8EAF6")
        self.label_fecha_devolucion.pack(pady=5)
        self.entry_fecha_devolucion = tk.Entry(self.window)
        self.entry_fecha_devolucion.pack(pady=5)

        self.realizar_button = tk.Button(self.window, text="Realizar", command=self.realizar_prestamo, bg="#C5CAE9")
        self.realizar_button.pack(pady=20)

    def realizar_prestamo(self):
        id_libro = self.entry_isbn.get()
        id_usuario = self.entry_id_usuario.get()
        fecha_prestamo = self.entry_fecha_prestamo.get()
        fecha_devolucion = self.entry_fecha_devolucion.get()

        libro_prestamo = self.biblioteca.buscar_libro_por_isbn(id_libro)
        usuario_prestamo = self.biblioteca.buscar_usuario_por_id(id_usuario)

        if libro_prestamo and usuario_prestamo:
            prestamo = Prestamo(libro_prestamo, usuario_prestamo, fecha_prestamo, fecha_devolucion)
            self.biblioteca.realizar_prestamo(prestamo)
            messagebox.showinfo("Información", "Préstamo realizado con éxito.")
            self.window.destroy()
        else:
            messagebox.showinfo("Error", "El libro o usuario especificado no existe.")