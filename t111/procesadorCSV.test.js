const fs = require("fs");
const path = require("path");
const { procesarArchivoCSV } = require("./p.js"); // Asegúrate de reemplazar 'tuArchivo' con el nombre real de tu archivo de script

test("Debe calcular correctamente las ganancias con datos válidos", (done) => {
  const datosCSV = `nombreActivo,precioCompra,precioVenta,cantidad
    A,10.50,5.0055,100
    B,20.00,18.4897,50
    C,30.00,35.999,200
    D,5.50,5,300.5`;

  // Crear un archivo CSV temporal para la prueba
  const rutaCSV = path.join(__dirname, "transaccionesValido.csv");
  fs.writeFileSync(rutaCSV, datosCSV);

  const consolaMock = jest.spyOn(console, "log").mockImplementation();

  procesarArchivoCSV(rutaCSV, () => {
    expect(consolaMock).toHaveBeenCalledWith(
      expect.stringContaining("Total de ganancias: €")
    );
    consolaMock.mockRestore();
    fs.unlinkSync(rutaCSV); // Eliminar el archivo después de la prueba
    done();
  });
});

test("Debe manejar algunos datos incorrectos correctamente", (done) => {
  const datosCSV = `nombreActivo,precioCompra,precioVenta,cantidad
    A,10.50,5.0055,100
    ,20.00,18.4897,50
    C,30.00,35.999,200
    D,invalid,5,300.5`;

  // Crear un archivo CSV temporal para la prueba
  const rutaCSV = path.join(__dirname, "transaccionesAlgunosIncorrectos.csv");
  fs.writeFileSync(rutaCSV, datosCSV);

  const consolaErrorMock = jest.spyOn(console, "error").mockImplementation();

  procesarArchivoCSV(rutaCSV, () => {
    // Asegúrate de que los errores fueron registrados
    expect(consolaErrorMock).toHaveBeenCalledWith(
      expect.stringContaining("El nombre del activo no puede estar vacío")
    );
    expect(consolaErrorMock).toHaveBeenCalledWith(
      expect.stringContaining(
        "Los precios y la cantidad deben ser valores numéricos positivos"
      )
    );

    consolaErrorMock.mockRestore();
    fs.unlinkSync(rutaCSV); // Eliminar el archivo después de la prueba
    done();
  });
});

test("Debe manejar todos los datos incorrectos correctamente", (done) => {
  const datosCSV = `nombreActivo,precioCompra,precioVenta,cantidad
    ,invalid,invalid,invalid
    ,invalid,invalid,invalid`;

  // Crear un archivo CSV temporal para la prueba
  const rutaCSV = path.join(__dirname, "transaccionesTodosIncorrectos.csv");
  fs.writeFileSync(rutaCSV, datosCSV);

  const consolaErrorMock = jest.spyOn(console, "error").mockImplementation();

  procesarArchivoCSV(rutaCSV, () => {
    // Asegúrate de que cada fila incorrecta fue registrada como error
    expect(consolaErrorMock).toHaveBeenCalledTimes(2); // Como hay 2 filas incorrectas

    consolaErrorMock.mockRestore();
    fs.unlinkSync(rutaCSV); // Eliminar el archivo después de la prueba
    done();
  });
});
