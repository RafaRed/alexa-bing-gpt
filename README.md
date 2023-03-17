# alexa-bing-gpt

Implementation of Bing GPT as a Alexa Skil.


1. Say "ask" followed by your question.
2. Recieve a password.
3. Say "password" followed by your password.
4. Return your bing chat response.

# Install

### Server

You need python 3.10.9
1. Download the project files in a folder
2. Open bing chat on Edge and copy your cookies to cookies.json, you can use the extension cookie-editor
2. Inside the folder run the command `pip install -r requirements.txt` on cmd
3. run the server with: `python server.py`

### Create - Alexa Skill
1. Go to `https://developer.amazon.com/alexa/console/ask`
2. Click on `Create Skill`
3. Choose a name and locale and Next
4. Select `other`use the custom model, in the bottom, select `Alexa-hosted (Python)` and Next
5. Select `Start from scratch` and Next
6. Click on `Create Skill`
