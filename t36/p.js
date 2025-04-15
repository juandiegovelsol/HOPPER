const fs = require("fs");

const EnergiaProcessor = {
  procesarArchivoJSON(rutaArchivo) {
    try {
      const jsonString = fs.readFileSync(rutaArchivo, "utf8");
      return this.procesarDatos(jsonString);
    } catch (error) {
      console.error("Error:", error.message);
      return null;
    }
  },

  procesarDatos(jsonString) {
    try {
      const registros = JSON.parse(jsonString);

      if (!Array.isArray(registros)) {
        throw new Error(
          "El formato JSON no es válido. Se espera un array de registros."
        );
      }

      this.validador.validarRegistros(registros);
      return this.analizador.analizarConsumo(registros);
    } catch (error) {
      console.error("Error al procesar los datos:", error.message);
      return null;
    }
  },

  validador: {
    validarRegistros(registros) {
      const idsRegistros = new Set();

      for (let i = 0; i < registros.length; i++) {
        const registro = registros[i];

        this.validarIdRegistro(registro, i, idsRegistros);

        if (!registro.fecha || typeof registro.fecha !== "string") {
          throw new Error(
            `Registro #${i + 1}: Falta fecha o formato incorrecto`
          );
        }

        if (!Array.isArray(registro.dispositivos)) {
          throw new Error(
            `Registro #${i + 1}: El campo 'dispositivos' debe ser un array`
          );
        }

        this.validarDispositivos(registro.dispositivos, i);
      }
    },

    validarIdRegistro(registro, indice, idsRegistros) {
      if (
        !registro.id ||
        typeof registro.id !== "number" ||
        registro.id <= 0 ||
        !Number.isInteger(registro.id)
      ) {
        throw new Error(
          `Registro #${indice + 1}: El ID debe ser un entero positivo`
        );
      }

      if (idsRegistros.has(registro.id)) {
        throw new Error(
          `Registro #${indice + 1}: El ID ${registro.id} está duplicado`
        );
      }
      idsRegistros.add(registro.id);
    },

    validarDispositivos(dispositivos, indiceRegistro) {
      for (let j = 0; j < dispositivos.length; j++) {
        const dispositivo = dispositivos[j];

        if (
          !dispositivo.idDispositivo ||
          typeof dispositivo.idDispositivo !== "number" ||
          dispositivo.idDispositivo <= 0 ||
          !Number.isInteger(dispositivo.idDispositivo)
        ) {
          throw new Error(
            `Registro #${indiceRegistro + 1}, Dispositivo #${
              j + 1
            }: El ID del dispositivo debe ser un entero positivo`
          );
        }

        if (
          !dispositivo.horasUso ||
          typeof dispositivo.horasUso !== "number" ||
          dispositivo.horasUso <= 0
        ) {
          throw new Error(
            `Registro #${indiceRegistro + 1}, Dispositivo #${
              j + 1
            }: Horas de uso inválidas`
          );
        }

        if (
          !dispositivo.potenciaKW ||
          typeof dispositivo.potenciaKW !== "number" ||
          dispositivo.potenciaKW <= 0
        ) {
          throw new Error(
            `Registro #${indiceRegistro + 1}, Dispositivo #${
              j + 1
            }: Potencia inválida`
          );
        }
      }
    },
  },

  analizador: {
    analizarConsumo(registros) {
      let consumoTotalKWh = 0;
      const consumoPorDispositivo = {};

      registros.forEach((registro) => {
        registro.dispositivos.forEach((dispositivo) => {
          const consumoKWh = dispositivo.potenciaKW * dispositivo.horasUso;
          consumoTotalKWh += consumoKWh;

          if (!consumoPorDispositivo[dispositivo.idDispositivo]) {
            consumoPorDispositivo[dispositivo.idDispositivo] = 0;
          }
          consumoPorDispositivo[dispositivo.idDispositivo] += consumoKWh;
        });
      });

      const dispositivoMayorConsumo = this.encontrarDispositivoMayorConsumo(
        consumoPorDispositivo
      );

      console.log(`Consumo total: ${consumoTotalKWh.toFixed(2)} KWh`);
      console.log(
        `Dispositivo con mayor consumo: ID ${
          dispositivoMayorConsumo.id
        } (${dispositivoMayorConsumo.consumo.toFixed(2)} KWh)`
      );

      return {
        consumoTotalKWh,
        dispositivoMayorConsumo,
      };
    },

    encontrarDispositivoMayorConsumo(consumoPorDispositivo) {
      let maxConsumo = 0;
      let dispositivoMayorConsumo = null;

      Object.entries(consumoPorDispositivo).forEach(
        ([idDispositivo, consumo]) => {
          if (consumo > maxConsumo) {
            maxConsumo = consumo;
            dispositivoMayorConsumo = { id: parseInt(idDispositivo), consumo };
          }
        }
      );

      return dispositivoMayorConsumo;
    },
  },
};

if (require.main === module) {
  const rutaArchivo = process.argv[2] || "consumo_energia.json";
  EnergiaProcessor.procesarArchivoJSON(rutaArchivo);
}

module.exports = EnergiaProcessor;
