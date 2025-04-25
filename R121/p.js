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
