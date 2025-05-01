const studentData = {
  "Alice": {
    code: "",
    feedback: "No feedback yet"
  },
  "Bob": {
    code: "",
    feedback: "No feedback yet"
  }
};

let selectedStudent = null;

function initStudentList() {
  const list = document.getElementById("studentList");
  list.innerHTML = "";
  for (const name in studentData) {
    const li = document.createElement("li");
    li.textContent = name;
    li.onclick = () => showStudentEditor(name);
    list.appendChild(li);
  }
}

function showStudentEditor(name) {
  selectedStudent = name;
  const student = studentData[name];
  const content = `
    <h2>Student: ${name}</h2>

    <h3>Student Code:</h3>
    <textarea id="studentCode" placeholder="Paste student code here...">${student.code}</textarea>

    <h3>Key Concept:</h3>
    <textarea id="keyConcept" placeholder="e.g., Loops, Conditionals, Functions..."></textarea>

    <h3>Exemplar:</h3>
    <textarea id="exemplar" placeholder="Exemplar Code"></textarea>

    <h3>Rubric Evaluation:</h3>
    <div class="rubric-container">
      <div class="rubric-section">
        <h4>Extensive Evidence</h4>
        <textarea id="extensiveEvidence" placeholder="Criteria for extensive evidence..."></textarea>
      </div>
      <div class="rubric-section">
        <h4>Convincing Evidence</h4>
        <textarea id="convincingEvidence" placeholder="Criteria for convincing evidence..."></textarea>
      </div>
      <div class="rubric-section">
        <h4>Limited Evidence</h4>
        <textarea id="limitedEvidence" placeholder="Criteria for limited evidence..."></textarea>
      </div>
      <div class="rubric-section">
        <h4>No Evidence</h4>
        <textarea id="noEvidence" placeholder="Criteria for no evidence..."></textarea>
      </div>
    </div>

    <button class="store-btn" onclick="submitToAI()">Submit to AI</button>

    <h3>AI Feedback:</h3>
    <pre id="aiFeedback"></pre>
  `;
  document.getElementById("mainContent").innerHTML = content;
}

function addStudent() {
  const input = document.getElementById("newStudentInput");
  const name = input.value.trim();
  if (!name || studentData[name]) {
    alert("Enter a unique student name.");
    return;
  }
  studentData[name] = { code: "", feedback: "No feedback yet" };
  initStudentList();
  input.value = "";
}

async function submitToAI() {
  if (!selectedStudent) return;

  const code = document.getElementById("studentCode").value.trim();
  const keyConcept = document.getElementById("keyConcept").value.trim();
  const exemplar = document.getElementById("exemplar").value.trim();
  const rubric = {
    extensive: document.getElementById("extensiveEvidence").value.trim(),
    convincing: document.getElementById("convincingEvidence").value.trim(),
    limited: document.getElementById("limitedEvidence").value.trim(),
    none: document.getElementById("noEvidence").value.trim()
  };
  
  //This is required for the way the API call works
  const body = new URLSearchParams();
  body.append("student_code", code);
  body.append("key_concept", keyConcept);
  body.append("exemplar", exemplar);
  body.append("rubric_extensive", rubric.extensive);
  body.append("rubric_convincing", rubric.convincing);
  body.append("rubric_limited", rubric.limited);
  body.append("rubric_none", rubric.none);

  const res = await fetch('/evaluate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body
  });
  //Returns a JSON object, so grab the object then make a string
  const feedbackObj = await res.json();
  const feedbackText = JSON.stringify(feedbackObj, null, 2);
  document.getElementById('aiFeedback').textContent = feedbackText;
}

window.onload = initStudentList;