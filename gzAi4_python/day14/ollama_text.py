
import ollama

# while True:
#   promt = input('请输入问题')
#   response = ollama.chat(model='qwen:0.5b', messages=[{
#     'role':'user',
#     'content':promt
#   }])
#   print(response.message.content)

prompt = '写一段python代码, 求两个数最大公约数'

result = ollama.chat(model='qwen:0.5b', messages=[{
  'role':'user',
  'content':prompt}
])

print(result.message.content)
