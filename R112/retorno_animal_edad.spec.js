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

describe("retorno_animal_edad", () => {
  it("procesa correctamente un animal con edad definida", () => {
    const datos = [{ animal: "perro", entorno: "casa", edad: 5 }];
    const resultado = retorno_animal_edad(datos);

    cy.wrap(resultado).should("deep.equal", [{ perro: "casa", edad: 10 }]);
  });

  it("calcula la edad basada en longitud cuando no se proporciona", () => {
    const datos = [{ animal: "gato", entorno: "casa" }];
    const resultado = retorno_animal_edad(datos);

    cy.wrap(resultado).should("deep.equal", [{ gato: "casa", edad: 40 }]);
  });
});
