function makeChange(amount, coins, bag = []) {
  if (amount === 0) return bag;
  let largestCoin = getLargestCoin(amount, coins);
  return makeChange(amount - largestCoin, coins, bag.concat([largestCoin]));
}

function getLargestCoin(amount, coins) {
  let sortedCoins = coins.sort((a, b) => a - b);
  for (let i = sortedCoins.length - 1; i >= 0; i--) {
    if (sortedCoins[i] <= amount) return sortedCoins[i];
  }
  throw new Error("no coin that divides amount");
}

console.log(makeChange(42, [1, 2, 5, 10, 20, 50]));
