import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('jPh4eRtgQSzB3zwLey9crrmPALlg_5si9sIYqEPGzpzG')
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)

speech_to_text.set_service_url('https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/85eef52a-017d-4521-87c2-06bd0ebf82ef')

with open(join(dirname(__file__), './.', 'hello.mp3'),
               'rb') as audio_file:
    speech_recognition_results = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/mp3',
    ).get_result()
#print(json.dumps(speech_recognition_results, indent=2))

str = ""

while bool(speech_recognition_results.get('results')):
    str=speech_recognition_results.get('results').pop().get('alternatives').pop().get('transcript')+str[:]

print(str)
