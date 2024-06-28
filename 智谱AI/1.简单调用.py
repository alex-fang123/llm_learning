"""
    用的官方教程里面的
    https://bigmodel.cn/dev/api#glm-4
    就是一个最简单最简单的单次对话
"""

from zhipuai import ZhipuAI

system_prompt = {"role": "system", "content": "现在你是一个吹牛专家，你需要做的就是不动声色地吹牛，就像一个金融从业者那样"}

f = open('./key.txt', 'r')
api_key = f.read()
client = ZhipuAI(api_key=api_key)
response = client.chat.completions.create(
    model='glm-4',
    messages=[
        system_prompt,
        {"role": "user", "content": "你好"},
    ],
)
print(response.choices[0].message.content)
