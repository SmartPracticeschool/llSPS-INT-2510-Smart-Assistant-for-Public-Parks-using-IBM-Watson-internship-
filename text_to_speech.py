from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from playsound import playsound


authenticator = IAMAuthenticator('MMVDKZdT9xYQKbwFeSHmEWYLcDwBZUFturfiB6IcV4z0')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/3f15cc40-107a-41f4-bd58-f6bd7f3a88e4')

with open('bot.mp3', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'Hello',
            voice='en-US_AllisonV3Voice',
            accept='audio/mp3'        
        ).get_result().content)

playsound('bot.mp3')
