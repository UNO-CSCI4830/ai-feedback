import quickjs
#THIS IS FOR THE STUDENT MANAGER TESTS
# Load class definition
with open("studentManager.js") as f:
    class_code = f.read()

# Load test code
with open("testStudentManager.js") as f:
    test_code = f.read()

ctx = quickjs.Context()
ctx.eval(class_code)
results = ctx.eval(test_code + "\nrunTests();")

for r in results:
    print(f"[{r['status']}] {r['message']}")
