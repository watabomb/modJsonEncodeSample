# json.dumpsでfloatの小数点以下の桁数を変えたい場合のメモ
# 参考＞https://docs.python.org/ja/3/library/json.html#json.JSONEncoder.default
import json
from json import encoder

class MyEncoder(json.JSONEncoder):
    def encode(self, obj):
        r=''
        for chunk in json.JSONEncoder.iterencode(self, obj):
            try:
                r=r+format(float(chunk), '.2f')
            except:
                r=r+chunk
                pass
        return r

val = {"val1":123.456789, "val2":123.1}
print("default", json.dumps(val))
print("to 2 decimal places ", json.dumps(val, cls=MyEncoder))

