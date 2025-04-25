import Foundation

class EstadoUsuario {
    var estado: Int
    var incrementarConteo: Int
    var decrementarConteo: Int

    init(estadoInicial: Int = 0) {
        self.estado = estadoInicial
        self.incrementarConteo = 0
        self.decrementarConteo = 0
    }
}

class ProcesadorEventos {
    private var estados: [String: EstadoUsuario] = [:]
    private let lock = NSLock()
    
    func procesarEvento(usuario: String, tipo: String, valor: Int) -> String {
        lock.lock()
        defer { lock.unlock() }
        
        if estados[usuario] == nil {
            estados[usuario] = EstadoUsuario()
        }
        
        guard let estadoUsuario = estados[usuario] else {
            return "Error al acceder al estado del usuario \(usuario)"
        }
        
        switch tipo {
        case "INICIO":
            estadoUsuario.estado = valor
            return "Estado inicializado a \(estadoUsuario.estado) para el usuario \(usuario)"
            
        case "INCREMENTAR":
            estadoUsuario.estado += valor
            estadoUsuario.incrementarConteo += 1
            return "Estado incrementado a \(estadoUsuario.estado) para el usuario \(usuario)"
            
        case "DECREMENTAR":
            if estadoUsuario.decrementarConteo < estadoUsuario.incrementarConteo {
                estadoUsuario.estado -= valor
                estadoUsuario.decrementarConteo += 1
                return "Estado decrementado a \(estadoUsuario.estado) para el usuario \(usuario)"
            } else {
                return "No se puede decrementar antes de tener incrementos suficientes para el usuario \(usuario)"
            }
            
        default:
            return "Tipo de evento desconocido para el usuario \(usuario)"
        }
    }
    
    func obtenerEstado(usuario: String) -> Int? {
        lock.lock()
        defer { lock.unlock() }
        
        return estados[usuario]?.estado
    }
}