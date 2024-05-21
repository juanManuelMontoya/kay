import tkinter as tk
from tkinter import ttk
from AnalizadorLexico import AnalizadorLexico

class InterfazGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("Kay")

        self.text_area = tk.Text(self.root, height=20, width=60)
        self.text_area.pack()

        self.boton_analizar = tk.Button(self.root, text="Analizar", command=self.analizar_codigo)
        self.boton_analizar.pack()

        self.tabla_tokens = ttk.Treeview(self.root, columns=("Lexema", "Categoría", "Posición"), show="headings")
        self.tabla_tokens.heading("Lexema", text="Lexema")
        self.tabla_tokens.heading("Categoría", text="Categoría")
        self.tabla_tokens.heading("Posición", text="Posición")
        self.tabla_tokens.pack()

    def analizar_codigo(self):
        codigo = self.text_area.get("1.0", tk.END)
        analizador = AnalizadorLexico(codigo)
        analizador.analizar()
        self.tabla_tokens.delete(*self.tabla_tokens.get_children())
        for token in analizador.obtener_tokens():
            self.tabla_tokens.insert("", tk.END, values=token)

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazGrafica(root)
    root.mainloop()