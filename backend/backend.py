from google import genai
import sys

#Prompt from AI team. May need changing if they want something changed.
entry_prompt = """You are an expert code evaluator tasked with assessing student work according to a detailed rubric. You will be provided with the following inputs in a JSON format:

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
- \"recommended_rating\": A string value representing the overall rating based on the rubric (e.g., \"4 - Exceeds Expectations\", \"Partially Meets\", etc.).
- \"justification\": An array of specific, concise justifications that support the rating. Each justification should reference a particular aspect of the student’s code and how it aligns or misaligns with the rubric and exemplar.
- \"feedback.what_went_well\": A student-friendly explanation of strengths in the code, emphasizing alignment with the rubric.
- \"feedback.areas_for_improvement\": Actionable suggestions that clearly connect to rubric expectations and highlight opportunities for growth.

Evaluation Guidelines:
- Each item in the justification array should be a standalone observation or comparison.
- Reference specific evidence and line numbers from the student code where applicable.
- Be objective and avoid assumptions about student intent.
- Language should be clear, specific, and rubric-aligned.
- Feedback responses should be written for a middle-school student with appropriate tone and voice.
- Respond only with a valid JSON object, properly formatted."""

#This will be Flask functions getting input from frontend in later version
print("Enter entire user input with proper formatting (CTRL + D twice when done): ")
user_input = sys.stdin.read().strip()
final_prompt = f"{entry_prompt}  {user_input}"

#Connects us to Gemini (use own key down below)
client = genai.Client(api_key="use own key here")
response = client.models.generate_content(model="gemini-2.0-flash", contents=final_prompt)

#Change to JSON and parse in later version
print(response.text)