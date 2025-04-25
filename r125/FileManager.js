const fs = require("fs");

class FileUtil {
  static randomword(length) {
    const letters = "abcdefghijklmnopqrstuvwxyz";
    let result = "";
    for (let i = 0; i < length; i++) {
      result += letters.charAt(Math.floor(Math.random() * letters.length));
    }
    return result;
  }
}

class ActionFile {
  constructor() {
    this._file_path = null;
    if (this.constructor === ActionFile) {
      throw new Error("Abstract class 'ActionFile' cannot be instantiated");
    }
  }

  read() {
    throw new Error("Method 'read' must be implemented");
  }

  write(content) {
    throw new Error("Method 'write' must be implemented");
  }
}

class FileManager extends ActionFile {
  constructor(file_path = null) {
    if (file_path !== null && !file_path.endsWith(".txt")) {
      throw new Error("File path must end with .txt");
    }
    super();
    this._file_path = file_path;
    fs.writeFileSync(this._file_path, "", { flag: "a" });
  }

  read() {
    return fs.readFileSync(this._file_path, "utf8");
  }

  write(content) {
    const processId = process.pid;
    console.log(
      `Writing to ${this._file_path}: ${content} with process ${processId}`
    );

    if (content === null || content === undefined) {
      throw new Error("Content cannot be null or undefined");
    }
    if (typeof content !== "string") {
      throw new Error("Content must be a string");
    }
    if (content.length > 100) {
      throw new Error("Content length exceeds 100 characters");
    }

    fs.appendFileSync(this._file_path, content + "\n");
  }
}
