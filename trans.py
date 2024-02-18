from flask import Flask, request
import requests
import json
import re
app = Flask(__name__)
@app.route('/translate', methods=['get'])
def translate():
    content = request.args.get('text')
    api_key = "AIzaSyAj1k9TCdLF2PL3Gz6lFGTYSZwLptUE9ig"
    # Set the HTTP proxy
    proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890',
    }
    Language="zh"
    # Set the request body
    request_body = {
        "contents": [
            {
                "parts": [
                    {
                        "text":"You are a professional,authentic translation engine,only returns translations.\nFor example:\n<Start>\nHello <Keep This Symbol>\nWorld <Keep This Symbol>\n<End>\nThe translation is:\n<Start>\n你好<Keep This Symbol>\n世界<Keep This Symbol>\n<End>\n\nTranslate the content to "+Language+" Language:\n\n<Start>"+content+"<End>"
                    }
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.9,
            "topK": 1,
            "topP": 1,
            "maxOutputTokens": 2048,
            "stopSequences": []
        },
        "safetySettings": [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_ONLY_HIGH"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_ONLY_HIGH"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_ONLY_HIGH"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_ONLY_HIGH"
            }
        ]
    }

    # Make the request
    response = requests.post(
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.0-pro:generateContent?key=" + api_key,
        headers={"Content-Type": "application/json"},
        json=request_body,
        proxies=proxies,
    )

    # Get the response data
    response_data = response.json()

    # Print the translated text

    trans=response_data["candidates"][0]["content"]["parts"][0]["text"]
   



    trans = re.sub(r"<Start>|<End>", "", trans)

    # Perform translation here
    return trans
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)