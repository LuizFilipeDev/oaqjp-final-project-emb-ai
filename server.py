"""
server.py

This module provides a Flask web server with an endpoint to detect emotions from a given statement.
It includes error handling for blank entries and formats the response to include emotion scores and 
the dominant emotion. The server listens on localhost:5000.

Modules:
    - Flask: Web framework for creating the server.
    - EmotionDetection: Custom package for emotion detection.

Endpoints:
    - POST /emotionDetector: Accepts a JSON body with a 'statement' field and returns the detected 
      emotions or an error message if the statement is blank.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotions():
    """
    Endpoint to detect emotions from a given statement.

    Expects a JSON body with a 'statement' field. Returns a response with detected emotions
    and the dominant emotion. If the statement is blank, returns an error message.

    Returns:
        Response object with JSON containing the formatted response or an error message.
    """
    data = request.json
    statement = data.get('statement')

    response = emotion_detector(statement)

    if response['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again."}), 400

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    formatted_response = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} "
        f"and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

    return jsonify({"response": formatted_response})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
