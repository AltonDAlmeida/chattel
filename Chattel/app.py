from flask import Flask, request, jsonify
import ai

app = Flask(__name__)

# Configure the chatbot with API key
API_KEY = "your_api_key"
ai.configure(api_key=API_KEY)

# Initialize the chatbot model
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json  # Receive JSON data from the frontend
    user_message = data.get('message')
    
    if user_message.lower() == "bye":
        return jsonify({"response": "Chatbot: Bye"})  # End the chat when "bye" is received
    
    # Get the response from the chatbot model
    response = chat.send_message(user_message)
    
    return jsonify({"response": response.text})  # Send the chatbot's response back to the frontend     

if __name__ == '__main__':
    app.run(port=5500, debug=True)
