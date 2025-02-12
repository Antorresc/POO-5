import tkinter as tk
from math import pi
from PIL import Image, ImageTk

class Cilindro:
    def __init__(self, root):
        self.root = root
        self.root.title("Cilindro")

        # Cargar la imagen del cilindro
        self.imagen = Image.open(r"C:\Users\User\Documents\PROGR\QUINTAENTREGA\8.3-FIGURAS\cil.jpg")
        self.imagen = self.imagen.resize((200, 200), Image.Resampling.LANCZOS)
        self.imagen_tk = ImageTk.PhotoImage(self.imagen)

        self.imagen_label = tk.Label(root, image=self.imagen_tk)
        self.imagen_label.pack(pady=5)

        self.radio_label = tk.Label(root, text="Radio (cm):")
        self.radio_label.pack(pady=5)

        self.radio_entry = tk.Entry(root)
        self.radio_entry.pack(pady=5)

        self.altura_label = tk.Label(root, text="Altura (cm):")
        self.altura_label.pack(pady=5)

        self.altura_entry = tk.Entry(root)
        self.altura_entry.pack(pady=5)

        self.calcular_button = tk.Button(root, text="Calcular", command=self.calcular)
        self.calcular_button.pack(pady=10)

        self.resultado_label = tk.Label(root, text="")
        self.resultado_label.pack(pady=5)

    def calcular(self):
        try:
            radio = float(self.radio_entry.get())
            altura = float(self.altura_entry.get())

            volumen = pi * (radio ** 2) * altura
            area_superficial = 2 * pi * radio * (radio + altura)

            resultado = f"Volumen: {volumen:.2f} cm³\nÁrea Superficial: {area_superficial:.2f} cm²"
            self.resultado_label.config(text=resultado)
        except ValueError:
            self.resultado_label.config(text="Por favor ingrese valores válidos.")
