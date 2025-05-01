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
    
    # DOM mock needed for testing. Modeled after some experimenting with StackOverflow.
    dom_mock = """
    // Define global object first
    const global = globalThis;
    
    // Mock DOM elements and functions
    const mockElements = {};
    const mockEventListeners = {};
    
    // Mock document object
    global.document = {
        getElementById: function(id) {
            if (!mockElements[id]) {
                mockElements[id] = {
                    innerHTML: '',
                    value: '',
                    textContent: '',
                    style: {},
                    appendChild: function(child) {
                        if (!this.children) this.children = [];
                        this.children.push(child);
                    },
                    children: []
                };
            }
            return mockElements[id];
        },
        createElement: function(tag) {
            return {
                textContent: '',
                onclick: null,
                style: {}
            };
        }
    };
    
    // Mock window object
    global.window = {
        onload: null,
        location: {
            href: 'http://localhost/'
        }
    };
    
    // Mock fetch API
    global.fetch = async function(url, options) {
        return {
            json: async function() {
                return {
                    recommended_rating: "Test Rating",
                    justification: ["Test justification"],
                    feedback: {
                        what_went_well: "Test feedback",
                        areas_for_improvement: "Test improvement"
                    }
                };
            }
        };
    };
    
    // Mock alert
    global.alert = function(msg) {
        global.lastAlert = msg;
    };
    """
    
    # Evaluate the DOM mock and the script
    runtime.eval(dom_mock)
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