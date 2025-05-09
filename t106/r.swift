import Foundation

func calculateTotal(from entries: [String]) -> String {
    let pattern = #"^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)\s+(\d+)$"#
    let regex = try! NSRegularExpression(pattern: pattern)
    var total: Double = 0

    for entry in entries {
        let trimmed = entry.trimmingCharacters(in: .whitespacesAndNewlines)
        let range = NSRange(trimmed.startIndex..<trimmed.endIndex, in: trimmed)

        guard let match = regex.firstMatch(in: trimmed, options: [], range: range) else {
            continue
        }

        let nsTrimmed = trimmed as NSString
        let hhString = nsTrimmed.substring(with: match.range(at: 1))
        let mmString = nsTrimmed.substring(with: match.range(at: 2))
        let ssString = nsTrimmed.substring(with: match.range(at: 3))
        let rateString = nsTrimmed.substring(with: match.range(at: 4))

        guard let hh = Int(hhString),
              let mm = Int(mmString),
              let ss = Int(ssString),
              let rate = Int(rateString),
              rate > 0
        else {
            continue
        }
        let seconds = hh * 3600 + mm * 60 + ss
        total += Double(seconds) / 3600.0 * Double(rate)
    }

    let formatter = NumberFormatter()
    formatter.numberStyle = .currency
    formatter.currencyCode = "EUR"
    formatter.locale = Locale(identifier: "es_ES")
    return formatter.string(from: NSNumber(value: total)) ?? "EUR \(total)"
}


// Función auxiliar para crear la cadena esperada formateada
func formatExpectedValue(_ value: Double) -> String {
    let formatter = NumberFormatter()
    formatter.numberStyle = .currency
    formatter.currencyCode = "EUR"
    formatter.locale = Locale(identifier: "es_ES")
    return formatter.string(from: NSNumber(value: value)) ?? ""
}

// Caso de prueba con todos los valores válidos
func testAllValidEntries() {
    let entries = [
        "01:30:45 20",
        "02:45:00 25",
        "08:00:00 30"
    ]
    let result = calculateTotal(from: entries)
    let expectedValue: Double = 339.00
    let expected = formatExpectedValue(expectedValue) 
    print("Prueba entradas válidas: Resultado = '\(result)', Esperado = '\(expected)'")
    assert(result == expected, "Falló la prueba de entradas válidas. Se esperaba '\(expected)' pero se obtuvo '\(result)'")
}

// Caso de prueba con algunos valores inválidos
func testSomeInvalidEntries() {
    let entries = [
        "01:30:45 20",
        "abcde",
        "24:00:00 25",
        "08:00:00 -5",
        "09:30:45 15"
    ]
    let result = calculateTotal(from: entries)
    let expectedValue: Double = 172.9375
    let expected = formatExpectedValue(expectedValue)
    print("Prueba algunas entradas inválidas: Resultado = '\(result)', Esperado = '\(expected)'")
    assert(result == expected, "Falló la prueba de entradas parcialmente inválidas. Se esperaba '\(expected)' pero se obtuvo '\(result)'")
}

// Caso de prueba con todos los valores inválidos
func testAllInvalidEntries() {
    let entries = [
        "25:00:00 20",
        "09:60:60 20",
        "abcde",
        "10:15:30 abc"
    ]
    let result = calculateTotal(from: entries)
    let expectedValue: Double = 0.00
    let expected = formatExpectedValue(expectedValue)
    print("Prueba todas entradas inválidas: Resultado = '\(result)', Esperado = '\(expected)'")
    assert(result == expected, "Falló la prueba de todas las entradas inválidas. Se esperaba '\(expected)' pero se obtuvo '\(result)'")
}

// Ejecutar las pruebas
testAllValidEntries()
testSomeInvalidEntries()
testAllInvalidEntries()
print("Pruebas Completadas")