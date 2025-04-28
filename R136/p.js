class LimitDictionary {
  constructor(capacity) {
    this.capacity = capacity;
    this.dictionary = new Map();
  }

  get(key) {
    if (!this.dictionary.has(key)) return -1;

    const value = this.dictionary.get(key);

    this.dictionary.delete(key);
    this.dictionary.set(key, value);
    return value;
  }

  put(key, value) {
    if (this.dictionary.has(key)) {
      this.dictionary.delete(key);
    }

    this.dictionary.set(key, value);

    if (this.dictionary.size > this.capacity) {
      const firstKey = this.dictionary.keys().next().value;
      this.dictionary.delete(firstKey);
    }
  }
}

k;
