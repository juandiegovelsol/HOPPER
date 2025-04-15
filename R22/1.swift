import Foundation

struct Stage {
    var number: String
    var date: String
    var distance: String
    var startPoint: String
    var endPoint: String
    
    // Función para convertir el formato de fecha MM/DD a DD/MM/YYYY
    mutating func updateDateFormat() {
        let components = date.split(separator: "/").map(String.init)
        if components.count == 2, let month = components.first, let day = components.last {
            self.date = "\(day)/\(month)/2025"
        }
    }
}

var stages = [
    Stage(number: "Stage 1", date: "05/05", distance: "182 km", startPoint: "Bilbao", endPoint: "Bilbao"),
    Stage(number: "Stage 2", date: "05/06", distance: "208.9 km", startPoint: "Vitoria Gasteiz", endPoint: "San Sebastián"),
    Stage(number: "Stage 3", date: "05/07", distance: "193.5 km", startPoint: "Amorebieta Etxano", endPoint: "Bayona"),
    Stage(number: "Stage 4", date: "06/09", distance: "181.8 km", startPoint: "Dax", endPoint: "Nogaro"),
    Stage(number: "Stage 5", date: "06/10", distance: "162.7 km", startPoint: "Pau", endPoint: "Laruns"),
    Stage(number: "Stage 6", date: "06/12", distance: "144.9 km", startPoint: "Tarbes", endPoint: "Cauterets"),
    Stage(number: "Stage 7", date: "06/13", distance: "169.9 km", startPoint: "Mont de Marsan", endPoint: "Burdeos"),
    Stage(number: "Stage 8", date: "07/15", distance: "200.7 km", startPoint: "Libourne", endPoint: "Limoges"),
    Stage(number: "Stage 9", date: "07/16", distance: "182.4 km", startPoint: "Saint Leonard de Noblat", endPoint: "Puy de Dome"),
    Stage(number: "Stage 10", date: "07/18", distance: "167.2 km", startPoint: "Bulcania", endPoint: "Issoire"),
    Stage(number: "Stage 11", date: "07/19", distance: "179.8 km", startPoint: "Clermont Ferrand", endPoint: "Moulins"),
    Stage(number: "Stage 12", date: "08/21", distance: "168.8 km", startPoint: "Roanne", endPoint: "Belleville en Beaujolais"),
    Stage(number: "Stage 13", date: "08/22", distance: "137.8 km", startPoint: "Chatillon sur Chalaronne", endPoint: "Grand Colombier"),
    Stage(number: "Stage 14", date: "08/24", distance: "151.8 km", startPoint: "Annemasse", endPoint: "Morzine Les Portes du Soleil"),
    Stage(number: "Stage 15", date: "08/25", distance: "179 km", startPoint: "Morzine Les Portes du Soleil", endPoint: "Saint Gervais Mont Blanc"),
    Stage(number: "Stage 16", date: "08/27", distance: "22.4 km", startPoint: "Passy", endPoint: "Combloux"),
    Stage(number: "Stage 17", date: "08/28", distance: "165.7 km", startPoint: "Saint Gervais Mont Blanc", endPoint: "Courchevel"),
    Stage(number: "Stage 18", date: "08/30", distance: "184.9 km", startPoint: "Moutiers", endPoint: "Bourg en Bresse"),
    Stage(number: "Stage 19", date: "08/31", distance: "172.8 km", startPoint: "Moirans en Montagne", endPoint: "Poligny"),
    Stage(number: "Stage 20", date: "09/02", distance: "133.5 km", startPoint: "Belford", endPoint: "Le Markstein Fellering"),
    Stage(number: "Stage 21", date: "09/03", distance: "115.1 km", startPoint: "Saint Quentin en Yvelines", endPoint: "París Campos Eliseos")
]


// Actualizar el formato de las fechas
for index in stages.indices {
    stages[index].updateDateFormat()
}

func convertStagesToJSON(stages: [Stage]) -> String? {
    var groupedStages = [String: [[String: Any]]]()

    // Agrupar etapas por mes
    for stage in stages {
        let dateComponents = stage.date.split(separator: "/").map(String.init)
        if dateComponents.count == 3 {
            let month = dateComponents[1]
            let stageInfo: [String: Any] = [
                "Numero de etapa": stage.number,
                "Fecha": stage.date,
                "Distancia en km": stage.distance,
                "Punto de partida": stage.startPoint,
                "Punto de llegada": stage.endPoint
            ]

            if groupedStages[month] != nil {
                groupedStages[month]?.append(stageInfo)
            } else {
                groupedStages[month] = [stageInfo]
            }
        }
    }

    // Convertir el diccionario a JSON
    do {
        let jsonData = try JSONSerialization.data(withJSONObject: groupedStages, options: .prettyPrinted)
        return String(data: jsonData, encoding: .utf8)
    } catch {
        print("Error al convertir a JSON: \(error)")
        return nil
    }
}

// Uso de la función
if let jsonOutput = convertStagesToJSON(stages: stages) {
    print(jsonOutput)
}