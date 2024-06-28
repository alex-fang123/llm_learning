"""
    根据智谱AI官方文档，可以方便地添加搜索功能
    这个有很多问题，比如，只在第一次回复时候进行了搜索，这样会导致后续ref_list行直接报错——因为没有web_search这个key
    此外，它会出现“搜索的网站的信息是对的，但是回答出来的答案是错误的”这种情况
"""

from rich.console import Console
from rich.markdown import Markdown
from zhipuai import ZhipuAI

system_prompt_template = {"role": "system",
                          "content": "现在你是一个生活秘书，你需要做的就是回答用户的问题，如果你不知道答案，可以告诉用户你不知道。"}

history = [system_prompt_template, ]

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
        tools=[
            {
                "type": "web_search",
                "web_search": {
                    "enable": True,
                    "search_result": True,
                }
            },
        ],
    )
    assistant_prompt = {"role": "assistant", "content": f"{response.choices[0].message.content}"}
    history.append(assistant_prompt)
    ref_list = [response.model_extra['web_search'][i]['link'] for i in range(len(response.model_extra['web_search']))]
    return_message = Markdown(history[-1]['content'] + "\n\n" + "参考网站列表：\n\n" + "\n".join(ref_list))
    console.print(return_message)
