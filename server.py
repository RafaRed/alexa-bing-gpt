from flask import Flask, request, jsonify
import json
import sys
import asyncio
import random
from EdgeGPT import Chatbot, ConversationStyle
import threading
cookies = None
import time

with open('./cookies.json', 'r') as f:
    cookies = json.load(f)

app = Flask(__name__)

responses_final_list = {}

def generate_code():
    code = ""
    for i in range(2):
        code += str(random.randint(0, 9))
    return str(code)


@app.route('/res/<codes>', methods=['GET'])
def lidar_com_resposta(codes):
    codes = codes.replace("%20","").replace(" ", "")
    print("Password: " + str(codes))
    if codes in responses_final_list:
        return responses_final_list[codes]
    else:
        time.sleep(6)
        if codes in responses_final_list:
            return responses_final_list[codes]
        else:
            return "Invalid code, try again in 1 minute."


async def ask_stream_task(question, codes):
    wrote = 0
    finished = False
    bot = Chatbot(cookies=cookies)
    response_list = []
    while not finished:
        async for final, response in bot.ask_stream(prompt=question, conversation_style=ConversationStyle.creative):
            if not final:
                response_list.append(response[wrote:])
                wrote = len(response)
                sys.stdout.flush()
            else:
                response_list.clear()
                response_list.append(response["item"]["messages"][-1]["text"])
                responses_final_list[str(codes)] = response["item"]["messages"][-1]["text"]
                finished = True
                print("Finished: " + str(codes))

def between_callback(prompt, codes):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(ask_stream_task(prompt, codes))
    loop.close()

@app.route("/api")
async def api():
    prompt = request.args.get("prompt")
    timeout = 6
    codes = generate_code()
    asyncio.create_task(ask_stream_task(prompt, codes))
    _thread = threading.Thread(target=between_callback, args=(prompt, codes))
    _thread.start()
    return codes

if __name__ == "__main__":
    app.run(port=8080)