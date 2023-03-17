# alexa-bing-gpt

Implementation of Bing GPT as a Alexa Skil.


1. Say "ask" followed by your question.
2. Recieve a password.
3. Say "password" followed by your password.
4. Return your bing chat response.

# Install

## Server

You need python 3.10.9
1. Download the project files in a folder
2. Open bing chat on Edge and copy your cookies to cookies.json, you can use the extension cookie-editor
2. Inside the folder run the command `pip install -r requirements.txt` on cmd
3. run the server with: `python server.py`

## Create - Alexa Skill

#### Create
1. Go to `https://developer.amazon.com/alexa/console/ask`
2. Click on `Create Skill`
3. Choose a name and locale and Next
4. Select `other`use the custom model, in the bottom, select `Alexa-hosted (Python)` and Next
5. Select `Start from scratch` and Next
6. Click on `Create Skill`

#### Choose a name
7. in `Invocations` select `Skill Invocation Name` and choose a name

#### QuestionIntent
8. in `Interaction Model` select `Intents` to create your first intent for recieve the questions
9. `+ Add Intent` write `QuestionIntent` and `Create custom intent`
10. in `Sample Utterances` add `ask {question}` accept the dialog box `Add`, and click in the `+` to add.
11. on the bottom you will see a field `question` in the slot type choose `AMAZON.SearchQuery`


#### CodeIntent
13. Create your intent to input the password
14.`+ Add Intent` write `CodeIntent` and `Create custom intent`
15. in `Sample Utterances` add `password {code}` accept the dialog box `Add`, and click in the `+` to add.
16. on the bottom you will see a field `code` in the slot type choose `AMAZON.SearchQuery`

#### Save
17. On the top click in `Save Model` and `Build Model`

### Change the Code
18. on the tab `code` replace the code on `lambda_function.py` for the code on the github with the same name
19. on the code, search for the two fields `SERVER_ADDRESS` and replace by your IP + port if needed. if you have trouble with port fowarding, see the next topic bellow.
20. click on `SAVE` and `DEPLOY`

### Testing
21. On the `Test` tab select `Development` on top
22. on the text box write Open and your choosen Skill Invocation Name
23. you should recieve the message `Hello, say ask and your question!`
24. you can ask anything using ask before the question `ask what is your name?`
25. you should recieve `say, password: ##`
26. wait 1 or 2 minutes, so bing can answer your question, then ask for it, with `password ##`
27. that's it. it should be enabled by default on your devices of the same amazon account
