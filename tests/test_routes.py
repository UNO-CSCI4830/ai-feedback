import json
import pytest

def test_index_route(client):
    """Test the index route returns the index.html template."""
    response = client.get('/')
    assert response.status_code == 200

def test_evaluate_route(client):
    """Test the evaluate route with basic Gemini API call."""
    
    # Send a POST request to the evaluate endpoint
    response = client.post('/evaluate', data={
        'key_concept': "test_concept",
        'rubric_extensive': "extensive_evidence",
        'rubric_convincing': "convincing_evidence",
        'rubric_limited': "limited_evidence",
        'rubric_none': "no_evidence",
        'exemplar': "exemplar",
        'student_code': "student_code"
    })
    
    # Check the response
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'recommended_rating' in data
    assert 'justification' in data
    assert 'feedback' in data
    assert 'what_went_well' in data['feedback']
    assert 'areas_for_improvement' in data['feedback']