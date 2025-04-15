function esPrimo(num) {
  if (num < 2) return false;
  for (let i = 2; i * i <= num; i++) {
    if (num % i === 0) return false;
  }
  return true;
}

function imprimirPrimos(N) {
  for (let i = 0; i <= N; i++) {
    if (esPrimo(i)) {
      console.log(i);
    }
  }
}

const N = 100;
if (!isNaN(N) && N >= 0) {
  console.log(`Números primos del 0 al ${N}:`);
  imprimirPrimos(N);
} else {
  console.log("Por favor, ingrese un número válido.");
}
