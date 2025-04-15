filePath = "./" + input("nombre del archivo .txt:\n-> ") + ".txt"

file = open(filePath,"r", encoding="utf-8")

line = file.readline()

gastosMensuales = {}

while line != "":
    line = line.split()
    filteredLine=""
    
    for char in line:
        filteredLine += char
    
    if (not filteredLine.isdigit()):
        nombreCategoria = filteredLine
        gastosMensuales[nombreCategoria] = 0
    
    else:
        gastosMensuales[nombreCategoria] += int(filteredLine)
        
    line = file.readline()

file.close()

if "" in gastosMensuales:
    del gastosMensuales[""]


totalMensual = "Total mensual es"
print("")
for key in gastosMensuales:
    print(key+":", gastosMensuales[key])
    totalMensual += gastosMensuales[key]

print("\n"+"El total del mes es", totalMensual,"\n")