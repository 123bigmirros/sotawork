"""
baidu voice service
"""
import base64
import json
import os
import time
import urllib

import requests
from aip import AipSpeech



"""
    百度的语音识别API.
    dev_pid:
        - 1936: 普通话远场
        - 1536：普通话(支持简单的英文识别)
        - 1537：普通话(纯中文识别)
        - 1737：英语
        - 1637：粤语
        - 1837：四川话
    要使用本模块, 首先到 yuyin.baidu.com 注册一个开发者账号,
    之后创建一个新应用, 然后在应用管理的"查看key"中获得 API Key 和 Secret Key
    然后在 config.json 中填入这两个值, 以及 app_id, dev_pid
    """


class BaiduVoice():
    def __init__(self):
        try:
            curdir = os.path.dirname(__file__)
            config_path = os.path.join(curdir, "config.json")
            bconf = None
            if not os.path.exists(config_path):  # 如果没有配置文件，创建本地配置文件
                bconf = {"lang": "zh", "ctp": 1, "spd": 5, "pit": 5, "vol": 5, "per": 0}
                with open(config_path, "w") as fw:
                    json.dump(bconf, fw, indent=4)
            else:
                with open(config_path, "r") as fr:
                    bconf = json.load(fr)

            self.app_id = "76866322"
            self.api_key = "7eQYVeX7TJLO91tp7kq2jtbu"
            self.secret_key = "tN7ntIFWJCtonb835CeRkyTNT7ZXvme5"
            self.dev_id = "1737"
            self.lang = "zh"
            self.ctp = 1
            self.spd = 5
            self.pit = 5
            self.vol = 5
            self.per = 0

            self.client = AipSpeech(self.app_id, self.api_key, self.secret_key)
        except Exception as e:
            print("BaiduVoice init failed: %s, ignore " % e)

    def get_access_token(self):
        """
        使用 AK，SK 生成鉴权签名（Access Token）
        :return: access_token，或是None(如果错误)
        """
        url = "https://aip.baidubce.com/oauth/2.0/token"
        params = {"grant_type": "client_credentials", "client_id": self.api_key, "client_secret": self.secret_key}
        res = str(requests.post(url, params=params).json().get("access_token"))
        return res

    def get_file_content_as_base64(self, path):
        """
        获取文件base64编码
        :param path: 文件路径
        :param urlencoded: 是否对结果进行urlencoded
        :return: base64编码信息
        """
        with open(path, "rb") as f:
            res = f.read()
            file_len = len(res)
            content = str(base64.b64encode(res),'utf-8')
        return content,file_len

   



    def voiceToText(self, voice_file):
        # 识别本地文件
        import wave
        def get_pcm_from_wav(wav_path):
            """
            从 wav 文件中读取 pcm

            :param wav_path: wav 文件路径
            :returns: pcm 数据
            """
            wav = wave.open(wav_path, "rb")
            return wav.readframes(wav.getnframes())
        
        pcm = get_pcm_from_wav(voice_file)
        pcm_base = base64.b64encode(pcm)

        res = self.client.asr(pcm, "pcm", 16000, {"dev_pid": self.dev_id})
        if res["err_no"] == 0:
            
            text = "".join(res["result"])
            print(text)
            return text
        else:
            
            print("hello")

    


import time

# 记录代码开始的时间
start_time = time.time()


if __name__ == "__main__":
    answer = {}
    baidu_voice = BaiduVoice()
    def list_files_in_directory(directory):
        for root, dirs, files in os.walk(directory):
            for file in files:
                # 获取文件的绝对路径
                absolute_path = os.path.join(root, file)
                yield absolute_path
    for path in list_files_in_directory("/Users/mz/Desktop/Learn/knowledge/computer/ML/实习/sotawork/语音转文本/test语音"):

        answer[path] = baidu_voice.voiceToText(path)
    with open('baidu_test.json', 'w') as f:
        json.dump(answer, f, indent=4, ensure_ascii=False)
    # baidu_voice.textToVoice("你好，欢迎使用语音助手")

# 记录代码结束的时间
end_time = time.time()

# 计算并输出运行时间
execution_time = end_time - start_time
print(f"代码运行时间: {execution_time}秒")