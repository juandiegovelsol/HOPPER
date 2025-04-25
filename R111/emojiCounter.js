function emojiCounter(text) {
  const categories = {
    happy: ["😀", "😁", "😄"],
    sad: ["😢", "😭", "😞"],
    neutral: ["😐", "😶", "😑"],
  };

  const counts = { happy: 0, sad: 0, neutral: 0 };

  for (const char of text) {
    for (const [key, emojis] of Object.entries(categories)) {
      if (emojis.includes(char)) {
        counts[key]++;
      }
    }
  }

  return counts;
}

module.exports = emojiCounter;
