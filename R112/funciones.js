function retorno_animal_edad(lista) {
  const animal_por_entorno = lista.map((item) => {
    const recipiente = {};
    recipiente[item.animal] = item.entorno;
    if (item.edad) {
      recipiente.edad = item.edad * 2;
    } else {
      recipiente.edad = item.animal.length * 10;
    }
    return recipiente;
  });
  return animal_por_entorno;
}
