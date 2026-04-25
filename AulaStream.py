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
    Este ambiente foi desenvolvido para apresentar minhas competências, certificações
    e projetos acadêmicos ao longo da minha formação em Análise e Desenvolvimento de Sistemas (3º semestre).
    """)

    st.markdown("---")

    st.subheader("🎯 Objetivo Profissional")
    st.write("""
    Atuar na área de tecnologia, com foco em desenvolvimento de sistemas e soluções voltadas
    ao mercado financeiro.
    """)

# ==============================
# 🚀 PROJETO ACADÊMICO
# ==============================
elif opcao == "Projeto Acadêmico":
    st.title("🚀 Projeto Acadêmico")

    st.write("""
    Projeto desenvolvido com foco em organização, desenvolvimento e aplicação prática.
    """)

    st.markdown("---")

    # 🔹 TRELLO
    st.subheader("📋 Organização do Projeto (Trello)")
    st.write("Gerenciamento de tarefas e acompanhamento do progresso.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("Trello.png",
                 caption="Visão geral do quadro no Trello.",
                 use_container_width=True)

    with col2:
        st.image("Trello2.png",
                 caption="Organização das tarefas por etapas.",
                 use_container_width=True)

    with col3:
        st.image("Trello3.png",
                 caption="Acompanhamento do progresso.",
                 use_container_width=True)

    st.markdown("---")

    # 🔹 CÓDIGO
    st.subheader("💻 Código")

    col1, col2 = st.columns(2)

    with col1:
        st.image("codigo1.png", caption="Estrutura inicial.", use_container_width=True)
        st.image("codigo2.png", caption="Lógica principal.", use_container_width=True)

    with col2:
        st.image("codigo3.png", caption="Organização do código.", use_container_width=True)
        st.image("codigo4.png", caption="Melhorias finais.", use_container_width=True)

    st.markdown("---")

    # 🔹 PORTFÓLIO
    st.subheader("🌐 Portfólio")

    col1, col2 = st.columns(2)

    with col1:
        st.image("portfolio1.png", caption="Tela inicial.", use_container_width=True)
        st.image("portfolio2.png", caption="Projetos.", use_container_width=True)

    with col2:
        st.image("portfolio3.png", caption="Apresentação pessoal.", use_container_width=True)

    st.markdown("---")

    # 🔹 AULAS
    st.subheader("📚 Aulas")

    col1, col2 = st.columns(2)

    with col1:
        st.image("aula1.png", caption="Atividade prática.", use_container_width=True)
        st.image("aula2.png", caption="Explicação.", use_container_width=True)

    with col2:
        st.image("aula3.png", caption="Laboratório.", use_container_width=True)
        st.image("aula4.png", caption="Evolução.", use_container_width=True)
