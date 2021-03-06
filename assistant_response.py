import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('a4AqChKZqBJAKxuSH28TtAYQe0iuy2ve1gikX0ZQjdJX')
assistant = AssistantV2(
    version='2020-04-01',
    authenticator = authenticator
)

assistant.set_service_url('https://api.eu-gb.assistant.watson.cloud.ibm.com/instances/d914b609-5302-4173-8376-eec616e99f8f')

response = assistant.message(
    assistant_id='f464c096-684c-4a7e-9de2-d8d8a5748a16',
    session_id='6b662d98-7ab8-4e94-b866-219f3da15fac',
    input={
        'message_type': 'text',
        'text': 'Hello'
    }
).get_result()

print(json.dumps(response, indent=2))
