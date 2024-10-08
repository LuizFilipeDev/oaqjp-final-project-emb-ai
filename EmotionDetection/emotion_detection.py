import requests
import json

def emotion_detector(text_to_analyze):
    """
    Endpoint to detect emotions from a given statement.

    Expects a JSON body with a 'text_to_analyze' field. Returns a response with detected emotions
    and the dominant emotion. If the text_to_analyze is blank, returns an empty object.

    Returns:
        Response object.
    """
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, headers=headers, json=input_json)
    
    if response.status_code == 200:

        response_json = response.json()
        
        emotions = response_json['emotionPredictions'][0]['emotion']
        anger_score = emotions.get('anger', 0)
        disgust_score = emotions.get('disgust', 0)
        fear_score = emotions.get('fear', 0)
        joy_score = emotions.get('joy', 0)
        sadness_score = emotions.get('sadness', 0)
        
        dominant_emotion = max(emotions, key=emotions.get)
        
        result = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
        return result
    else:
        return f"Error: {response.status_code}, {response.text}"