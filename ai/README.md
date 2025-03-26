# AI Team

## Testing Data

The `testing-datasets.ipynb` Jupyter Notebook can be used to save example {concept, rubric, exemplar} to use for testing. The easiest way to do this is to copy-and-paste from a Code.org level, such as https://studio.code.org/s/csd3-2024/lessons/17/levels/7 (requires a teacher account)
![image](https://github.com/user-attachments/assets/3d577e33-7065-414a-8d67-8ada08918a0a)
From there, you can paste into the Jupyter notebook and it will format everything and save as a JSON file.
![image](https://github.com/user-attachments/assets/1979ff8b-7dde-44bd-a6ca-ecc3820f464d)
If you're having trouble running the notebook from your own environment, you should be able to run it in Google Colab - https://colab.research.google.com/github/ 

## Gemini Notebook

The `gemini.ipynb` file is a Jupyter notebook that walks through an API call to Google Gemini Flash 2.0. To recreate these steps, you need to perform the following actions

### Step 1: Make an API Key

You can do that here: https://aistudio.google.com/apikey

Note that most usage of Google Gemini Flash 2.0 is within a Free tier:

![gemini_costs](https://github.com/user-attachments/assets/f282e4b1-9be4-4018-8b83-ea8ad1531c32)

### Step 2: Get Setup with Google Cloud

Once you make an API Key, you are prompted to continue setting up a Google Cloud account for a new project at this URL: https://console.cloud.google.com/welcome/. When you sign up, you can activate your account to earn $300 in free credits.

![gemini_free_trial](https://github.com/user-attachments/assets/3448e108-2041-46bd-8459-df85984251e8)

However, once the credits run out, you will be charged. I also setup a budget for my project so I could get notified if this happens and shut things down

![google_cloud_budget_setup](https://github.com/user-attachments/assets/b09e394b-ea60-4875-beed-dd13d99d2c9b)

### Step 3: Use AI Studio to prototype a prompt

Using aistudio.google.com, you can prototype a prompt and responses with an AI model. I iterated on a prompt using some prompting best-practices (like structured outputs and chain of reasoning) to generate this prompt and try a few examples from our testing data.

![image](https://github.com/user-attachments/assets/a8115630-0b69-44c9-bbec-c439034a8d1c)

### Step 4: Generate the Code

AI Studio has a mechanism to turn your prompt into Python code

![image](https://github.com/user-attachments/assets/95b2da90-2492-4a75-a1e3-ae1d5c79f401)

Using this as the base, you can create the Jupyter notebook

