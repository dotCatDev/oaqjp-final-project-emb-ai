import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    myobj = { "raw_document": { "text": text_to_analyse } }

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(url, json=myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    emotions = formatted_response['emotionPredictions'];


    anger_score = emotions[0]['emotion']['anger']
    disgust_score = emotions[0]['emotion']['disgust']
    fear_score = emotions[0]['emotion']['fear']
    joy_score = emotions[0]['emotion']['joy']
    sadness_score = emotions[0]['emotion']['sadness']

    prev_emotion = 0
    max_emotion = 0
    dominant_emotion = {}
    for emotion in emotions[0]['emotion']:
        curr_emotion = emotions[0]['emotion'][emotion]

        if(curr_emotion > prev_emotion):
            dominant_emotion = emotion
            prev_emotion = curr_emotion
            

        

    output = {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': dominant_emotion
    }

    return output



    