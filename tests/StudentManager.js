class StudentManager {
  constructor() {
    this.students = {};
  }

  addStudent(name) {
    if (!name || this.students[name]) {
      throw new Error("Invalid or duplicate student name.");
    }
    this.students[name] = { code: "", feedback: "No feedback yet" };
  }

  setCode(name, code) {
    if (!this.students[name]) throw new Error("Student not found.");
    this.students[name].code = code;
  }

  setFeedback(name, feedback) {
    if (!this.students[name]) throw new Error("Student not found.");
    this.students[name].feedback = feedback;
  }

  getStudent(name) {
    return this.students[name] || null;
  }
}

// Export for QuickJS
globalThis.StudentManager = StudentManager;
