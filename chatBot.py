import streamlit as st
import google.generativeai as genai

# Load API key from Streamlit secrets
genai.configure(api_key=st.secrets["gemini_api_key"])

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

def main():
    st.set_page_config(page_title="Mental-Health-ChatBot", page_icon="🧠")

    st.title("Mental-Health-Chatbot")
    st.write("I'm a your ChatBot, You can find all your problems's solution in just One Click!")

    # Custom CSS for chat messages
    st.markdown("""
    <style>
        .stChatMessage {
            border-radius: 10px;
            padding: 10px;
            margin: 5px 0;
        }
        .stChatMessage.user {
            background-color: #e3f2fd;
        }
        .stChatMessage.assistant {
            background-color: #f5f5f5;
        }
    </style>
    """, unsafe_allow_html=True)

    # Initialize session state for chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    user_input = st.chat_input("Type your message here...")

    if user_input:
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Get response from Gemini
        response = model.generate_content(user_input)
        bot_response = response.text

        # Add bot response to chat history
        st.session_state.chat_history.append({"role": "assistant", "content": bot_response})
        with st.chat_message("assistant"):
            st.markdown(bot_response)

if __name__ == "__main__":
    main()