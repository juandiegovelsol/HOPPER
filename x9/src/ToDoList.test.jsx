import React from "react";
import { render, screen, fireEvent } from "@testing-library/react";
import ToDoList from "./ToDoList"; // Asegúrate de que la ruta sea correcta

describe("ToDoList Component", () => {
  beforeEach(() => {
    render(<ToDoList />);
  });

  test("Debe agregar una tarea válida", () => {
    const input = screen.getByPlaceholderText("Nueva tarea");
    const addButton = screen.getByText("Agregar");

    fireEvent.change(input, { target: { value: "Nueva tarea" } });
    fireEvent.click(addButton);

    expect(screen.getByText("Nueva tarea")).toBeInTheDocument();
  });

  test("Debe marcar una tarea como completada", () => {
    const input = screen.getByPlaceholderText("Nueva tarea");
    const addButton = screen.getByText("Agregar");

    fireEvent.change(input, { target: { value: "Nueva tarea" } });
    fireEvent.click(addButton);

    const task = screen.getByText("Nueva tarea");
    fireEvent.click(task);

    expect(task).toHaveStyle("text-decoration: line-through");
  });

  test("Debe eliminar una tarea", () => {
    const input = screen.getByPlaceholderText("Nueva tarea");
    const addButton = screen.getByText("Agregar");

    fireEvent.change(input, { target: { value: "Nueva tarea" } });
    fireEvent.click(addButton);

    const deleteButton = screen.getByText("Eliminar");
    fireEvent.click(deleteButton);

    expect(screen.queryByText("Nueva tarea")).not.toBeInTheDocument();
  });

  test("No debería agregar una tarea vacía y mostrar un mensaje de error", () => {
    const addButton = screen.getByText("Agregar");
    fireEvent.click(addButton);

    expect(screen.getByRole("alert")).toHaveTextContent(
      "La tarea no puede estar vacía"
    );
  });

  test("No debería agregar una tarea si la entrada es solo un espacio en blanco", () => {
    const input = screen.getByPlaceholderText("Nueva tarea");
    const addButton = screen.getByText("Agregar");

    fireEvent.change(input, { target: { value: "   " } });
    fireEvent.click(addButton);

    expect(screen.getByRole("alert")).toHaveTextContent(
      "La tarea no puede estar vacía"
    );
  });
});
