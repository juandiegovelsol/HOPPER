const usePasswordStrength = () => {
  const [strength, setStrength] = useState("weak");
  const [suggestions, setSuggestions] = useState([]);

  const hasUpper = (str) => {
    for (let i = 0; i < str.length; i++) {
      if (str[i] !== str[i].toLowerCase()) return true;
    }
    return false;
  };

  const hasLower = (str) => {
    for (let i = 0; i < str.length; i++) {
      if (str[i] !== str[i].toUpperCase()) return true;
    }
    return false;
  };

  const hasDigit = (str) => {
    for (let i = 0; i < str.length; i++) {
      if (!isNaN(parseInt(str[i]))) return true;
    }
    return false;
  };

  const hasSpecial = (str) => {
    const specials = `!@#$%^&*()_+-=[]{};':"\\|,.<>/?~`;
    return [...specials].some((c) => str.includes(c));
  };

  const isCommon = (str) => {
    const common = ["password", "123456", "qwerty"];
    const lowerStr = str.toLowerCase();
    return common.some((p) => lowerStr.includes(p));
  };

  const hasRepeats = (str) => {
    for (let i = 0; i < str.length - 3; i++) {
      if (str[i] === str[i + 1] && str[i] === str[i + 2]) return true;
    }
    return false;
  };

  const checkStrength = (password) => {
    if (!password) {
      setStrength("empty");
      setSuggestions([]);
      return;
    }

    let score = 0;
    const tips = [];

    if (password.length >= 12) score += 2;
    else if (password.length >= 8) score += 1;
    else tips.push("Use 8+ characters");

    if (hasUpper(password)) score += 1;
    else tips.push("Add uppercase");

    if (hasLower(password)) score += 1;
    else tips.push("Add lowercase");

    if (hasDigit(password)) score += 1;
    else tips.push("Add numbers");

    if (hasSpecial(password)) score += 1;
    else tips.push("Add special chars");

    if (isCommon(password)) {
      score -= 2;
      tips.push("Avoid common phrases");
    }

    if (hasRepeats(password)) {
      score -= 1;
      tips.push("Avoid repeats");
    }

    setStrength(score >= 6 ? "strong" : score >= 4 ? "medium" : "weak");
    setSuggestions(tips);
  };

  return { strength, suggestions, checkStrength };
};
