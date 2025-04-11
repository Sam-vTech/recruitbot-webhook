from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ["OPENAI_API_KEY"]

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()
        print("Received data:", data)

        user_input = data['queryResult']['queryText']
        print("User input:", user_input)

        prompt = f"You are pretending to be a job candidate in a mock interview. Provide a detailed and natural response to this recruiter question: '{user_input}'"

        response = openai.Completion.create(
            model="gpt-4",
            prompt=prompt,            max_tokens=150,
            temperature=0.8
        )
        print("OpenAI response:", response)

        answer = response['choices'][0]['text'].strip()
        print("Answer:", answer)

        return jsonify({"fulfillmentText": answer})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"fulfillmentText": "An error occurred."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
