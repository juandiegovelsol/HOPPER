import tkinter as tk
from tkinter import messagebox

class ListaComprasApp:
    def __init__(self, root):
        """Inicializa la aplicación y crea la interfaz de usuario."""
        self.root = root
        self.root.title("Lista de Compras")
        self._crear_widgets()
        self._configurar_layout()

    def _crear_widgets(self):
        """Crea los widgets necesarios para la aplicación."""
        self.articulos_pendientes = [] 
        self.articulos_comprados = [] 

        self.frame_entrada = tk.Frame(self.root)
        self.label_articulo = tk.Label(self.frame_entrada, text="Artículo:")
        self.entry_articulo = tk.Entry(self.frame_entrada)
        self.label_presupuesto = tk.Label(self.frame_entrada, text="Presupuesto ($):")
        self.entry_presupuesto = tk.Entry(self.frame_entrada)
        self.label_cantidad = tk.Label(self.frame_entrada, text="Cantidad:")
        self.entry_cantidad = tk.Entry(self.frame_entrada)
        
        self.boton_agregar = tk.Button(self.frame_entrada, text="Agregar", command=self.agregar_articulo)

        self.frame_pendientes = tk.LabelFrame(self.root, text="Artículos Pendientes")
        self.listbox_pendientes = tk.Listbox(self.frame_pendientes, width=50)
        self.listbox_pendientes.bind('<Double-Button-1>', self.mover_a_comprados)

        self.frame_comprados = tk.LabelFrame(self.root, text="Artículos Comprados")
        self.listbox_comprados = tk.Listbox(self.frame_comprados, width=50)
        self.listbox_comprados.bind('<Double-Button-1>', self.mover_a_pendientes)

    def _configurar_layout(self):
        """Configura el layout de la interfaz de usuario."""
        self.frame_entrada.pack(side=tk.TOP, fill=tk.X)
        self.label_articulo.pack(side=tk.LEFT)
        self.entry_articulo.pack(side=tk.LEFT)
        self.label_presupuesto.pack(side=tk.LEFT)
        self.entry_presupuesto.pack(side=tk.LEFT)
        self.label_cantidad.pack(side=tk.LEFT)
        self.entry_cantidad.pack(side=tk.LEFT)
        self.boton_agregar.pack(side=tk.LEFT)
        
        self.frame_pendientes.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.listbox_pendientes.pack(fill=tk.BOTH, expand=True)
        
        self.frame_comprados.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.listbox_comprados.pack(fill=tk.BOTH, expand=True)

    def agregar_articulo(self):
        """Agrega un artículo a la lista de pendientes validando los datos."""
        articulo = self.entry_articulo.get()
        if not articulo:
            messagebox.showerror("Error de entrada", "El nombre del artículo no puede estar vacío.")
            return
        
        try:
            presupuesto = float(self.entry_presupuesto.get())
            cantidad = int(self.entry_cantidad.get())
            
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser un entero mayor que cero.")
            if presupuesto < 0:
                raise ValueError("El presupuesto no puede ser negativo.")
            
        except ValueError as e:
            messagebox.showerror("Error de entrada", f"Datos inválidos: {e}")
            return

        item_tuple = (articulo, presupuesto, cantidad)
        self.articulos_pendientes.append(item_tuple)
        self.actualizar_listas()
        self.clear_entries()

    def mover_a_comprados(self, event):
        """Mueve un artículo seleccionado de la lista de pendientes a la lista de comprados."""
        selected_indices = self.listbox_pendientes.curselection()
        if selected_indices:
            index = selected_indices[0]
            item_tuple = self.articulos_pendientes.pop(index)
            self.articulos_comprados.append(item_tuple)
            self.actualizar_listas()

    def mover_a_pendientes(self, event):
        """Mueve un artículo seleccionado de la lista de comprados a la lista de pendientes."""
        selected_indices = self.listbox_comprados.curselection()
        if selected_indices:
            index = selected_indices[0]
            item_tuple = self.articulos_comprados.pop(index)
            self.articulos_pendientes.append(item_tuple)
            self.actualizar_listas()

    def actualizar_listas(self):
        """Actualiza las listas de artículos pendientes y comprados."""
        self.listbox_pendientes.delete(0, tk.END)
        self.listbox_comprados.delete(0, tk.END)

        for articulo_tuple in self.articulos_pendientes:
            self._agregar_item_a_listbox(self.listbox_pendientes, articulo_tuple)

        for articulo_tuple in self.articulos_comprados:
            self._agregar_item_a_listbox(self.listbox_comprados, articulo_tuple)

    def _agregar_item_a_listbox(self, listbox, articulo_tuple):
        """Agrega un artículo a un listbox en formato de visualización."""
        nombre = articulo_tuple[0]
        presupuesto = articulo_tuple[1]
        cantidad = articulo_tuple[2]
        display_string = f"{nombre} - {cantidad} unidades - ${presupuesto:.2f}"
        listbox.insert(tk.END, display_string)

    def clear_entries(self):
        """Limpia los campos de entrada de datos."""
        self.entry_articulo.delete(0, tk.END)
        self.entry_presupuesto.delete(0, tk.END)
        self.entry_cantidad.delete(0, tk.END)
        self.entry_articulo.focus_set()

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaComprasApp(root)
    root.minsize(600, 300)
    root.mainloop()