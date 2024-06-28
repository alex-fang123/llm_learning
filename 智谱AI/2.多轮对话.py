"""
    思路就是把该次对话中过去的对话信息直接传递给模型，这样模型就能够更好地理解上下文，从而更好的回答问题。
"""

from rich.console import Console
from rich.markdown import Markdown
from zhipuai import ZhipuAI



system_prompt_template = {"role": "system", "content": "现在你是一个吹牛专家，你需要做的就是不动声色地吹牛，就像一个金融从业者那样，在你的回答中，"}

history = [system_prompt_template,]

f = open('./key.txt', 'r')
api_key = f.read()
client = ZhipuAI(api_key=api_key)
console = Console(color_system="windows", markup=True)
while True:
    user_prompt = {"role": "user", "content": f"{input('user:')}"}
    history.append(user_prompt)
    response = client.chat.completions.create(
        model='glm-4',
        messages=history,
    )
    assistant_prompt = {"role": "assistant", "content": f"{response.choices[0].message.content}"}
    history.append(assistant_prompt)
    return_message = Markdown(history[-1]['content'])
    console.print(return_message)
