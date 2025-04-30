from flask import Flask, render_template, request
from dotenv import load_dotenv
from google import genai
from google.genai import types
import os, json

#Load API key from .env
load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_KEY")
client = genai.Client(api_key=GEMINI_KEY)

app = Flask(__name__)

SYSTEM_PROMPT = """You are an expert code evaluator tasked with assessing student work according to a detailed rubric. You will be provided with the following inputs in a JSON format:

- Key Concept: The central idea or skill that the student should demonstrate in their program.
- Rubric: A criteria-based scoring guide with descriptions for various performance levels.
- Exemplar Program: A reference implementation that fully demonstrates the key concept at the highest level of the rubric.
- Student Program: The code written by the student to be evaluated.

Your task is to analyze the student program in relation to the key concept, rubric, and exemplar program, and return a structured evaluation in valid JSON format.

Your output must exactly match this JSON structure:

```
{
  \"recommended_rating\": \"string\",
  \"justification\": [
    \"string\",
    \"string\",
    \"... (additional specific justifications)\"
  ],
  \"feedback\": {
    \"what_went_well\": \"string\",
    \"areas_for_improvement\": \"string\"
  }
}
```
Field descriptions:
- \"recommended_rating\": A string value representing the overall rating that always provides a response based on the rubric (e.g., \"4 - Exceeds Expectations\", \"Partially Meets\", etc.).
- \"justification\": An array of specific, concise justifications that support the rating. Each justification should reference a particular aspect of the student’s code and how it aligns or misaligns with the rubric and exemplar.
- \"feedback.what_went_well\": A student-friendly explanation of strengths in the code, emphasizing alignment with the rubric.
- \"feedback.areas_for_improvement\": Actionable suggestions that clearly connect to rubric expectations and highlight opportunities for growth.

Evaluation Guidelines
- Each item in the justification array should be a standalone observation or comparison.
-Ensure that the recommended rating and justification line up and do not contradict each other.
- Reference specific evidence and line numbers from the student code where applicable.
-Justifications must include an analysis of all parts of the rubric. If a section of the rubric is not met, the justification must explain why.
-If the code does something that matches a grade of a lower score on the rubric, make sure it gets that grade
-The 'feedback.what_went_well' and 'feedback.areas_for_improvement' sections must directly reference elements of the rubric. Explain why certain aspects were successful or unsuccessful based on the rubric's criteria.
-Example: 'The code creates two sprites (lines 1 and 3) but they are at the same location (200, 200) therefore it does not meet the extensive evidence grade.'
-All references to the student code within the justification must include the line number of the code being referenced.
- Be objective and avoid assumptions about student intent.
- Language should be clear, specific, and rubric-aligned.
- Feedback responses should be written for a middle-school student with appropriate tone and voice.
-Feedback responses should be specific on what they missed to get them the specific grade.
- Respond only with a valid JSON object, properly formatted.
-Example: If the rubric states that 'Convincing Evidence' is when 'two sprites are created with different animations' and the student code has two sprites with different animations, then the recommended_rating must be 'Convincing Evidence'.
-If the Student Program contains errors that prevent it from running or being properly evaluated, indicate this in the 'justification' and 'feedback.areas_for_improvement'. If possible, specify the type of error and its location (line number)."""

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/evaluate", methods=["POST"])
def evaluate():
    key_concept = request.form["key_concept"]
    rubric = {
        "Extensive Evidence": request.form["rubric_extensive"],
        "Convincing Evidence": request.form["rubric_convincing"],
        "Limited Evidence": request.form["rubric_limited"],
        "No Evidence": request.form["rubric_none"]
    }
    exemplar = request.form["exemplar"]
    student_code = request.form["student_code"]

    payload = {
        "key_concept": key_concept,
        "rubric": rubric,
        "exemplar": exemplar,
        "student_code": student_code
    }

    contents = [types.Content(role="user", parts=[types.Part(text=json.dumps(payload))])]

    config = types.GenerateContentConfig(
        temperature=1,
        top_p=0.95,
        top_k=40,
        max_output_tokens=8192,
        response_mime_type="text/plain",
        system_instruction=[types.Part(text=SYSTEM_PROMPT)],
    )

    result_text = ""
    for chunk in client.models.generate_content_stream(
        model="gemini-2.0-flash",
        contents=contents,
        config=config
    ):
        result_text += chunk.text

    # Strip codeblock wrapper if present
    if result_text.strip().startswith("```json"):
        result_text = result_text.strip()[7:-3].strip()

    try:
        feedback = json.loads(result_text)
    except json.JSONDecodeError:
        feedback = {"error": "AI returned invalid JSON", "response": result_text}

    return render_template("index.html", feedback=json.dumps(feedback, indent=2))

if __name__ == "__main__":
    app.run()
