const fs = require("fs");

const trades = JSON.parse(fs.readFileSync("operaciones.json", "utf8"));

let total = 0;

for (const { name, entryPrice, exitPrice, quantity, isLong } of trades) {
  const profit =
    (isLong ? exitPrice - entryPrice : entryPrice - exitPrice) * quantity;
  console.log(`${name}: ${profit}`);
  total += profit;
}

console.log(`Total: ${total}`);
