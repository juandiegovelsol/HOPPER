import tkinter as tk
from tkinter import messagebox

class ListaComprasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Compras")
        
        self.articulos = {}
        self.articulos_comprados = {}
        
        self.crear_widgets()

    def crear_widgets(self):
        # Entradas
        self.nombre_articulo = tk.Entry(self.root)
        self.nombre_articulo.grid(row=0, column=0, padx=5, pady=5)
        self.nombre_articulo.insert(0, "Artículo")
        
        self.cantidad = tk.Entry(self.root)
        self.cantidad.grid(row=0, column=1, padx=5, pady=5)
        self.cantidad.insert(0, "Cantidad")
        
        self.presupuesto = tk.Entry(self.root)
        self.presupuesto.grid(row=0, column=2, padx=5, pady=5)
        self.presupuesto.insert(0, "Presupuesto ($)")
        
        self.agregar_btn = tk.Button(self.root, text="Agregar", command=self.agregar_articulo)
        self.agregar_btn.grid(row=0, column=3, padx=5, pady=5)

        # Lista de artículos pendientes
        self.lista_pendiente = tk.Listbox(self.root, selectmode=tk.SINGLE, width=50)
        self.lista_pendiente.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self.lista_pendiente.bind('<Double-1>', self.mover_comprado)

        # Lista de artículos comprados
        self.lista_comprada = tk.Listbox(self.root, selectmode=tk.SINGLE, width=50)
        self.lista_comprada.grid(row=1, column=2, columnspan=2, padx=5, pady=5)
        self.lista_comprada.bind('<Double-1>', self.mover_pendiente)

        # Botones de movimiento
        self.mover_a_comprado_btn = tk.Button(self.root, text="Comprar →", command=self.mover_a_comprado)
        self.mover_a_comprado_btn.grid(row=2, column=0, padx=5, pady=5)

        self.mover_a_pendiente_btn = tk.Button(self.root, text="← Devolver", command=self.mover_a_pendiente)
        self.mover_a_pendiente_btn.grid(row=2, column=1, padx=5, pady=5)

    def agregar_articulo(self):
        nombre = self.nombre_articulo.get()
        cantidad = self.cantidad.get()
        presupuesto = self.presupuesto.get()

        if not nombre or not cantidad or not presupuesto:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        try:
            self.articulos[nombre] = (cantidad, float(presupuesto))
            self.actualizar_lista_pendiente()
        except ValueError:
            messagebox.showerror("Error", "Presupuesto debe ser un número válido.")

    def actualizar_lista_pendiente(self):
        self.lista_pendiente.delete(0, tk.END)
        for nombre, (cantidad, presupuesto) in self.articulos.items():
            self.lista_pendiente.insert(tk.END, f"{nombre} - Cantidad: {cantidad} - Presupuesto: {presupuesto}")

    def mover_a_comprado(self):
        try:
            selected = self.lista_pendiente.curselection()[0]
            articulo = self.lista_pendiente.get(selected)
            self.lista_comprada.insert(tk.END, articulo)
            
            nombre = articulo.split(" - ")[0]
            del self.articulos[nombre]
            
            self.actualizar_lista_pendiente()
        except IndexError:
            messagebox.showwarning("Seleccionar artículo", "Por favor, seleccione un artículo para comprar.")

    def mover_a_pendiente(self):
        try:
            selected = self.lista_comprada.curselection()[0]
            articulo = self.lista_comprada.get(selected)
            self.lista_pendiente.insert(tk.END, articulo)
            
            nombre = articulo.split(" - ")[0]
            cantidad, presupuesto = self.articulos_comprados.pop(nombre)
            self.articulos[nombre] = (cantidad, presupuesto)
            
            self.actualizar_lista_pendiente()
        except IndexError:
            messagebox.showwarning("Seleccionar artículo", "Por favor, seleccione un artículo para devolver.")

    def mover_comprado(self, event):
        self.mover_a_comprado()

    def mover_pendiente(self, event):
        self.mover_a_pendiente()

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaComprasApp(root)
    root.mainloop()