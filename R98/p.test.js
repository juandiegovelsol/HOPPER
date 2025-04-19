import { existsSync, unlinkSync, readFileSync } from "fs";
import { parsearMetarXml, exportarResumen } from "./index";

describe("parsearMetarXml", () => {
  const mockXML = {
    response: {
      data: [
        {
          METAR: [
            {
              raw_text: ["KJFK 122351Z 18010KT 10SM CLR 20/10 A2992 RMK AO2"],
              temp_c: ["20.0"],
              wind_dir_degrees: ["180"],
              wind_speed_kt: ["10"],
            },
          ],
        },
      ],
    },
  };

  test("extrae correctamente los datos de METAR", () => {
    const metar = parsearMetarXml(mockXML);
    expect(metar.texto_crudo).toMatch(/KJFK/);
    expect(metar.temp_c).toBe("20.0");
    expect(metar.velocidad_viento_kt).toBe("10");
  });

  test("maneja la ausencia de METAR correctamente", () => {
    const xmlVacio = { response: { data: [{}] } };
    const resultado = parsearMetarXml(xmlVacio);
    expect(resultado).toBe("No hay METAR reciente disponible.");
  });
});

describe("exportarResumen", () => {
  const resumen = {
    aeropuerto: {
      nombre: "Aeropuerto Internacional de Prueba",
      pais: "XX",
      codigo_gps: "XXXX",
      altitud_ft: 100,
    },
    metar: { texto_crudo: "EJEMPLO", temp_c: "25", velocidad_viento_kt: "10" },
  };

  afterEach(() => {
    if (existsSync("resumen-vuelo.json")) unlinkSync("resumen-vuelo.json");
  });

  test("exporta a JSON", () => {
    exportarResumen(resumen, "json");
    const contenido = JSON.parse(readFileSync("resumen-vuelo.json", "utf-8"));
    expect(contenido.aeropuerto.nombre).toBe(
      "Aeropuerto Internacional de Prueba"
    );
  });
});
