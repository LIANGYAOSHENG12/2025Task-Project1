client = OpenAI(api_key=api_key, base_url=base_url)  # 初始化 OpenAI 客户端

history = []  # 初始化对话历史记录

num1 = 0  # 初始化对话次数
mport os
from openai import OpenAI
# ❌如果报错 ModuleNotFoundError，请运行下面的命令行👇
# pip install openai -i https://pypi.tuna.tsinghua.edu.cn/simple

# 💡在远程平台运行时，采用下面两行代码
api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL")

# 💡在本地使用自定义的服务时，采用下面两行代码
# api_key = "你的 API Key"
# base_url = "提供商指定的 Base URL"

client = OpenAI(api_key=api_key, base_url=base_url)  # 初始化 OpenAI 客户端

history = []  # 初始化对话历史记录

num1 = 0 # 初始化对话次数

# 循环多轮对话
while True:
    if num1 <= 3:  # 未达次数时正常运行
        prompt = input()
        if not prompt:
            break  # 输入为空时退出
    else:
        prompt = "我准备要清空我们的历史对话记录了，请你为了确保清空记录后仍能衔接上我的下一句对话内容，并且不失去我的和我所说的重要信息，请你总结一下目前记录中存在的对话内容，在这次回复中，请严格回复：因对话内容过多，我已总结以上对话内容，请继续提问吧"
        num1 = 0  # 清空对话次数
        history = []  # 清空对话历史

    history.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="ernie-x1.1-preview",  # 改成提供商指定的模型名称
        messages=history,
        max_tokens=1000
    )

    answer = response.choices[0].message.content
    history.append({"role": "assistant", "content": answer})
    print(answer)
    num1 += 1  # 次数变化
