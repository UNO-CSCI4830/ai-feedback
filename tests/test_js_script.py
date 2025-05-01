import pytest
import quickjs
import os
import json

# StackOverflow said to do this
def load_js_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

# Create a QuickJS runtime and context for testing
@pytest.fixture
def js_context():
    runtime = quickjs.Context()
    
    script_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'script.js')
    script_content = load_js_file(script_path)
    
    runtime.eval(script_content)
    
    return runtime

def test_init_student_list(js_context):
    """Basic test of first function"""
    # Call the function
    js_context.eval("initStudentList()")
    
    # It should have updated this element, so grab it
    student_list = js_context.eval("document.getElementById('studentList')")
    
    # Check that it worked as expected
    assert js_context.eval("Object.keys(studentData).length") == 2