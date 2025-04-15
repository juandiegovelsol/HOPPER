function paginateAndFilter(data, { page = 1, limit = 10, filters = {} }) {
  const filteredData = data.filter((item) =>
    Object.entries(filters).every(([key, value]) =>
      item[key]?.toString().toLowerCase().includes(value.toLowerCase())
    )
  );

  const startIndex = (page - 1) * limit;
  const endIndex = startIndex + limit;
  const paginatedData = filteredData.slice(startIndex, endIndex);

  return {
    totalItems: filteredData.length,
    totalPages: Math.ceil(filteredData.length / limit),
    currentPage: page,
    data: paginatedData,
  };
}

const data = [
  { id: 1, name: "Juan Pérez", role: "admin" },
  { id: 2, name: "María García", role: "user" },
  { id: 3, name: "Carlos López", role: "user" },
  { id: 4, name: "Ana Fernández", role: "admin" },
];

console.log(
  paginateAndFilter(data, { page: 1, limit: 2, filters: { role: "admin" } })
);

console.log(
  paginateAndFilter(data, { page: 2, limit: 2, filters: { role: "admin" } })
);

console.log(paginateAndFilter(data, { page: 1, limit: 2, filters: {} }));
