// emojiCounter.test.js
const emojiCounter = require("./emojiCounter"); // Ajusta este path según la ubicación del código

describe("emojiCounter", () => {
  // Test para emojis felices
  test("debería contar correctamente los emojis felices", () => {
    const text = "😀 😁 😄";
    const result = emojiCounter(text);
    expect(result).toEqual({ happy: 3, sad: 0, neutral: 0 });
  });

  // Test para emojis tristes
  test("debería contar correctamente los emojis tristes", () => {
    const text = "😢 😭 😞";
    const result = emojiCounter(text);
    expect(result).toEqual({ happy: 0, sad: 3, neutral: 0 });
  });

  // Test para emojis neutros
  test("debería contar correctamente los emojis neutros", () => {
    const text = "😐 😶 😑";
    const result = emojiCounter(text);
    expect(result).toEqual({ happy: 0, sad: 0, neutral: 3 });
  });

  // Test para combinación de emojis de diferentes categorías
  test("debería contar correctamente una mezcla de emojis", () => {
    const text = "😀 😭 😐";
    const result = emojiCounter(text);
    expect(result).toEqual({ happy: 1, sad: 1, neutral: 1 });
  });

  // Test para texto sin emojis
  test("debería devolver conteos de cero para texto sin emojis", () => {
    const text = "Este es un texto sin emojis";
    const result = emojiCounter(text);
    expect(result).toEqual({ happy: 0, sad: 0, neutral: 0 });
  });

  // Test para emojis adicionales no definidos en el objeto de categorías
  test("debería ignorar emojis no definidos en el objeto de categorías", () => {
    const text = "😎 🤔";
    const result = emojiCounter(text);
    expect(result).toEqual({ happy: 0, sad: 0, neutral: 0 });
  });
});
