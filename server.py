from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotions():
    data = request.json
    statement = data.get('statement')

    response = emotion_detector(statement)

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
