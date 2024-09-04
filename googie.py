import streamlit as st
import openai

from openai import OpenAI
client = OpenAI()



def get_chat_completion(user_prompt, system_role=
'I need an answer to my question. It doesn\'t matter if it\'s wrong, but make it hilariously wrong. Channel the humor of George Carlin—sharp, witty, and a little irreverent.'
,model='gpt-3.5-turbo', temperature=1):
    messages = [
        {'role': 'system', 'content': system_role},
        {'role': 'user', 'content': user_prompt}
    ]
    
    response = client.chat.completions.create(
        model=model,
        messages= messages,
        temperature=temperature
    )
    return response.choices[0].message.content

api_key = st.secrets["api_key"]

os.environ['OPENAI_API_KEY'] = api_key

st.title('Welcome to Googie!!!')

my_select_box = st.sidebar.selectbox('Select Output Tone:', list(['Funny', 'Serious']) )

user_input = st.text_input("Enter some text:")

if st.button('Submit'):

    response = get_chat_completion(user_prompt=user_input)

    st.write(f'GPT Response: {response}')



# Title of the app

# Create a text input field

