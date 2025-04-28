// transactionValidator.js
function validateTransactions(transactionList) {
  if (!Array.isArray(transactionList)) {
    throw new TypeError("Input must be an array");
  }

  const invalidTransactions = transactionList.filter((tx) => {
    return (
      !tx ||
      typeof tx !== "object" ||
      !("amount" in tx) ||
      !("date" in tx) ||
      !("accountId" in tx)
    );
  });

  return {
    hasInvalids: invalidTransactions.length > 0,
    invalidTransactions,
  };
}

module.exports = { validateTransactions };
