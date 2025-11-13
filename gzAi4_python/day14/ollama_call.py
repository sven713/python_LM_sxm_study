



import ollama


if __name__ == '__main__':
    """
        同学们拿我的代码运行，可能会报错，可能的报错原因如下：
            1- 本地的Ollama软件没有启动运行
            2- 本地没有qwen2:0.5b大模型
    """
    response = ollama.chat(model="qwen:0.5b",messages=[{"role":"user","content":"广州有什么好吃的？"}])
    print(response, type(response))
    print(response.message.content)