import streamlit as st

st.set_page_config(page_title="Apresentando Mikael", layout="wide")

# MENU LATERAL (apenas 1 aba ativa visualmente)
st.sidebar.title("📌 Menu")
opcao = st.sidebar.radio(
    "Navegação:",
    ["Seja Bem-Vindo"],
)

# ==============================
# 🔹 ÚNICA TELA
# ==============================
if opcao == "Seja Bem-Vindo":

    st.title("👋 Seja Bem-Vindo")

    st.write("""
    Este ambiente foi desenvolvido para apresentar minhas competências e o projeto acadêmico
    de Análise e Desenvolvimento de Sistemas (3º semestre).
    """)

    st.markdown("---")

    st.subheader("🎯 Objetivo")
    st.write("""
    Demonstração simples e direta para avaliação do projeto e apresentação das atividades desenvolvidas.
    """)

    st.markdown("---")

    # ==============================
    # 🚀 PROJETO ACADÊMICO
    # ==============================

    st.title("🚀 Projeto Acadêmico")

    st.write("""
    Este projeto foi desenvolvido com o objetivo de aplicar conceitos de finanças básicas de forma prática,
    utilizando organização no Trello e desenvolvimento de um aplicativo funcional.(Para ampliar imagens, click no canto direto da imagem). 
    """)

    st.markdown("---")

    # 🔹 TRELLO
    st.subheader("📋 Organização do Projeto (Trello)")
    st.write("Desenvolvimento e organização das etapas do projeto no Trello.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("Trello.png",
                 caption="Visão geral do quadro no Trello.",
                 use_container_width=True)

    with col2:
        st.image("Trello02.png",
                 caption="Organização inicial da apresentação.",
                 use_container_width=True)

    with col3:
        st.image("Trello03.png",
                 caption="Finalização e conclusão das atividades no Trello.",
                 use_container_width=True)

    st.markdown("---")

    # 🔹 CÓDIGO
    st.subheader("💻 Demonstração do Aplicativo Prático")

    col1, col2 = st.columns(2)

    with col1:
        st.image("codigo1.png", caption="Funcionamento inicial.", use_container_width=True)
        st.image("codigo2.png", caption="Lógica principal.", use_container_width=True)

    with col2:
        st.image("codigo3.png", caption="Organização das informações.", use_container_width=True)
        st.image("codigo4.png", caption="Resultado final do sistema.", use_container_width=True)

    st.markdown("---")

    # 🔹 PORTFÓLIO
    st.subheader("🌐 Portfólio Pessoal")

    col1, col2 = st.columns(2)

    with col1:
        st.image("portfolio1.png", caption="Tela inicial.", use_container_width=True)
        st.image("portfolio2.png", caption="Apresentação pessoal.", use_container_width=True)

    with col2:
        st.image("portfolio3.png", caption="Certificações.", use_container_width=True)

    st.markdown("---")

    # 🔹 AULAS
    st.subheader("📚 Aulas")

    col1, col2 = st.columns(2)

    with col1:
        st.image("aula1.png", caption="Atividade prática.", use_container_width=True)
        st.image("aula2.png", caption="Explicação.", use_container_width=True)

    with col2:
        st.image("aula3.png", caption="Aplicação prática.", use_container_width=True)
        st.image("aula4.png", caption="Finalização da apresentação.", use_container_width=True)

    st.markdown("---")

    # 🎥 VÍDEO
    st.subheader("🎥 Demonstração em Aula")

    st.write("""
    Registro da participação presencial na aula de educação financeira, realizada no local do projeto.
    Foram utilizados equipamentos pessoais, como notebook e cabos, para apoio na execução da atividade.
    """)

    st.video("Video.mp4")
