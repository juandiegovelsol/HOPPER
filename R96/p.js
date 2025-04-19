function calculateMathString(mathStr) {
  const parts = mathStr.match(/(\d+|\+|\-|\*|\/|\(|\))/g) || [];
  let currentPosition = 0;

  const getNumber = () => {
    if (parts[currentPosition] === "(") {
      currentPosition++;
      const result = solveExpression();
      currentPosition++;
      return result;
    }
    return parseInt(parts[currentPosition++]);
  };

  const solveMultDiv = () => {
    let total = getNumber();
    while (parts[currentPosition] === "*" || parts[currentPosition] === "/") {
      const operation = parts[currentPosition++];
      const nextNum = getNumber();
      total = operation === "*" ? total * nextNum : total / nextNum;
    }
    return total;
  };

  const solveExpression = () => {
    let total = solveMultDiv();
    while (parts[currentPosition] === "+" || parts[currentPosition] === "-") {
      const operation = parts[currentPosition++];
      const nextNum = solveMultDiv();
      total = operation === "+" ? total + nextNum : total - nextNum;
    }
    return total;
  };

  return solveExpression();
}

console.log(calculateMathString("2+3*4"));

console.log(calculateMathString("(2+3)*4"));

console.log(calculateMathString("10/2-3"));

/* console.log(calculateMathString(null)); */

console.log(calculateMathString(""));
