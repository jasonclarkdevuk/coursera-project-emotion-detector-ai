'''
This module is able to analyse text / emotion detection
'''
import json
import requests

def emotion_detector(text_to_analyze):
    '''
    A function that gathers emotion data.
    It provides the tone label and the score.
    Provides errors if there is invalid input.
    '''
    url = "https://sn-watson-emotion.labs.skills.network/v1"
    url_2 = "/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze }}

    # HTTP Post request to get emotion data
    response = requests.post(url + url_2, json=input_json, headers=headers)

    return response.text