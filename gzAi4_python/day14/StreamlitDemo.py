import streamlit as st

prompt = st.chat_input('请输入你的问题!!')

if prompt:

  # st.write(f'你的问题是:{prompt}')
  with st.chat_message('user'):
    st.write(prompt)





# 使用 st.chat_message 创建一个消息容器，用于显示回复消息
message = st.chat_message('assistant')
# 在消息容器中显示文本 'Hello Human'，模拟助手的回复
message.write('Hello Human')

