import streamlit as st

st.set_page_config(page_title="Apresentando Mikael", layout="wide")

# MENU LATERAL
st.sidebar.title("📌 Menu")
opcao = st.sidebar.radio(
    "Escolha uma opção:",
    ["Seja Bem-Vindo", "Projeto Acadêmico"],
)

# ==============================
# 🔹 TELA INICIAL
# ==============================
if opcao == "Seja Bem-Vindo":
    st.title("👋 Seja Bem-Vindo")

    st.write("""
    Este ambiente foi desenvolvido para apresentar minhas competência e Projeto Acadêmico de Análise e Desenvolvimento de Sistemas (3º semestre).
    """)

    st.markdown("---")

    st.subheader("🎯 Objetivo")
    st.write("""
    Demonstração simples e direta para o avaliador.
    """)

# ==============================
# 🚀 PROJETO ACADÊMICO
# ==============================
elif opcao == "Projeto Acadêmico":
    st.title("🚀 Projeto Acadêmico")

    st.write("""
    Este projeto foi desenvolvido com o objetivo de aplicar conceitos de finanças básicas de forma prática, utilizando organização no Trello e Desenvolvimento em código de aplicativo pratico.(Pode ampliar imagens clicando nela na parte superior direta).
    """)

    st.markdown("---")

    # 🔹 TRELLO
    st.subheader("📋 Organização do Projeto (Trello)")
    st.write("Desenvovimento no Trello.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("Trello.png",
                 caption="Visão geral do quadro no Trello.",
                 use_container_width=True)

    with col2:
        st.image("Trello02.png",
                 caption="Organização Incio da Apresentação.",
                 use_container_width=True)

    with col3:
        st.image("Trello03.png",
                 caption="Final apresentação pelo Trello.",
                 use_container_width=True)

    st.markdown("---")

    # 🔹 CÓDIGO
    st.subheader("💻 Demostração Apricativo Pratico")

    col1, col2 = st.columns(2)

    with col1:
        st.image("codigo1.png", caption="Funcionalmento inicial.", use_container_width=True)
        st.image("codigo2.png", caption="Lógica principal.", use_container_width=True)

    with col2:
        st.image("codigo3.png", caption="Organização e apresntação informações.", use_container_width=True)
        st.image("codigo4.png", caption="Resultado final.", use_container_width=True)

    st.markdown("---")

    # 🔹 PORTFÓLIO
    st.subheader("🌐 Portfólio Pessoal.")

    col1, col2 = st.columns(2)

    with col1:
        st.image("portfolio1.png", caption="Tela inicial.", use_container_width=True)
        st.image("portfolio2.png", caption="Me apresetando.", use_container_width=True)

    with col2:
        st.image("portfolio3.png", caption="Certificações.", use_container_width=True)

    st.markdown("---")

    # 🔹 AULAS
    st.subheader("📚 Aulas")

    col1, col2 = st.columns(2)

    with col1:
        st.image("aula1.png", caption="Atividade na prática.", use_container_width=True)
        st.image("aula2.png", caption="Explicação.", use_container_width=True)

    with col2:
        st.image("aula3.png", caption="Apricativo.", use_container_width=True)
        st.image("aula4.png", caption="Final da Apresetnação.", use_container_width=True)
        
        # 🎥 VÍDEO (AQUI NO FINAL DAS AULAS)
st.markdown("---")

st.subheader("🎥 Demonstração em Aula")

st.write("""
Registro da aplicação prática do projeto durante a aula de educação financeira,
utilizando o sistema como ferramenta de apoio.
""")

st.video("video.mp4")
