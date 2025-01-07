import requests
import json
import requests
import os
answer = {}

wavlist = []

answer = {}
def list_files_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 获取文件的绝对路径
            absolute_path = os.path.join(root, file)
            yield absolute_path
def getpath(directory):
    for path in list_files_in_directory(directory):



        url = "https://nexus.sotawork.com/upload_and_return_url/?target=local&directory=test"

        payload={}
        files=[
        ('file',(path,open(path,'rb'),'audio/wav'))
        ]
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        resource_url = response.json()['data']['file_url']
        yield path,resource_url


for now_path,url in getpath('/Users/mz/Desktop/Learn/knowledge/computer/ML/实习/sotawork/语音转文本/音频文件'):
    answer[now_path] = []
    # 火山引擎API信息
    appid = '4047031898'
    access_token = 'dq120nidzwClPET5lodSeH-CCkk4UPIL'
    secerete = 'Woctm7DUfxCyP3REJ-uCq2hVe45WUwqk'

    api_endpoint = 'https://openspeech.bytedance.com/api/v1/auc/submits'

    # 上传的音频文件路径

    # API 请求头
    headers = {
        'Authorization': 'Bearer;dq120nidzwClPET5lodSeH-CCkk4UPIL',
        'Content-Type': 'application/json'
    }

    body_content ={
        "app": {
            "appid": "4047031898",
            "token": "dq120nidzwClPET5lodSeH-CCkk4UPIL",
            "cluster": "volc_auc_common"
        },
        "user": {
            "uid": "388808087185088"
    },
    "request":{
        "boosting_table_name":"db6115f9-d51a-4f22-a11c-d6c881ee7b4a"
    },
        "audio": {
            "format": "wav",
            "url": url
        },
        "additions": {
            "use_itn": "False",
            "with_speaker_info": "True"
        },
    }

    response = requests.post('https://openspeech.bytedance.com/api/v1/auc/submit', json=body_content, headers=headers)
    response = response.json()
    # print(response)
    # 火山引擎API信息
    appid = '4047031898'
    access_token = 'dq120nidzwClPET5lodSeH-CCkk4UPIL'
    secerete = 'Woctm7DUfxCyP3REJ-uCq2hVe45WUwqk'
    cluster = 'volc_auc_common'
    api_endpoint = 'https://openspeech.bytedance.com/api/v1/auc/submits'


    
    # API 请求头
    headers = {
        'Authorization': 'Bearer;dq120nidzwClPET5lodSeH-CCkk4UPIL',
        'Content-Type': 'application/json'
    }

    body_content ={
        "appid": appid,
        "token": access_token,
        "cluster": cluster,
        "id": response['resp']['id']
        # "id":"f0b3f2a8-fab4-4826-9a60-09b5e1722909"
    }
    
    response = requests.post('https://openspeech.bytedance.com/api/v1/auc/query', 
    json=body_content, headers=headers)
    while len(response.json()['resp']['text']) == 0:
        response = requests.post('https://openspeech.bytedance.com/api/v1/auc/query', 
    json=body_content, headers=headers)
    response = response.json()
    print(response)
    answer[now_path].append(response)

    # 将列表内容写入文件
with open('huoshan_output.json', 'w') as f:
    json.dump(answer, f, indent=4, ensure_ascii=False)
print("文件已保存为t")