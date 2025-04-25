import { useState, useEffect } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);
  console.log(usePasswordStrength("aA1"));
  console.log(usePasswordStrength("$uperStr0ng!"));
  console.log(usePasswordStrength("password123"));
  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  );
}

export default App;

const usePasswordStrength = (password) => {
  const [strength, setStrength] = useState("empty");
  const [feedback, setFeedback] = useState([]);

  useEffect(() => {
    if (!password) {
      setStrength("empty");
      setFeedback([]);
      return;
    }

    const checks = [
      { test: password.length >= 12, message: "12+ characters" },
      { test: /[A-Z]/.test(password), message: "uppercase letter" },
      { test: /[0-9]/.test(password), message: "number" },
      { test: /[^A-Za-z0-9]/.test(password), message: "symbol" },
      {
        test: !/(password|123456)/i.test(password),
        message: "uncommon phrase",
      },
    ];

    const passed = checks.filter((c) => c.test);
    setFeedback(passed.map((c) => c.message));
    setStrength(
      password.length < 8 ? "weak" : passed.length < 3 ? "medium" : "strong"
    );
  }, [password]);

  return { strength, feedback };
};
