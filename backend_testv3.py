import unittest
from app import app

class EvaluateRouteTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.valid_form_data = {
            "key_concept": "Respond to arrow keys",
            "rubric_extensive": "All 4 keys",
            "rubric_convincing": "Most keys",
            "rubric_limited": "Some input",
            "rubric_none": "No input",
            "exemplar": "function draw() { if (keyDown('left')) { ... } }",
            "student_code": "function draw() { if (keyDown('right')) { ... } }"
        }

    def test_valid_input_returns_200(self):
        print("Running: test_valid_input_returns_200")
        res = self.client.post("/evaluate", data=self.valid_form_data)
        self.assertEqual(res.status_code, 200)

    def test_valid_input_returns_json_keys(self):
        print("Running: test_valid_input_returns_json_keys")
        res = self.client.post("/evaluate", data=self.valid_form_data)
        data = res.get_json()
        self.assertIn("recommended_rating", data)
        self.assertIn("feedback", data)

    def test_missing_student_code_field(self):
        print("Running: test_missing_student_code_field")
        bad_data = self.valid_form_data.copy()
        del bad_data["student_code"]
        res = self.client.post("/evaluate", data=bad_data)
        self.assertNotEqual(res.status_code, 200)

    def test_incorrect_content_type_fails(self):
        print("Running: test_incorrect_content_type_fails")
        res = self.client.post("/evaluate", data="invalid", content_type="application/json")
        self.assertNotEqual(res.status_code, 200)

if __name__ == "__main__":
    unittest.main()
