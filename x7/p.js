function transformToBW(hex, opacity) {
  const r = parseInt(hex.substr(1, 2), 16);
  const g = parseInt(hex.substr(3, 2), 16);
  const b = parseInt(hex.substr(5, 2), 16);
  const avg = (r + g + b) / 3;
  const mixed = avg * opacity + 255 * (1 - opacity);
  console.log(mixed);
  if (mixed < 128) {
    console.log(`${hex} @${opacity} → Negro`);
  } else if (mixed > 128) {
    console.log(`${hex} @${opacity} → Blanco`);
  } else {
    console.log(`${hex} @${opacity} → Gris`);
  }
}

transformToBW("#FF0000", 1);
transformToBW("#00FF00", 0.5);
transformToBW("#0000FF", 0.2);
transformToBW("#123456", 1);
