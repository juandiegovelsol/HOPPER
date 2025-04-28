// transactionValidator.test.js
const { validateTransactions } = require("./transactionValidator");

describe("validateTransactions", () => {
  // Test cuando todas las transacciones son válidas
  /* test("should return no invalid transactions and hasInvalids false when all transactions are valid", () => {
    const transactions = [
      { amount: 100, date: "2024-09-09", accountId: "A123" },
      { amount: 200, date: "2024-09-10", accountId: "A124" },
      { amount: 300, date: "2024-09-11", accountId: "A125" },
    ];
    const result = validateTransactions(transactions);
    expect(result).toEqual({
      invalidTransactions: [],
      hasInvalids: false,
    });
  });

  // Test cuando hay transacciones con campos faltantes
  test("should return invalid transactions and hasInvalids true when transactions have missing fields", () => {
    const transactions = [
      { amount: 100, date: "2024-09-09" },
      { amount: 200, accountId: "A124" },
      { date: "2024-09-11", accountId: "A125" },
    ];
    const result = validateTransactions(transactions);
    expect(result).toEqual({
      invalidTransactions: transactions,
      hasInvalids: true,
    });
  });
 */
  // Test cuando hay transacciones vacías o con tipos incorrectos
  test("should return invalid transactions when transactions are empty or have incorrect types", () => {
    const transactions = [
      {},
      { amount: 100, date: "2024-09-09", accountId: "A123" },
      { amount: 200, date: "09-09-2024", accountId: "A123" },
    ];
    const result = validateTransactions(transactions);
    console.log(result);
    expect(result).toEqual({
      hasInvalids: true,
      invalidTransactions: [{}],
    });
  });

  // Test cuando la lista está vacía
  /* test("should return no invalid transactions and hasInvalids false when the list is empty", () => {
    const transactions = [];
    const result = validateTransactions(transactions);
    expect(result).toEqual({
      invalidTransactions: [],
      hasInvalids: false,
    });
  });

  // Test cuando la entrada no es un arreglo válido
  test("should throw TypeError when input is not a valid array", () => {
    const transactions = "not an array";
    expect(() => validateTransactions(transactions)).toThrow(TypeError);
  }); */
});
