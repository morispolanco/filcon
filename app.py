import streamlit as st
import requests
import json

# Configurar la API key desde los secrets
API_URL = "https://api.together.xyz/v1/chat/completions"
API_KEY = st.secrets["TOGETHER_API_KEY"]

# Definir el contexto del chatbot
context = """
Context: You are immersed in the dynamic world of contemporary philosophy, where ideas and thinkers continually shape our understanding of reality, ethics, and society. The landscape of modern philosophy is vast and ever-evolving, with numerous philosophers contributing groundbreaking ideas across various sub-disciplines. To navigate this complex terrain and provide insightful guidance, a structured approach is essential. Your task is to create a comprehensive guide that introduces and explains the thought of the ten most prominent philosophers of our time. This guide will serve as a foundational resource for students, educators, and enthusiasts seeking to understand the cutting-edge developments in philosophy.

Role: You are a distinguished tutor of philosophy with over two decades of experience in academia. Your expertise spans the entire spectrum of philosophical thought, with a particular focus on contemporary philosophy. You are renowned for your ability to distill complex ideas into accessible and engaging explanations. Your thought leadership is evident in your numerous publications, keynote speeches, and innovative teaching methods. You possess an encyclopedic knowledge of the works and contributions of the most influential philosophers of our era.
"""

# Interfaz de usuario de Streamlit
st.title("Chatbot de Filosofía Contemporánea")
st.write("Conversa con un tutor experto en filosofía contemporánea. Pregunta sobre filósofos, conceptos y teorías.")

# Entrada del usuario
user_input = st.text_input("Tu pregunta o comentario:", "")

if user_input:
    # Llamada a la API para obtener respuesta
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-ai/DeepSeek-R1",
        "messages": [
            {"role": "system", "content": context},
            {"role": "user", "content": user_input}
        ],
        "max_tokens": 500,
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "repetition_penalty": 1.0,
        "stop": ["<\u2758end\u2758of\u2758sentence\u2758>"]
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        response_data = response.json()
        chatbot_reply = response_data.get('choices', [{}])[0].get('message', {}).get('content', "No tengo una respuesta en este momento.")
        st.write("### Respuesta del Chatbot:")
        st.write(chatbot_reply)
    else:
        st.error("Error al obtener respuesta del chatbot. Intenta nuevamente.")
