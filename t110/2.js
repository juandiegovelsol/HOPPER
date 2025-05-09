const fs = require("fs");
const path = require("path");

function readCSV(filePath) {
  return fs.readFileSync(filePath, "utf8");
}

function parseCSV(data) {
  const lines = data.trim().split("\n");
  const headers = lines.shift().split(",");
  return lines.map((line) => {
    const values = line.split(",");
    return headers.reduce((obj, header, index) => {
      obj[header] = values[index];
      return obj;
    }, {});
  });
}

function calculateProfitLoss(transactions) {
  return transactions.reduce((total, transaction) => {
    const priceCompra = parseFloat(transaction["precio_compra"]);
    const precioVenta = parseFloat(transaction["precio_venta"]);
    const cantidad = parseFloat(transaction["cantidad"]);
    const profitLoss = (precioVenta - priceCompra) * cantidad;
    return total + profitLoss;
  }, 0);
}

const filePath = path.join(__dirname, "transacciones.csv");
const csvData = readCSV(filePath);
const transactions = parseCSV(csvData);
const totalProfitLoss = calculateProfitLoss(transactions);
console.log("Total de ganancias o pérdidas: €" + totalProfitLoss.toFixed(2));
