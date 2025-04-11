from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ["OPENAI_API_KEY"]

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    user_input = data['queryResult']['queryText']

    prompt = f"You are pretending to be a job candidate in a mock interview. Provide a detailed and natural response to this recruiter question: '{user_input}'"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8
    )

    answer = response['choices'][0]['message']['content'].strip()
    return jsonify({"fulfillmentText": answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
@app.route('/')
def home():
    return "Server is running!"
