import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["api_key"])

# Function to get chat completion using the new API method
def get_chat_completion(user_prompt, system_role=(
    'I need an answer to my question. It doesn\'t matter if it\'s wrong, but make it hilariously wrong. '
    'Channel the humor of George Carlin—sharp, witty, and a little irreverent.'
), model='gpt-3.5-turbo', temperature=1):
    messages = [
        {'role': 'system', 'content': system_role},
        {'role': 'user', 'content': user_prompt}
    ]
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature
        )
        return response.choices[0].message['content']
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Streamlit App
st.title('Welcome to Googie!!!')

my_select_box = st.sidebar.selectbox('Select Output Tone:', ['Funny', 'Serious'])

user_input = st.text_input("Enter some text:")

if st.button('Submit'):
    response = get_chat_completion(user_prompt=user_input)
    
    if response:
        st.write(f'GPT Response: {response}')
