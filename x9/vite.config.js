import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  test: {
    globals: true, // permite usar describe/test sin importar importar
    environment: "jsdom", // simula el DOM de un navegador
    setupFiles: "./src/setupTests.js", // archivo para extensiones (ej. jest-dom)
  },
});
