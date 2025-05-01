const results = [];

function assert(condition, message) {
  results.push({ message, status: condition ? "PASS" : "FAIL" });
}

function runTests() {
  const manager = new StudentManager();

  try {
    manager.addStudent("Alice");
    assert(manager.getStudent("Alice") !== null, "Add student: Alice added");
  } catch (e) {
    assert(false, "Add student: threw error");
  }

  try {
    manager.addStudent("Alice");
    assert(false, "Duplicate student: should throw");
  } catch (e) {
    assert(true, "Duplicate student: correctly threw");
  }

  try {
    manager.setCode("Alice", "print('Hello')");
    assert(manager.getStudent("Alice").code === "print('Hello')", "Set code");
  } catch {
    assert(false, "Set code error");
  }

  return results;
}

runTests();
