import json
from os.path import join, dirname
from ibm_watson import AssistantV2, TextToSpeechV1, SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from playsound import playsound


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


authenticator = IAMAuthenticator('a4AqChKZqBJAKxuSH28TtAYQe0iuy2ve1gikX0ZQjdJX')
assistant = AssistantV2(
    version='2020-04-01',
    authenticator = authenticator
)

assistant.set_service_url('https://api.eu-gb.assistant.watson.cloud.ibm.com/instances/d914b609-5302-4173-8376-eec616e99f8f')

response = assistant.message(
    assistant_id='f464c096-684c-4a7e-9de2-d8d8a5748a16',
    session_id='10046e4a-59be-4d9d-8278-aa24d23274b4',
    input={
        'message_type': 'text',
        'text': str
    }
).get_result()

print(json.dumps(response, indent=2))



authenticator = IAMAuthenticator('MMVDKZdT9xYQKbwFeSHmEWYLcDwBZUFturfiB6IcV4z0')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/3f15cc40-107a-41f4-bd58-f6bd7f3a88e4')


with open('bot.mp3', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            json.dumps(response["output"]["generic"][0]["text"]),
            voice='en-US_AllisonV3Voice',
            accept='audio/mp3'        
        ).get_result().content)

playsound('bot.mp3')
