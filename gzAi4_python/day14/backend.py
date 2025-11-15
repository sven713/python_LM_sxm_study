
import ollama


def get_response(prompt):

  
  response = ollama.chat(model="qwen:0.5b",messages=[{"role":"user","content":prompt}])
  # print(response, type(response))
  # print(response.message.content)
  return response.message.content


# if __name__ == '__main__':
#   prompt = '孙悟空是谁'

#   res = get_response(prompt)
#   print(res)

