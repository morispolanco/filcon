import streamlit as st
import requests
import json

# Configurar la API key desde los secrets
API_URL = "https://api.together.xyz/v1/chat/completions"
API_KEY = st.secrets["TOGETHER_API_KEY"]

# Definir el contexto del chatbot
contexto = """
Contexto: Estás inmerso en el mundo dinámico de la filosofía contemporánea, donde las ideas y los pensadores moldean continuamente nuestra comprensión de la realidad, la ética y la sociedad. El panorama de la filosofía moderna es vasto y en constante evolución, con numerosos filósofos que contribuyen con ideas revolucionarias en diversas subdisciplinas. Para navegar por este terreno complejo y ofrecer una guía útil, es esencial un enfoque estructurado. Tu tarea es crear una guía completa que introduzca y explique el pensamiento de los diez filósofos más destacados de nuestro tiempo. Esta guía servirá como un recurso fundamental para estudiantes, educadores y entusiastas que buscan comprender los desarrollos más avanzados en la filosofía.

Rol: Eres un tutor distinguido de filosofía con más de dos décadas de experiencia en el mundo académico. Tu experiencia abarca todo el espectro del pensamiento filosófico, con un enfoque particular en la filosofía contemporánea. Eres conocido por tu habilidad para simplificar ideas complejas y hacerlas accesibles y atractivas. Tu liderazgo intelectual es evidente en tus numerosas publicaciones, conferencias magistrales y métodos de enseñanza innovadores. Posees un conocimiento enciclopédico sobre las obras y contribuciones de los filósofos más influyentes de nuestra época.
"""

# Interfaz de usuario de Streamlit
st.title("Chatbot de Filosofía Contemporánea")
st.write("Conversa con un tutor experto en filosofía contemporánea. Pregunta sobre filósofos, conceptos y teorías.")

# Entrada del usuario
entrada_usuario = st.text_input("Tu pregunta o comentario:", "")

if entrada_usuario:
    # Llamada a la API para obtener respuesta
    encabezados = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    datos = {
        "model": "deepseek-ai/DeepSeek-R1",
        "messages": [
            {"role": "system", "content": contexto},
            {"role": "user", "content": entrada_usuario}
        ],
        "max_tokens": 3000,
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "repetition_penalty": 1.0,
        "stop": ["<\u2758end\u2758of\u2758sentence\u2758>"]
    }

    respuesta = requests.post(API_URL, headers=encabezados, json=datos)

    if respuesta.status_code == 200:
        datos_respuesta = respuesta.json()
        respuesta_chatbot = datos_respuesta.get('choices', [{}])[0].get('message', {}).get('content', "No tengo una respuesta en este momento.")
        st.write("### Respuesta del Chatbot:")
        st.write(respuesta_chatbot)
    else:
        st.error("Error al obtener respuesta del chatbot. Intenta nuevamente.")
