import streamlit as st
import openai

st.title("💰 Meu Gerador de Grana")

# Pede a chave para funcionar
chave = st.text_input("Cole sua Chave API aqui:", type="password")

if chave:
    client = openai.OpenAI(api_key=chave)
    tema = st.text_input("Sobre o que quer escrever?")
    
    if st.button("Gerar Texto"):
        # Comando que pede para a IA escrever
        chamada = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Crie um texto de venda sobre: {tema}"}]
        )
        st.write(chamada.choices[0].message.content)
else:
    st.write("Coloque a chave na caixa acima para o site ligar!")
