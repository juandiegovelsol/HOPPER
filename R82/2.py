class GestorUsuarios:
    def __init__(self):
        self.usuarios = []
        self.ultimo_id = 0

    def agregar_usuario(self, nombre, edad):
        if not nombre or edad <= 0:
            raise ValueError("El nombre no puede ser vacío y la edad debe ser un número positivo.")
        
        self.ultimo_id += 1
        usuario = {
            'id': self.ultimo_id,
            'nombre': nombre,
            'edad': edad
        }
        self.usuarios.append(usuario)
        return usuario

    def buscar_usuario_por_nombre(self, nombre):
        for usuario in self.usuarios:
            if usuario['nombre'].lower() == nombre.lower():
                return usuario
        return None

    def mostrar_usuarios(self):
        return self.usuarios

# Ejemplo de uso
gestor = GestorUsuarios()
gestor.agregar_usuario("123", 30.55)
gestor.agregar_usuario("Bob", 25)

usuario_alice = gestor.buscar_usuario_por_nombre("Alice")
print("Usuario encontrado:", usuario_alice)

usuarios_registrados = gestor.mostrar_usuarios()
print("Usuarios registrados:", usuarios_registrados)