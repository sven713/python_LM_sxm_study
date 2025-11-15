
import streamlit as st
import backend


if __name__ == '__main__':
  st.title('sv的AI聊天机器人')

  prompt = st.chat_input('请输入你的问题:')

  if(prompt):
    res = backend.get_response(prompt)

    st.chat_message('assistant').markdown(res)



