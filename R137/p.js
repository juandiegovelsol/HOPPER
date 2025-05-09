function List(key, val) {
  this.key = key;
  this.val = val;
  this.next = null;
  this.prev = null;
}

function LRUCache(capacity) {
  this.capacity = capacity;
  this.length = 0;
  this.map = {};
  this.head = null;
  this.tail = null;
}

LRUCache.prototype.get = function (key) {
  const node = this.map[key];

  if (!node) return -1;

  this.remove(node);
  this.insert(node.key, node.val);
  return node.val;
};

LRUCache.prototype.put = function (key, value) {
  if (this.map[key]) {
    this.remove(this.map[key]);
    this.insert(key, value);
  } else {
    if (this.length === this.capacity) {
      this.remove(this.head);
      this.insert(key, value);
    } else {
      this.insert(key, value);
      this.length++;
    }
  }
};

LRUCache.prototype.remove = function (node) {
  const prev = node.prev;
  const next = node.next;

  if (next) next.prev = prev;
  if (prev) prev.next = next;

  if (this.head === node) this.head = next;
  if (this.tail === node) this.tail = prev;

  delete this.map[node.key];
};

LRUCache.prototype.insert = function (key, val) {
  const node = new List(key, val);

  if (!this.tail) {
    this.tail = node;
    this.head = node;
  } else {
    this.tail.next = node;
    node.prev = this.tail;
    this.tail = node;
  }

  this.map[key] = node;
};

// Crear caché con capacidad 2
const cache = new LRUCache(2);

cache.put("a", 1);
cache.put("b", 2);

console.log(cache.get("a")); // → 1  (a se vuelve el más recientemente usado)
// Ahora el orden interno es [b ← a] (head ← tail)

cache.put("c", 3);
// Se excede capacidad; expulsa 'b' (el menos recientemente usado)
console.log(cache.get("b")); // → -1 (ya no está en caché)
console.log(cache.get("c")); // → 3
console.log(cache.get("a")); // → 1
