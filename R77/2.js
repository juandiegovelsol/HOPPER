const fs = require("fs");
const cheerio = require("cheerio");
const csv = require("csv-writer");

// Ruta al archivo HTML
const htmlFilePath = "tu_archivo.html";
// Ruta donde se guardará el CSV
const csvFilePath = "trabajos_aplicados.csv";

// Inicializar el escritor de CSV
const writer = fs.createWriteStream(csvFilePath);
const csvWriter = csv.createObjectCsvWriter({
  path: csvFilePath,
  header: [
    { id: "compañía", title: "Compañía" },
    { id: "ubicación", title: "Ubicación" },
    { id: "puesto", title: "Puesto de Trabajo" },
    { id: "fecha_aplicación", title: "Fecha de Aplicación" },
    { id: "url_linkedin", title: "URL de LinkedIn" },
  ],
});

// Leer el archivo HTML
fs.readFile(htmlFilePath, "utf8", (err, data) => {
  if (err) {
    console.error("Error al leer el archivo HTML:", err);
    return;
  }

  // Cargar el HTML con Cheerio
  const $ = cheerio.load(data);
  let trabajos = [];

  // Extraer información de los trabajos
  $(".pt3.pb3.t-12.t-black--light").each((index, element) => {
    const $element = $(element);
    const puesto = $element.find("a.job-link").text().trim();
    const compañía = $element.find("div.company-name").text().trim();
    const ubicación = $element.find("div.location").text().trim();
    const fechaAplicación = $element
      .find("span.application-date")
      .text()
      .trim();
    const urlLinkedIn = $element.find("a.job-link").attr("href").split("?")[0];

    trabajos.push({
      compañía,
      ubicación,
      puesto,
      fechaAplicación,
      urlLinkedIn,
    });
  });

  // Escribir los datos en el archivo CSV
  csvWriter
    .writeRecords(trabajos)
    .then(() => {
      console.log("Archivo CSV generado con éxito en:", csvFilePath);
    })
    .catch((error) => {
      console.error("Error al escribir en el archivo CSV:", error);
    });
});
