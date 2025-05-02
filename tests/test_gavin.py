import json
import pytest

def testNoRubricSent(client):
    #Although rubric not sent, some sort of data should be received 
    # and filled out in JSON format.
    #Otherwise errors could occur during parsing
    response = client.post('/evaluate', data={"key_concept": "Use conditionals to control the flow of a program.",
    "rubric_extensive": "",
    "rubric_convincing": "",
    "rubric_limited": "",
    "rubric_none": "",
    "exemplar": "\nvar backdrop = createSprite(200,200);\nbackdrop.setAnimation(\"sci_fi\");\nvar dinosaur = createSprite(200, 350);\ndinosaur.scale = 0.2;\ndinosaur.setAnimation(\"tyrannosaurus\");\n\nfunction draw() {\n  //move the dinosaur up\n  dinosaur.y = dinosaur.y - 5;\n\n  //if it gets to the sky, turn it into a pterodactyl\n  if (dinosaur.y < 100) {\n    dinosaur.setAnimation(\"pterodactyl\");\n  }\n\n  //draw everything\n  drawSprites();\n}\n",
    "student_code": "Anything can go here when it comes to what I'm testing"})
                           
    content = json.loads(response.data)
    feedback = content["feedback"]
    justification = content["justification"]
    recommended_rating = content["recommended_rating"]
    
    assert len(justification) > 0
    assert len(feedback) > 0
    assert len(recommended_rating) > 0

def testNoExampleSent(client):
    #Same idea as first but with no example sent
    response = client.post('/evaluate', data={"key_concept": "Use conditionals to control the flow of a program.",
    "rubric_extensive": "The sprite's image changes from an T-rex to a pterodactyl when the sprite reaches the sky.",
    "rubric_convincing": "There is a conditional in the draw loop that checks whether the sprite has reached the sky.",
    "rubric_limited": "There is a conditional in the draw loop that checks the value of a Boolean expression.",
    "rubric_none": "There are no conditionals in the draw loop.",
    "exemplar": "",
    "student_code":"Anything can go here when it comes to what I'm testing"})
    
    content = json.loads(response.data)
    feedback = content["feedback"]
    justification = content["justification"]
    recommended_rating = content["recommended_rating"]
    
    assert len(justification) > 0
    assert len(feedback) > 0
    assert len(recommended_rating) > 0

def testNoKeyConcept(client):
    #Same idea as before with different information not sent (key concept)
    response = client.post('/evaluate', data={"key_concept": "",
    "rubric_extensive": "The sprite's image changes from an T-rex to a pterodactyl when the sprite reaches the sky.",
    "rubric_convincing": "There is a conditional in the draw loop that checks whether the sprite has reached the sky.",
    "rubric_limited": "There is a conditional in the draw loop that checks the value of a Boolean expression.",
    "rubric_none": "There are no conditionals in the draw loop.",
    "exemplar": "\nvar backdrop = createSprite(200,200);\nbackdrop.setAnimation(\"sci_fi\");\nvar dinosaur = createSprite(200, 350);\ndinosaur.scale = 0.2;\ndinosaur.setAnimation(\"tyrannosaurus\");\n\nfunction draw() {\n  //move the dinosaur up\n  dinosaur.y = dinosaur.y - 5;\n\n  //if it gets to the sky, turn it into a pterodactyl\n  if (dinosaur.y < 100) {\n    dinosaur.setAnimation(\"pterodactyl\");\n  }\n\n  //draw everything\n  drawSprites();\n}\n",
    "student_code":"Anything can go here when it comes to what I'm testing"})
    
    content = json.loads(response.data)
    feedback = content["feedback"]
    justification = content["justification"]
    recommended_rating = content["recommended_rating"]
    
    assert len(justification) > 0
    assert len(feedback) > 0
    assert len(recommended_rating) > 0
