

const studentData = {

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

      <button class="store-btn" onclick="submitToAI()">Submit to AI</button>

      <h3>AI Feedback:</h3>
      <pre id="aiFeedback">${student.feedback}</pre>
  `;
  document.getElementById("mainContent").innerHTML = content;
  document.querySelector("#studentCode").addEventListener("input", function() {
    const code = this.value.trim();
    if(selectedStudent) {
        studentData[selectedStudent].code = code;
    }
  });
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

  try {
      const res = await fetch('/evaluate', {
          method: 'POST',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
          body: body
      });
      //Returns a JSON object, so grab the object then make a string
      const feedbackObj = await res.json();
      const feedbackText = JSON.stringify(feedbackObj, null, 2);

      studentData[selectedStudent].code = code;
      studentData[selectedStudent].feedback = feedbackText;
      document.getElementById('aiFeedback').textContent = feedbackText;
      alert("Student code and rubric submitted to AI successfully!");

  } catch (error) {
      console.error("Failed to get feedback:", error);
      alert("Failed to fetch AI feedback.  Check the server connection and ensure the /evaluate endpoint is working.");
      document.getElementById('aiFeedback').textContent = "Error fetching feedback.";
  }
}

async function getClassRecommendations() {
  const allFeedback = Object.values(studentData).map(s => s.feedback);
  console.log("Sending feedback to AI:", allFeedback);

  // Simulate fetch request to AI backend
  fetch("/class-recommendations", {
      method: "POST",
      headers: {
          "Content-Type": "application/json"
      },
      body: JSON.stringify({ feedbackData: allFeedback })
  })
  .then(res => res.json())
  .then(data => {
      alert("AI Recommendations:\n" + data.recommendations);
  })
  .catch(err => {
      console.error("Failed to get recommendations:", err);
      alert("Failed to fetch class recommendations.");
  });
}

window.onload = initStudentList;