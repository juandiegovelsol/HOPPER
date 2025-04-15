const ionData = [
{ zPosition: 0.1, carga: +1, densidad: 0.05 },
{ zPosition: 0.2, carga: -1, densidad: 0.03 },
]


function calculateChargeDensity(data) {
return data.map((entry) => ({
chargeDensity: entry * entry.density,
}));

constchargeDensityResults = calculateChargeDensity(ionData);
console.log("Results:",chargeDensitResults);