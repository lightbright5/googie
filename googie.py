import streamlit as st
import openai

api_key = st.secrets["api_key"]
openai.api_key = api_key

# Function to get chat completion
def get_chat_completion(user_prompt, system_role=(
    'I need an answer to my question. It doesn\'t matter if it\'s wrong, but make it hilariously wrong. '
    'Channel the humor of George Carlin—sharp, witty, and a little irreverent.'
), model='gpt-3.5-turbo', temperature=1):
    messages = [
        {'role': 'system', 'content': system_role},
        {'role': 'user', 'content': user_prompt}
    ]
    
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message['content']

st.title('Welcome to Googie!!!')

my_select_box = st.sidebar.selectbox('Select Output Tone:', ['Funny', 'Serious'])

user_input = st.text_input("Enter some text:")

if st.button('Submit'):
    response = get_chat_completion(user_prompt=user_input)
    st.write(f'GPT Response: {response}')


