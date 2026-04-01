streamlit
openai
 import streamlit as st
from openai import OpenAI

# Configuração visual do seu site
st.set_page_config(page_title="IA Lucrativa", page_icon="💰")
st.title("🤖 Gerador de Conteúdo para Venda")
st.markdown("---")

# Barra lateral para configurar a "Chave da IA"
st.sidebar.header("Configuração")
api_key = st.sidebar.text_input("Cole sua OpenAI API Key aqui:", type="password")

if not api_key:
    st.info("💡 Para começar, cole sua API Key da OpenAI na barra lateral esquerda.")
    st.stop()

# Inicializa a IA com a sua chave
client = OpenAI(api_key=api_key)

# Opções de serviços que você pode vender
servico = st.selectbox("O que você quer criar para seu cliente?", 
                      ["Legenda para Instagram", "Descrição de Produto (E-commerce)", "Roteiro de Vídeo Curto", "E-mail Marketing"])

detalhes = st.text_area("Descreva o que o cliente pediu (ex: Loja de sapatos, promoção de 20%):")

if st.button("Gerar Conteúdo Agora"):
    if detalhes:
        with st.spinner('A IA está criando o texto...'):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": f"Você é um especialista em vendas. Crie um {servico} profissional."},
                        {"role": "user", "content": detalhes}
                    ]
                )
                texto_final = response.choices.message.content
                st.success("✅ Conteúdo gerado com sucesso!")
                st.markdown("### Resultado:")
                st.write(texto_final)
                st.download_button("Baixar Texto", texto_final)
            except Exception as e:
                st.error(f"Erro na chave da API: {e}")
    else:
        st.warning("Por favor, descreva o que você quer criar.")

st.markdown("---")
st.caption("Dica: Venda este serviço em sites como VinteConto ou Workana.")
