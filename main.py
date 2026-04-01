import streamlit as st
from openai import OpenAI

# Configuração da Página
st.set_page_config(page_title="Gerador de Grana com IA", page_icon="💰")
st.title("🤖 Assistente de Conteúdo Lucrativo")
st.write("Crie textos de alta conversão e venda para clientes!")

# Aqui você insere sua chave da API da OpenAI
# Pegue a sua em: https://openai.com
api_key = st.sidebar.text_input("Insira sua OpenAI API Key", type="password")

if api_key:
    client = OpenAI(api_key=api_key)
    
    servico = st.selectbox("O que você quer vender hoje?", 
                          ["Legendas para Instagram", "Roteiro de TikTok", "Descrição de Produto (E-commerce)"])
    
    detalhes = st.text_area("Sobre o que é o conteúdo?")
    
    if st.button("Gerar Conteúdo para Venda"):
        with st.spinner('A IA está trabalhando para você...'):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"Você é um expert em marketing. Crie um {servico}."},
                    {"role": "user", "content": detalhes}
                ]
            )
            resultado = response.choices[0].message.content
            st.success("Conteúdo Pronto!")
            st.write(resultado)
            st.download_button("Baixar Texto", resultado)
else:
    st.warning("Coloque sua API Key na barra lateral para começar a faturar.")
