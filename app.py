import streamlit as st
import requests
import json

# Configurar la API key desde los secrets
API_URL = "https://api.together.xyz/v1/chat/completions"
API_KEY = st.secrets["TOGETHER_API_KEY"]

# Definir el prompt
prompt = """
Context: You are immersed in the dynamic world of contemporary philosophy, where ideas and thinkers continually shape our understanding of reality, ethics, and society. The landscape of modern philosophy is vast and ever-evolving, with numerous philosophers contributing groundbreaking ideas across various sub-disciplines. To navigate this complex terrain and provide insightful guidance, a structured approach is essential. Your task is to create a comprehensive guide that introduces and explains the thought of the ten most prominent philosophers of our time. This guide will serve as a foundational resource for students, educators, and enthusiasts seeking to understand the cutting-edge developments in philosophy.

Role: You are a distinguished tutor of philosophy with over two decades of experience in academia. Your expertise spans the entire spectrum of philosophical thought, with a particular focus on contemporary philosophy. You are renowned for your ability to distill complex ideas into accessible and engaging explanations. Your thought leadership is evident in your numerous publications, keynote speeches, and innovative teaching methods. You possess an encyclopedic knowledge of the works and contributions of the most influential philosophers of our era.

Action:
1. Identify the Top Ten Contemporary Philosophers: Begin by compiling a list of the ten most prominent philosophers of the present day. These philosophers should be selected based on their significant contributions to the field, the impact of their ideas, and their influence on academic and public discourse.
2. Provide Biographical Information: For each philosopher, provide a brief biography that includes their birthdate, educational background, notable achievements, and any relevant personal or professional milestones.
3. Summarize Key Contributions: Outline the key contributions of each philosopher to the field of philosophy. This should include their most important works, theories, and concepts, as well as their impact on philosophical thought and other disciplines.
4. Explain Core Ideas: For each philosopher, explain their core ideas in a clear and concise manner. Use examples and analogies to illustrate complex concepts and make them accessible to a broader audience.
5. Contextualize Their Work: Place each philosopher's work within the broader context of contemporary philosophy. Discuss how their ideas relate to those of other prominent philosophers and how they have influenced or been influenced by broader intellectual and cultural trends.
6. Provide Critical Evaluation: Offer a critical evaluation of each philosopher's work, highlighting both its strengths and weaknesses. Discuss any controversies or debates surrounding their ideas and how they have been received within the philosophical community.
7. Include References and Further Reading: For each philosopher, provide a list of key references and further reading materials. This should include their most important works, as well as secondary sources that offer in-depth analyses of their ideas.
8. Organize Information: Ensure that the information is organized in a logical and coherent manner. Use headings, subheadings, and bullet points to make the guide easy to navigate and understand.
9. Review and Edit: Carefully review and edit the guide to ensure accuracy, clarity, and consistency. Make sure that the explanations are accessible to the target audience and that the guide is free of errors.
10. Format for Accessibility: Ensure that the guide is formatted in a way that is accessible and user-friendly. Use clear and concise language, and avoid unnecessary jargon. Include visual aids, such as diagrams and charts, where appropriate to enhance understanding.

Format: The guide should be presented in a structured and organized format, with each philosopher's section following a consistent template.
"""

# Interfaz de usuario de Streamlit
st.title("Contemporary Philosophy Guide Generator")
st.write("Genera una guía detallada sobre los filósofos contemporáneos más destacados.")

# Botón para generar la guía
if st.button("Generar Guía de Filosofía"):
    # Llamada a la API
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-ai/DeepSeek-R1",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 3000,
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "repetition_penalty": 1.0,
        "stop": ["<\u2758end\u2758of\u2758sentence\u2758>"]
    }

    response = requests.post(API_URL, headers=headers, json=data, stream=True)

    if response.status_code == 200:
        st.success("Guía generada exitosamente.")
        guide_content = ""
        for line in response.iter_lines():
            if line:
                guide_content += line.decode("utf-8") + "\n"
        st.text_area("Guía Generada", guide_content, height=500)
    else:
        st.error("Error al generar la guía. Intenta nuevamente.")
