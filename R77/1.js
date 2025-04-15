const fs = require("fs");
const cheerio = require("cheerio");
const request = require("request");

// URL del archivo HTML local o remoto
//const htmlFileUrl = "tu-archivo-aqui.html";

// Opcional: si es un archivo remoto, descomenta la siguiente línea y comenta la línea anterior
const htmlFileUrl = "http://127.0.0.1:5501/R77/tu-archivo-aqui.html";

// Función para descargar el HTML del archivo remoto
function downloadHtml(url, callback) {
  request(url, (error, response, body) => {
    if (!error && response.statusCode == 200) {
      callback(body);
    } else {
      console.error(
        "Error al descargar el archivo:",
        error || response.statusCode
      );
      callback(null);
    }
  });
}

// Función para extraer la información de los trabajos
function extractJobInfo(html) {
  const $ = cheerio.load(html);
  const jobs = [];

  $(".pt3.pb3.t-12.t-black--light").each((index, element) => {
    const $element = $(element);

    const jobName = $element.find(".t-roman.t-sans a").text().trim();
    const companyName = $element.find(".company-name").text().trim();
    const location = $element.find(".location").text().trim();
    const applicationDate = $element
      .find(".reusable-search-simple-insight__text-container span")
      .text()
      .replace("Aplicado el", "")
      .trim();
    const linkedinUrl = $element.find(".t-roman.t-sans a").attr("href").trim();

    jobs.push({
      jobName,
      companyName,
      location,
      applicationDate,
      linkedinUrl: linkedinUrl.split("?")[0], // Quita parámetros como refId
    });
  });

  return jobs;
}

// Función para convertir los datos a CSV
function convertToCSV(jobs) {
  const headers =
    "Nombre de la compañía, Ubicación, Puesto de trabajo, Fecha de aplicación, URL de LinkedIn\n";
  return (
    headers +
    jobs
      .map(
        (job) =>
          `"${job.companyName}","${job.location}","${job.jobName}","${job.applicationDate}","${job.linkedinUrl}"`
      )
      .join("\n")
  );
}

// Opción 1: Leer HTML desde un archivo local
fs.readFile(htmlFileUrl, "utf8", (err, data) => {
  if (err) {
    console.error("Error al leer el archivo HTML:", err);
    return;
  }

  const jobs = extractJobInfo(data);
  const csvContent = convertToCSV(jobs);

  fs.writeFile("trabajos_aplicados.csv", csvContent, (err) => {
    if (err) {
      console.error("Error al escribir el archivo CSV:", err);
    } else {
      console.log(
        "Archivo CSV generado exitosamente como trabajos_aplicados.csv"
      );
    }
  });
});

// Opción 2: Leer HTML desde un archivo remoto
downloadHtml(htmlFileUrl, (htmlData) => {
  if (htmlData) {
    const jobs = extractJobInfo(htmlData);
    const csvContent = convertToCSV(jobs);

    fs.writeFile("trabajos_aplicados.csv", csvContent, (err) => {
      if (err) {
        console.error("Error al escribir el archivo CSV:", err);
      } else {
        console.log(
          "Archivo CSV generado exitosamente como trabajos_aplicados.csv"
        );
      }
    });
  }
});
