from flask import Flask, request, jsonify
import openai
import os
import traceback

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

        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8
        )

        print("OpenAI response object:", response)

        answer = response.choices[0].message.content.strip()
        print("Answer:", answer)

        return jsonify({"fulfillmentText": answer})

    except Exception as e:
        traceback.print_exc()  # 🔥 Prints full error stack trace
        print("Error:", str(e))
        return jsonify({"fulfillmentText": "An error occurred."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
