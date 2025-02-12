
import tkinter as tk
from cilindro import Cilindro
from esfera import Esfera
from piramide import Piramide
from cubo import Cubo
from prisma import Prisma

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Selecciona una figura")

        # Etiqueta de bienvenida
        self.titulo_label = tk.Label(root, text="Selecciona una figura para calcular", font=("Arial", 14))
        self.titulo_label.pack(pady=10)

        # Botón para Cilindro
        self.boton_cilindro = tk.Button(root, text="Cilindro", command=self.abrir_cilindro)
        self.boton_cilindro.pack(pady=5)

        # Botón para Esfera
        self.boton_esfera = tk.Button(root, text="Esfera", command=self.abrir_esfera)
        self.boton_esfera.pack(pady=5)

        # Botón para Pirámide
        self.boton_piramide = tk.Button(root, text="Pirámide", command=self.abrir_piramide)
        self.boton_piramide.pack(pady=5)

        # Botón para Cubo
        self.boton_cubo = tk.Button(root, text="Cubo", command=self.abrir_cubo)
        self.boton_cubo.pack(pady=5)

        # Botón para Prisma Rectangular
        self.boton_prisma = tk.Button(root, text="Prisma Rectangular", command=self.abrir_prisma)
        self.boton_prisma.pack(pady=5)

    def abrir_cilindro(self):
        nueva_ventana = tk.Toplevel(self.root)
        Cilindro(nueva_ventana)

    def abrir_esfera(self):
        nueva_ventana = tk.Toplevel(self.root)
        Esfera(nueva_ventana)

    def abrir_piramide(self):
        nueva_ventana = tk.Toplevel(self.root)
        Piramide(nueva_ventana)

    def abrir_cubo(self):
        nueva_ventana = tk.Toplevel(self.root)
        Cubo(nueva_ventana)

    def abrir_prisma(self):
        nueva_ventana = tk.Toplevel(self.root)
        Prisma(nueva_ventana)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
