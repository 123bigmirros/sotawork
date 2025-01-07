import requests
import json
import requests
import os
import time
start_time = time.time()
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


for now_path,url in getpath('/Users/mz/Desktop/Learn/knowledge/computer/ML/实习/sotawork/语音转文本/困难'):
    answer[now_path] = []
    # 火山引擎API信息
    appid = '2166725073'
    access_token = 'v8MEhYaZ4dCjAb6sFOlNQBjb2Z_8c-Hz'
    secerete = '9TIlUflHjZTEHJsxKY2rTQNTJVroUsBo'
    import uuid
    uuid = uuid.uuid4()
    api_endpoint = 'https://openspeech.bytedance.com/api/v3/auc/bigmodel/submit'

    # 上传的音频文件路径

    # API 请求头
    headers = {
        'Authorization': f'Bearer;{access_token}',
        'Content-Type': 'application/json',
        'X-Api-App-Key':appid,
        'X-Api-Access-Key':access_token,
        'X-Api-Resource-Id':'volc.bigasr.auc',
        'X-Api-Request-Id':str(uuid),
        'X-Api-Sequence':str(-1)
    }

    body_content ={
        
        "user": {
            "uid": "388808087185088"
        },
        "request": {
            "model_name": "bigmodel",
            "enable_itn": True
        },
        "audio": {
            "format": "wav",
            "url": url
        }
    }

    response = requests.post(api_endpoint, json=body_content, headers=headers)
    # uuid = response.headers.get('X-Tt-Logid')
    print(uuid)
    print(response.headers.get('X-Api-Message'))
    print(response.headers.get('X-Api-Status-Code'))
    # returns
    # print(response)
    # 火山引擎API信息
    appid = '2166725073'
    access_token = 'v8MEhYaZ4dCjAb6sFOlNQBjb2Z_8c-Hz'
    secerete = '9TIlUflHjZTEHJsxKY2rTQNTJVroUsBo'
    api_endpoint = 'https://openspeech.bytedance.com/api/v3/auc/bigmodel/query'


    
    headers = {
        'Authorization': f'Bearer;{access_token}',
        'Content-Type': 'application/json',
        'X-Api-App-Key':appid,
        'X-Api-Access-Key':access_token,
        'X-Api-Resource-Id':'volc.bigasr.auc',
        'X-Api-Request-Id':str(uuid),
        # 'X-Api-Sequence':str(-1)
    }
    # body_content ={
    #     "appid": appid,
    #     "token": access_token,
    #     "cluster": cluster,
    #     "id": response['resp']['id']
    #     # "id":"f0b3f2a8-fab4-4826-9a60-09b5e1722909"
    # }

    body_content = {}
    response = requests.post('https://openspeech.bytedance.com/api/v3/auc/bigmodel/query', 
    json=body_content, headers=headers)
    print(response.json())
    while len(response.json()['result']['text'])==0:
        response = requests.post('https://openspeech.bytedance.com/api/v3/auc/bigmodel/query', 
        json=body_content, headers=headers)
    
    print(response.json())
    # while len(response.json()['resp']['text']) == 0:
    #     response = requests.post('https://openspeech.bytedance.com/api/v1/auc/query', 
    # json=body_content, headers=headers)
    # response = response.json()
    # print(response)
    answer[now_path].append(response.json()['result']['text'])

    # 将列表内容写入文件
with open('test.json', 'w') as f:
    json.dump(answer, f, indent=4, ensure_ascii=False)
print("文件已保存为t")
end_time = time.time()
# 计算时间差
elapsed_time = end_time - start_time
print(f"代码运行时间: {elapsed_time}秒")