import tkinter as tk
from PIL import Image, ImageTk

class Cubo:
    def __init__(self, root):
        self.root = root
        self.root.title("Cubo")

        # Cargar la imagen del cubo
        self.imagen = Image.open(r"C:\Users\User\Documents\PROGR\QUINTAENTREGA\8.3-FIGURAS\cub.jpg")
        self.imagen = self.imagen.resize((200, 200), Image.Resampling.LANCZOS)
        self.imagen_tk = ImageTk.PhotoImage(self.imagen)

        self.imagen_label = tk.Label(root, image=self.imagen_tk)
        self.imagen_label.pack(pady=5)

        self.lado_label = tk.Label(root, text="Lado (cm):")
        self.lado_label.pack(pady=5)

        self.lado_entry = tk.Entry(root)
        self.lado_entry.pack(pady=5)

        self.calcular_button = tk.Button(root, text="Calcular", command=self.calcular)
        self.calcular_button.pack(pady=10)

        self.resultado_label = tk.Label(root, text="")
        self.resultado_label.pack(pady=5)

    def calcular(self):
        try:
            lado = float(self.lado_entry.get())

            volumen = lado ** 3
            area_superficial = 6 * (lado ** 2)

            resultado = f"Volumen: {volumen:.2f} cm³\nÁrea Superficial: {area_superficial:.2f} cm²"
            self.resultado_label.config(text=resultado)
        except ValueError:
            self.resultado_label.config(text="Por favor ingrese valores válidos.")
