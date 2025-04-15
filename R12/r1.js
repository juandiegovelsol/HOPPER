function calculateDistance(point1, point2) {
  return Math.abs(point1[0] - point2[0]) + Math.abs(point1[1] - point2[1]);
}

function getPermutations(array) {
  if (array.length === 0) return [[]];
  const firstEl = array[0];
  const remainingEls = array.slice(1);
  const permsWithoutFirst = getPermutations(remainingEls);
  const allPermutations = [];

  permsWithoutFirst.forEach((perm) => {
    for (let i = 0; i <= perm.length; i++) {
      const permWithFirst = [...perm.slice(0, i), firstEl, ...perm.slice(i)];
      allPermutations.push(permWithFirst);
    }
  });

  return allPermutations;
}

function optimizeRoute(products) {
  const start = [0, 0];
  let minDistance = Infinity;
  let bestRoute = null;

  const permutations = getPermutations(products);
  console.log(permutations);

  permutations.forEach((route) => {
    let currentDistance = 0;
    let currentPoint = start;

    route.forEach((product) => {
      currentDistance += calculateDistance(currentPoint, product.location);
      currentPoint = product.location;
    });

    currentDistance += calculateDistance(currentPoint, start); // Return to start

    if (currentDistance < minDistance) {
      minDistance = currentDistance;
      bestRoute = route;
    }
  });

  return bestRoute;
}

const products = [
  { name: "Leche", location: [2, 5] },
  { name: "Pan", location: [6, 3] },
  { name: "Huevos", location: [4, 7] },
  { name: "Manzanas", location: [1, 2] },
];

const optimizedRoute = optimizeRoute(products);

console.log("Ruta optimizada:");
optimizedRoute.forEach((product, index) => {
  console.log(`${index + 1}. ${product.name} en ${product.location}`);
});
