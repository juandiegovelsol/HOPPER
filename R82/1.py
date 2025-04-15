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

    def obtener_usuario(self, usuario_id):
        for usuario in self.usuarios:
            if usuario['id'] == usuario_id:
                return usuario
        return None

    def listar_usuarios(self):
        return self.usuarios

    def eliminar_usuario(self, usuario_id):
        for i, usuario in enumerate(self.usuarios):
            if usuario['id'] == usuario_id:
                return self.usuarios.pop(i)
        return None

# Ejemplo de uso:
gestor = GestorUsuarios()
gestor.agregar_usuario(123, 25.5)
gestor.agregar_usuario("Ana Gómez", 30)

print(gestor.listar_usuarios())
print(gestor.obtener_usuario(1))
gestor.eliminar_usuario(2)
print(gestor.listar_usuarios())