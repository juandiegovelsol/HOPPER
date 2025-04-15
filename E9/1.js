let bookCollection = [
  {
    title: "1984",
    author: "George Orwell",
    genre: "Dystopian",
    publicationYear: 1949,
    status: "read",
    rating: 5,
  },
  {
    title: "To Kill a Mockingbird",
    author: "Harper Lee",
    genre: "Fiction",
    publicationYear: 1960,
    status: "currently reading",
    rating: 4,
  },
  {
    title: "The Great Gatsby",
    author: "F. Scott Fitzgerald",
    genre: "Fiction",
    publicationYear: 1925,
    status: "want to read",
    rating: null,
  },
];

function filterBooksByStatus(status) {
  const filteredBooks = bookCollection.filter(
    (book) => book.status.toLowerCase() === status.toLowerCase()
  );
  return filteredBooks.length > 0
    ? JSON.stringify({ books: filteredBooks }, null, 2)
    : JSON.stringify({
        message: "No se encontraron libros que coincidan con los criterios",
      });
}

function calculateAverageRating() {
  const totalRating = bookCollection.reduce(
    (acc, book) => acc + (book.rating || 0),
    0
  );
  const averageRating = totalRating / bookCollection.length;
  return JSON.stringify({ averageRating });
}

// Ejemplos de uso
console.log(filterBooksByStatus("currently reading"));
console.log(filterBooksByStatus("fantasy"));
console.log(calculateAverageRating());
