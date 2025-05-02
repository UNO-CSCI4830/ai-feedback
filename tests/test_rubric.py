import json
import pytest

def test_lesson_8(client):
    """Test the AI's evaluation of some student code of lesson 8"""
    
    # Send a completed rubric of lesson 8 to the endpoint
    response = client.post('/evaluate', data={
        "key_concept": "Create and use sprites.",
        'rubric_extensive': "At least two sprites have been created with different animations that are drawn to the canvas at different locations. Each sprite has a unique and meaningful label.",
        'rubric_convincing': "At least two sprites were created with different animations that were drawn to the canvas. The sprites may not have different locations or unique and meaningful labels.",
        'rubric_limited': "At least one sprite has been created with an animation that is drawn to the canvas.",
        'rubric_none': "No sprites were created or were created without an animation - shown by a gray square.",
        'exemplar': "\nvar sprite = createSprite(200, 200);\nsprite.setAnimation(\"crab_1\");\nvar b = createSprite(75, 125);\nb.setAnimation(\"fork_1\");\nvar c = createSprite(325, 125);\nc.setAnimation(\"knife_1\");\ndrawSprites();\n",
        'student_code': "var sprite1 = createSprite(200, 200);\nsprite1.setAnimation(\"crab_1\");\nvar sprite2 = createSprite(200, 200);\nsprite2.setAnimation(\"fork_1\");\ndrawSprites();\n"
    })
    
    # Check the response
    data = json.loads(response.data)
    assert data['recommended_rating'] == 'Convincing Evidence'

def test_lesson_9(client):
    """Test the AI's evaluation of some student code of lesson 9"""
    
    # Send a completed rubric of lesson 9 to the endpoint
    response = client.post('/evaluate', data={
        "key_concept": "Use dot notation to update a sprite's properties.",
        'rubric_extensive': "The arrangement of sprites is identical to the example provided in the instructions.",
        'rubric_convincing': "The sprites have been resized to fit inside the circle. There may be some slight differences between the student's work and the provided example.",
        'rubric_limited': "The sprites have been resized, but are still too large to fit inside the circle.",
        'rubric_none': "The code is either the same or has been changed in ways unrelated the assignment.",
        'exemplar': "\nbackground(\"burlywood\");\nfill(\"white\");\nellipse(200,200, 350);\nvar fries = createSprite(250,140);\nfries.setAnimation(\"fries\");\nvar burger = createSprite(110,200);\nburger.setAnimation(\"burger\");\nvar dessert = createSprite(240,270);\ndessert.setAnimation(\"watermelon\");\nfries.scale = 0.6;\nburger.scale = 0.6;\ndessert.scale = 0.6;\ndrawSprites();\n",
        'student_code': "background(\"burlywood\");\nfill(\"white\");\nellipse(200,200, 350);\nvar fries = createSprite(250,140);\nfries.setAnimation(\"fries\");\nvar burger = createSprite(110,200);\nburger.setAnimation(\"burger\");\nvar dessert = createSprite(240,270);\ndessert.setAnimation(\"watermelon\");\nfries.scale = 1.5;\nburger.scale = 1.5;\ndessert.scale = 1.5;\ndrawSprites();\n"
    })
    
    # Check the response
    data = json.loads(response.data)
    assert data['recommended_rating'] == 'Limited Evidence'

def test_lesson_15(client):
    """Test the AI's evaluation of some student code of lesson 15"""
    
    # Send a completed rubric of lesson 15 to the endpoint
    response = client.post('/evaluate', data={
        "key_concept": "Use conditionals to control the flow of a program.",
        'rubric_extensive': "The sprite's image changes from an T-rex to a pterodactyl when the sprite reaches the sky.",
        'rubric_convincing': "There is a conditional in the draw loop that checks whether the sprite has reached the sky.",
        'rubric_limited': "There is a conditional in the draw loop that checks the value of a Boolean expression.",
        'rubric_none': "There are no conditionals in the draw loop.",
        'exemplar': "\nvar backdrop = createSprite(200,200);\nbackdrop.setAnimation(\"sci_fi\");\nvar dinosaur = createSprite(200, 350);\ndinosaur.scale = 0.2;\ndinosaur.setAnimation(\"tyrannosaurus\");\n\nfunction draw() {\n  //move the dinosaur up\n  dinosaur.y = dinosaur.y - 5;\n\n  //if it gets to the sky, turn it into a pterodactyl\n  if (dinosaur.y < 100) {\n    dinosaur.setAnimation(\"pterodactyl\");\n  }\n\n  //draw everything\n  drawSprites();\n}\n",
        'student_code': "var backdrop = createSprite(200,200);\nbackdrop.setAnimation(\"sci_fi\");\nvar dinosaur = createSprite(200, 350);\ndinosaur.scale = 0.2;\ndinosaur.setAnimation(\"tyrannosaurus\");\n\nfunction draw() {\n  dinosaur.y = dinosaur.y - 5;\n  if (dinosaur.y < 100) {\n    dinosaur.setAnimation(\"pterodactyl\");\n  }\n  drawSprites();\n}"
    })
    
    # Check the response
    data = json.loads(response.data)
    assert data['recommended_rating'] == 'Extensive Evidence'