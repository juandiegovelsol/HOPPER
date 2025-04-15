import Foundation

// Estructura que representa una etapa de la carrera
struct Etapa {
    var numero: String
    var fecha: String
    var distancia: String
    var partida: String
    var llegada: String
}

// Función para cambiar el formato de la fecha de MM/DD a DD/MM/YYYY
func cambiarFormatoFecha(fecha: String) -> String {
    let components = fecha.split(separator: "/").map { String($0) }
    guard components.count == 2 else {
        return fecha
    }
    let mes = components[0]
    let dia = components[1]
    let anio = "2025"
    print("\(dia)/\(mes)/\(anio)")
    return "\(dia)/\(mes)/\(anio)"
}

// Función para agrupar las etapas por mes y convertirlas a formato JSON
func convertirEtapasAJSON(etapas: [Etapa]) -> String? {
    var etapasPorMes: [String: [[String: Any]]] = [:]

    // Organizar las etapas por mes
    for etapa in etapas {
        let fechaConvertida = cambiarFormatoFecha(fecha: etapa.fecha)
        let mes = String(fechaConvertida.split(separator: "/")[1])
        
        // Crear el diccionario de la etapa con la fecha convertida
        let etapaDic = [
            "Numero": etapa.numero,
            "Fecha": fechaConvertida,
            "Distancia": etapa.distancia,
            "Partida": etapa.partida,
            "Llegada": etapa.llegada
        ]

        // Insertar la etapa en el mes correspondiente
        if etapasPorMes[mes] != nil {
            etapasPorMes[mes]?.append(etapaDic)
        } else {
            etapasPorMes[mes] = [etapaDic]
        }
    }

    // Convertir a JSON
    let sortedEtapasPorMes = etapasPorMes.keys.sorted().map { mes in
        return [mes: etapasPorMes[mes] ?? []]
    }

    if let jsonData = try? JSONSerialization.data(withJSONObject: sortedEtapasPorMes, options: .prettyPrinted) {
        return String(data: jsonData, encoding: .utf8)
    }
    
    return nil
}

// Ejemplo de cómo usar el código
let etapas = [
    Etapa(numero: "Stage 1", fecha: "05/05", distancia: "182 km", partida: "Bilbao", llegada: "Bilbao"),
    Etapa(numero: "Stage 2", fecha: "05/06", distancia: "208.9 km", partida: "Vitoria Gasteiz", llegada: "San Sebastián"),
    Etapa(numero: "Stage 3", fecha: "05/07", distancia: "193.5 km", partida: "Amorebieta Etxano", llegada: "Bayona"),
    Etapa(numero: "Stage 4", fecha: "06/09", distancia: "181.8 km", partida: "Dax", llegada: "Nogaro"),
    Etapa(numero: "Stage 5", fecha: "06/10", distancia: "162.7 km", partida: "Pau", llegada: "Laruns"),
    Etapa(numero: "Stage 6", fecha: "06/12", distancia: "144.9 km", partida: "Tarbes", llegada: "Cauterets"),
    Etapa(numero: "Stage 7", fecha: "06/13", distancia: "169.9 km", partida: "Mont de Marsan", llegada: "Burdeos"),
    Etapa(numero: "Stage 8", fecha: "07/15", distancia: "200.7 km", partida: "Libourne", llegada: "Limoges"),
    Etapa(numero: "Stage 9", fecha: "07/16", distancia: "182.4 km", partida: "Saint Leonard de Noblat", llegada: "Puy de Dome"),
    Etapa(numero: "Stage 10", fecha: "07/18", distancia: "167.2 km", partida: "Bulcania", llegada: "Issoire"),
    Etapa(numero: "Stage 11", fecha: "07/19", distancia: "179.8 km", partida: "Clermont Ferrand", llegada: "Moulins"),
    Etapa(numero: "Stage 12", fecha: "08/21", distancia: "168.8 km", partida: "Roanne", llegada: "Belleville en Beaujolais"),
    Etapa(numero: "Stage 13", fecha: "08/22", distancia: "137.8 km", partida: "Chatillon sur Chalaronne", llegada: "Grand Colombier"),
    Etapa(numero: "Stage 14", fecha: "08/24", distancia: "151.8 km", partida: "Annemasse", llegada: "Morzine Les Portes du Soleil"),
    Etapa(numero: "Stage 15", fecha: "08/25", distancia: "179 km", partida: "Morzine Les Portes du Soleil", llegada: "Saint Gervais Mont Blanc"),
    Etapa(numero: "Stage 16", fecha: "08/27", distancia: "22.4 km", partida: "Passy", llegada: "Combloux"),
    Etapa(numero: "Stage 17", fecha: "08/28", distancia: "165.7 km", partida: "Saint Gervais Mont Blanc", llegada: "Courchevel"),
    Etapa(numero: "Stage 18", fecha: "08/30", distancia: "184.9 km", partida: "Moutiers", llegada: "Bourg en Bresse"),
    Etapa(numero: "Stage 19", fecha: "08/31", distancia: "172.8 km", partida: "Moirans en Montagne", llegada: "Poligny"),
    Etapa(numero: "Stage 20", fecha: "09/02", distancia: "133.5 km", partida: "Belford", llegada: "Le Markstein Fellering"),
    Etapa(numero: "Stage 21", fecha: "09/03", distancia: "115.1 km", partida: "Saint Quentin en Yvelines", llegada: "París Campos Eliseos")
    // Añade todas las demás etapas aquí...
]

if let jsonResult = convertirEtapasAJSON(etapas: etapas) {
    print(jsonResult)
}