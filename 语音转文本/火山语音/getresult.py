import requests

url = "https://nexus.sotawork.com/upload_and_return_url/?target=local&directory=test"

payload={}
files=[
   ('file',(r'C:\Users\28254\Desktop\sotawork\语音转文本\test语音',open(r'C:\Users\28254\Desktop\sotawork\语音转文本\test语音','rb'),'audio/wav'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)

