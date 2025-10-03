from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/sms", methods=["POST"])
def sms_reply():
    user_msg = request.form["Body"]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a playful and insightful AI texting friend."},
            {"role": "user", "content": user_msg}
        ]
    )

    ai_reply = response["choices"][0]["message"]["content"]

    twilio_response = MessagingResponse()
    twilio_response.message(ai_reply)
    return str(twilio_response)

if __name__ == "__main__":
    app.run(debug=True)
