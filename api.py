import requests

API_KEY = 'your api key'

reqId = requests.post(
    url='https://api.assemblyai.com/v2/transcript',
    json={
        "audio_url": "https://bit.ly/3yxKEIY"
    },
    headers={
        'Authorization':API_KEY

    }
)

reqId.raise_for_status()

ID:str = reqId.json()['id']

req = requests.get(
    url=f"https://api.assemblyai.com/v2/transcript/{ID}",
    headers={
        'Authorization':API_KEY
    }
)
req.raise_for_status()

print(req.json())