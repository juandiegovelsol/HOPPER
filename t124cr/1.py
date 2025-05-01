import tkinter as tk
from tkinter import messagebox

class ListaComprasApp:
    def __init__(self, root):
        """Inicializa la aplicación y crea la interfaz de usuario."""
        self.root = root
        self.root.title("Lista de Compras")
        self._create_widgets()
        self.articulos_pendientes = [] 
        self.articulos_comprados = [] 

    def _create_widgets(self):
        """Crea los widgets de entrada y los frames para las listas."""
        self.frame_entrada = tk.Frame(self.root)
        self.frame_entrada.pack(side=tk.TOP, fill=tk.X)

        self._create_entry_widgets()
        self._create_buttons_widgets()
        self._create_listbox_widgets()

    def _create_entry_widgets(self):
        """Crea y empaqueta los widgets de entrada de datos."""
        tk.Label(self.frame_entrada, text="Artículo:").pack(side=tk.LEFT)
        self.entry_articulo = tk.Entry(self.frame_entrada)
        self.entry_articulo.pack(side=tk.LEFT)

        tk.Label(self.frame_entrada, text="Presupuesto ($):").pack(side=tk.LEFT)
        self.entry_presupuesto = tk.Entry(self.frame_entrada)
        self.entry_presupuesto.pack(side=tk.LEFT)

        tk.Label(self.frame_entrada, text="Cantidad:").pack(side=tk.LEFT)
        self.entry_cantidad = tk.Entry(self.frame_entrada)
        self.entry_cantidad.pack(side=tk.LEFT)

    def _create_buttons_widgets(self):
        """Crea y empaqueta el botón de agregar artículos."""
        self.boton_agregar = tk.Button(self.frame_entrada, text="Agregar", command=self.agregar_articulo)
        self.boton_agregar.pack(side=tk.LEFT)

    def _create_listbox_widgets(self):
        """Crea y empaqueta los Listbox para artículos pendientes y comprados."""
        self.frame_pendientes = tk.LabelFrame(self.root, text="Artículos Pendientes")
        self.frame_pendientes.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.listbox_pendientes = tk.Listbox(self.frame_pendientes, width=50)
        self.listbox_pendientes.pack(fill=tk.BOTH, expand=True)
        self.listbox_pendientes.bind('<Double-Button-1>', self.mover_a_comprados)

        self.frame_comprados = tk.LabelFrame(self.root, text="Artículos Comprados")
        self.frame_comprados.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.listbox_comprados = tk.Listbox(self.frame_comprados, width=50)
        self.listbox_comprados.pack(fill=tk.BOTH, expand=True)
        self.listbox_comprados.bind('<Double-Button-1>', self.mover_a_pendientes)

    def agregar_articulo(self):
        """Agrega un artículo a la lista de pendientes validando los datos."""
        articulo = self.entry_articulo.get().strip()
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
        """Mueve un artículo seleccionado de pendientes a comprados."""
        self._mover_articulo(self.listbox_pendientes, self.articulos_pendientes, self.articulos_comprados)

    def mover_a_pendientes(self, event):
        """Mueve un artículo seleccionado de comprados a pendientes."""
        self._mover_articulo(self.listbox_comprados, self.articulos_comprados, self.articulos_pendientes)

    def _mover_articulo(self, listbox_src, lista_src, lista_dest):
        """Mueve un artículo de una lista a otra."""
        selected_indices = listbox_src.curselection()
        if selected_indices:
            index = selected_indices[0]
            item_tuple = lista_src.pop(index)
            lista_dest.append(item_tuple)
            self.actualizar_listas()

    def actualizar_listas(self):
        """Actualiza las listas de artículos pendientes y comprados."""
        self.listbox_pendientes.delete(0, tk.END)
        self.listbox_comprados.delete(0, tk.END)

        self._fill_listbox(self.listbox_pendientes, self.articulos_pendientes)
        self._fill_listbox(self.listbox_comprados, self.articulos_comprados)

    def _fill_listbox(self, listbox, lista_articulos):
        """Llena un listbox con los artículos de la lista proporcionada."""
        for articulo_tuple in lista_articulos:
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