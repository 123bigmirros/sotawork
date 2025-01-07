import json
def huoshan_data():
    # 读取json文件 
    result = {}
    with open('/Users/mz/Desktop/Learn/knowledge/computer/ML/实习/sotawork/huoshan_output.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for key in data.keys():
        result[key.split('/')[-1]] = data[key][0]["resp"]['text']
    return result

def keda_data():
    # 读取json文件 
    result = {}
    with open('/Users/mz/Desktop/Learn/knowledge/computer/ML/实习/sotawork/keda.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for key in data.keys():
        text = ""
        texts_dict = data[key]
        # print(texts_dict)
        for t in texts_dict:
            t = json.loads(t)
            for tt in t:
                for ttt in tt["cw"]:
                    

                    text += ttt["w"]
        result[key.split('/')[-1] ]= text
    return result

def baidu_data():
    with open('/Users/mz/Desktop/Learn/knowledge/computer/ML/实习/sotawork/baidu.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    result = {}
    for key in data.keys():
        result[key.split('/')[-1]] = data[key]
    return result
hs_data = huoshan_data()
print(len(hs_data.keys()))
kd_data = keda_data()
print(len(kd_data.keys()))
bd_data = baidu_data()
print(len(bd_data.keys()))

import pandas as pd
print('wocao')
dc = [hs_data,kd_data,bd_data]
df = pd.DataFrame(dc, index=['火山','科大讯飞','百度'],columns=bd_data.keys())
print(df.head())
df = df.T
df.to_csv('result.csv')

