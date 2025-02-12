import tkinter as tk
from PIL import Image, ImageTk

class Prisma:
    def __init__(self, root):
        self.root = root
        self.root.title("Prisma Rectangular")

        # Cargar la imagen del prisma
        self.imagen = Image.open(r"C:\Users\User\Documents\PROGR\QUINTAENTREGA\8.3-FIGURAS\pris.jpg")
        self.imagen = self.imagen.resize((200, 200), Image.Resampling.LANCZOS)
        self.imagen_tk = ImageTk.PhotoImage(self.imagen)

        self.imagen_label = tk.Label(root, image=self.imagen_tk)
        self.imagen_label.pack(pady=5)

        self.base_label = tk.Label(root, text="Base (cm):")
        self.base_label.pack(pady=5)

        self.base_entry = tk.Entry(root)
        self.base_entry.pack(pady=5)

        self.altura_label = tk.Label(root, text="Altura (cm):")
        self.altura_label.pack(pady=5)

        self.altura_entry = tk.Entry(root)
        self.altura_entry.pack(pady=5)

        self.profundidad_label = tk.Label(root, text="Profundidad (cm):")
        self.profundidad_label.pack(pady=5)

        self.profundidad_entry = tk.Entry(root)
        self.profundidad_entry.pack(pady=5)

        self.calcular_button = tk.Button(root, text="Calcular", command=self.calcular)
        self.calcular_button.pack(pady=10)

        self.resultado_label = tk.Label(root, text="")
        self.resultado_label.pack(pady=5)

    def calcular(self):
        try:
            base = float(self.base_entry.get())
            altura = float(self.altura_entry.get())
            profundidad = float(self.profundidad_entry.get())

            volumen = base * altura * profundidad
            area_superficial = 2 * (base * altura + base * profundidad + altura * profundidad)

            resultado = f"Volumen: {volumen:.2f} cm³\nÁrea Superficial: {area_superficial:.2f} cm²"
            self.resultado_label.config(text=resultado)
        except ValueError:
            self.resultado_label.config(text="Por favor ingrese valores válidos.")
