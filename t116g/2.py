import tkinter as tk
from tkinter import messagebox

class ListaComprasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Compras")
        
        self.articulos_pendientes = []  # Lista de artículos no comprados
        self.articulos_comprados = []   # Lista de artículos comprados

        # Entradas para artículo, presupuesto y cantidad
        self.frame_entrada = tk.Frame(self.root)
        self.frame_entrada.pack(side=tk.TOP, fill=tk.X)

        self.label_articulo = tk.Label(self.frame_entrada, text="Artículo:")
        self.label_articulo.pack(side=tk.LEFT)
        self.entry_articulo = tk.Entry(self.frame_entrada)
        self.entry_articulo.pack(side=tk.LEFT)

        self.label_presupuesto = tk.Label(self.frame_entrada, text="Presupuesto ($):")
        self.label_presupuesto.pack(side=tk.LEFT)
        self.entry_presupuesto = tk.Entry(self.frame_entrada)
        self.entry_presupuesto.pack(side=tk.LEFT)

        self.label_cantidad = tk.Label(self.frame_entrada, text="Cantidad:")
        self.label_cantidad.pack(side=tk.LEFT)
        self.entry_cantidad = tk.Entry(self.frame_entrada)
        self.entry_cantidad.pack(side=tk.LEFT)

        self.boton_agregar = tk.Button(self.frame_entrada, text="Agregar", command=self.agregar_articulo)
        self.boton_agregar.pack(side=tk.LEFT)

        # Listbox de artículos pendientes
        self.frame_pendientes = tk.LabelFrame(self.root, text="Artículos Pendientes")
        self.frame_pendientes.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.listbox_pendientes = tk.Listbox(self.frame_pendientes, width=50)
        self.listbox_pendientes.pack(fill=tk.BOTH, expand=True)
        self.listbox_pendientes.bind('<Double-Button-1>', self.mover_a_comprados)

        # Listbox de artículos comprados
        self.frame_comprados = tk.LabelFrame(self.root, text="Artículos Comprados")
        self.frame_comprados.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.listbox_comprados = tk.Listbox(self.frame_comprados, width=50)
        self.listbox_comprados.pack(fill=tk.BOTH, expand=True)
        self.listbox_comprados.bind('<Double-Button-1>', self.mover_a_pendientes)

    def agregar_articulo(self):
        articulo = self.entry_articulo.get()
        try:
            presupuesto = float(self.entry_presupuesto.get())
            cantidad = int(self.entry_cantidad.get())
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor que cero.")
        except ValueError as e:
            messagebox.showerror("Error de entrada", f"Datos inválidos: {e}")
            return

        self.articulos_pendientes.append((articulo, presupuesto, cantidad))
        self.actualizar_listas()
        self.clear_entries()

    def mover_a_comprados(self, event):
        selected = self.listbox_pendientes.curselection()
        if selected:
            articulo = self.listbox_pendientes.get(selected[0])
            self.articulos_comprados.append(articulo)
            self.articulos_pendientes.remove(articulo)
            self.actualizar_listas()

    def mover_a_pendientes(self, event):
        selected = self.listbox_comprados.curselection()
        if selected:
            articulo = self.listbox_comprados.get(selected[0])
            self.articulos_pendientes.append(articulo)
            self.articulos_comprados.remove(articulo)
            self.actualizar_listas()

    def actualizar_listas(self):
        self.listbox_pendientes.delete(0, tk.END)
        self.listbox_comprados.delete(0, tk.END)

        for articulo in self.articulos_pendientes:
            self.listbox_pendientes.insert(tk.END, f"{articulo[0]} - {articulo[2]} unidades - ${articulo[1]}")

        for articulo in self.articulos_comprados:
            self.listbox_comprados.insert(tk.END, f"{articulo[0]} - {articulo[2]} unidades - ${articulo[1]}")

    def clear_entries(self):
        self.entry_articulo.delete(0, tk.END)
        self.entry_presupuesto.delete(0, tk.END)
        self.entry_cantidad.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaComprasApp(root)
    root.mainloop()