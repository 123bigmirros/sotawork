import hmac
from hashlib import sha1
import base64
import time
import uuid

def make_sign():
    """
    生成签名
    """

    # API访问密钥
    secret_key = 'isNsd1L9yfHLMM4MUks_NRQ7avMlP55J'
    #/api/generate/webui/text2img
    # 请求API接口的uri地址
    # uri = "/api/model/version/get"
    uri = "/api/generate/webui/text2img"
    uri = "/api/generate/webui/status"
    uri = "/api/generate/webui/img2img"
    # 当前毫秒时间戳
    timestamp = str(int(time.time() * 1000))
    # 随机字符串
    signature_nonce= str(uuid.uuid4())
    # 拼接请求数据
    content = '&'.join((uri, timestamp, signature_nonce))

    # 生成签名
    digest = hmac.new(secret_key.encode(), content.encode(), sha1).digest()
    # 移除为了补全base64位数而填充的尾部等号
    sign = base64.urlsafe_b64encode(digest).rstrip(b'=').decode()
    result = f'?AccessKey=dJsFLZRidcsf1cSlBwzeSQ&Signature={sign}&Timestamp={timestamp}&SignatureNonce={signature_nonce}'
    return result 
import pyperclip  
pyperclip.copy(make_sign())
