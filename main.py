from flask import Flask, request, jsonify
from flask_cors import CORS
import traceback

app = Flask(__name__)
CORS(app)  # ✅ Enables browser access (CORS)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()
        print("📨 Received data:", data)

        user_input = data['queryResult']['queryText']
        print("💬 User input:", user_input)

        # 🧪 Mocked GPT-style response
        answer = f"Mocked response: I appreciate your question. Here's how I would answer – '{user_input}'"

        print("🤖 Mocked Answer:", answer)

        return jsonify({"fulfillmentText": answer})

    except Exception as e:
        traceback.print_exc()
        print("❌ Error:", str(e))
        return jsonify({"fulfillmentText": "An error occurred."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
