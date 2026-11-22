from chatbot_backend import chatbot
from langchain_core.messages import HumanMessage
import streamlit as st

Config = {
    'configurable': {
        'thread_id': 'thread-1'
    }
}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# Conversation history between AI and user
for message in st.session_state['message_history']:
    with st.chat_message(message['Role']):
        st.text(message['content'])


user_input= st.chat_input('Start your day...')

if user_input:
# first add the prompt of user to message history 
    st.session_state['message_history'].append({'Role':'user','content':user_input})

    with st.chat_message('user'):
        st.text(user_input)

    response = chatbot.invoke({'messages': [HumanMessage(content=user_input)]},config=Config)
    AI_input = response['messages'][-1].content

    if isinstance(AI_input, list):
        AI_input = "".join(
            item["text"]
            for item in AI_input
            if isinstance(item, dict) and item.get("type") == "text"
        )

# first add the prompt of user to message history 
    st.session_state['message_history'].append({'Role':'user','content':AI_input})

    with st.chat_message('AI'):
        st.text(AI_input)