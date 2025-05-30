from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    subject = data.get('subject')
    message = data.get('message')
    print(f"Sending Email\nSubject: {subject}\nMessage: {message}")
    return jsonify({"message": "Email sent successfully!"})

if __name__ == '__main__':
    app.run(debug=True)