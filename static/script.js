

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

      <button class="store-btn" id="studentButton" onclick="submitToAI()">Submit to AI</button>

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
  studentData[name] = { code: "", feedback: "{}" };
  initStudentList();
  input.value = "";
}

async function submitToAI() {
  if (!selectedStudent) return;

  document.querySelector("#studentButton").disabled = true;
  document.querySelector("#studentButton").textContent = "Submitting...";

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
      //alert("Student code and rubric submitted to AI successfully!");

      document.querySelector("#studentButton").disabled = false;
      document.querySelector("#studentButton").textContent = "Submit to AI";

  } catch (error) {
      console.error("Failed to get feedback:", error);
      //alert("Failed to fetch AI feedback.  Check the server connection and ensure the /evaluate endpoint is working.");
      document.getElementById('aiFeedback').textContent = "Error fetching feedback.";
      document.querySelector("#studentButton").disabled = false;
      document.querySelector("#studentButton").textContent = "Submit to AI";
  }
}

async function getClassRecommendations(test=false) {
  document.querySelector("#classButton").disabled = true;
  document.querySelector("#classButton").textContent = "Submitting...";
  let allFeedback = Object.values(studentData).map(s => s.feedback);
  if(test === true) {
    allFeedback = [
      "{\n  \"feedback\": {\n    \"areas_for_improvement\": \"To improve your code, you need to add a conditional statement inside the draw loop. The conditional should check if the sprite has reached the sky. If it has, then the sprite's image should change from a T-rex to a pterodactyl.\",\n    \"what_went_well\": \"You have successfully created a sprite and made it move. Keep up the good work!\"\n  },\n  \"justification\": [\n    \"The student's code does not contain any conditional statements inside the draw loop. Therefore, the code does not meet any of the criteria for 'Limited Evidence', 'Convincing Evidence', or 'Extensive Evidence' based on the rubric.\",\n    \"The absence of a conditional statement means the student's code only moves the dinosaur without changing its image or checking any conditions, directly corresponding to the 'No Evidence' level.\"\n  ],\n  \"recommended_rating\": \"No Evidence\"\n}",
      "{\n  \"feedback\": {\n    \"areas_for_improvement\": \"To achieve a higher rating, make sure your conditional statement checks the sprite's position to determine when to change the animation. You need to update the `isSky` variable based on the dinosaur's y position to make the animation change when the dinosaur reaches the sky. You are currently checking a boolean value of isSky but that value is never changed.\",\n    \"what_went_well\": \"You correctly implemented a conditional statement inside the draw loop. This shows you understand the basic structure for controlling program flow based on a condition.\"\n  },\n  \"justification\": [\n    \"The code includes a conditional statement within the draw loop (line 9).\",\n    \"The conditional checks the value of the Boolean variable `isSky` (line 9).\",\n    \"The sprite's image does not change based on the sprite's position in the sky, as `isSky` is never set to true, and thus it doesn't reach the \\\"Convincing Evidence\\\" or \\\"Extensive Evidence\\\" levels. The exemplar uses `if (dinosaur.y < 100)`.\"\n  ],\n  \"recommended_rating\": \"Limited Evidence\"\n}",
      "{\n  \"feedback\": {\n    \"areas_for_improvement\": \"You've successfully met all the requirements for this task! There are no specific areas for improvement in this particular program. Keep experimenting with different conditions and actions to further enhance your programming skills.\",\n    \"what_went_well\": \"Great job! You used a conditional statement to change the dinosaur's animation when it reached a certain point in the sky. The sprite successfully transforms from a T-rex to a pterodactyl, demonstrating excellent control of the program's flow based on conditions.\"\n  },\n  \"justification\": [\n    \"The student's code fulfills the 'Extensive Evidence' criteria. The dinosaur sprite moves upwards, and its image changes from a tyrannosaurus to a pterodactyl when it reaches a y-coordinate of less than 100 (line 9), effectively simulating reaching the sky.\",\n    \"The code includes a conditional statement (line 8) inside the draw loop that checks if the sprite has reached the sky (dinosaur.y < 100), thus meeting the 'Convincing Evidence' criterion.\",\n    \"The conditional statement evaluates a Boolean expression (dinosaur.y < 100) inside the draw loop (line 7-11), therefore fulfilling the 'Limited Evidence' requirement.\"\n  ],\n  \"recommended_rating\": \"Extensive Evidence\"\n}"
    ]
  }
  console.log((test ? "[TEST]" : "") + "Sending feedback to AI:", allFeedback);

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
      console.log(data);

      document.querySelector("#classButton").disabled = false;
      document.querySelector("#classButton").textContent = "Get Class Recommendations";
  })
  .catch(err => {
      console.error("Failed to get recommendations:", err);
      //alert("Failed to fetch class recommendations.");
  });
}

window.onload = initStudentList;