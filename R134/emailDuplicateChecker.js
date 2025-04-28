// emailDuplicateChecker.js

/**
  Recibe una lista de correos electrónicos y retorna un objeto con: 
  - duplicates: array con los correos duplicados (sin repetirlos). 
  - hasDuplicates: booleano indicando si hay duplicados o no. 
 */

function findDuplicateEmails(emailList) {
  if (!Array.isArray(emailList)) {
    throw new TypeError("Input must be an array");
  }

  const seen = new Set();
  const duplicates = new Set();

  for (const email of emailList) {
    const normalized = String(email).trim().toLowerCase();
    if (seen.has(normalized)) {
      duplicates.add(normalized);
    } else {
      seen.add(normalized);
    }
  }

  return {
    hasDuplicates: duplicates.size > 0,
    duplicates: Array.from(duplicates),
  };
}

module.exports = { findDuplicateEmails };
