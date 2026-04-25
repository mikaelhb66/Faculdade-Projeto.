import streamlit as st

st.set_page_config(page_title="Apresentando Mikael", layout="wide")

# MENU LATERAL (apenas 2 abas)
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

    Aqui você encontrará exemplos práticos das minhas habilidades em desenvolvimento,
    organização de projetos e aplicação de tecnologia na resolução de problemas reais.
    """)

    st.markdown("---")

    st.subheader("🎯 Objetivo Profissional")
    st.write("""
    Atuar na área de tecnologia, com foco em desenvolvimento de sistemas e soluções voltadas
    ao mercado financeiro, aplicando boas práticas de programação, organização de código
    e uso de ferramentas modernas para criação de sistemas eficientes.
    """)

# ==============================
# 🚀 PROJETO ACADÊMICO
# ==============================
elif opcao == "Projeto Acadêmico":
    st.title("🚀 Projeto Acadêmico")

    st.write("""
    Este projeto foi desenvolvido com o objetivo de aplicar na prática os conhecimentos adquiridos
    durante o curso, envolvendo organização, desenvolvimento e apresentação de um sistema funcional.

    Durante sua construção, utilizei ferramentas de apoio, incluindo inteligência artificial,
    para otimizar o desenvolvimento e melhorar a qualidade do código.
    """)

    st.markdown("---")

    # 🔹 TRELLO
    st.subheader("📋 Organização do Projeto (Trello)")
    st.write("""
    O planejamento e acompanhamento das atividades foram realizados utilizando o Trello,
    permitindo melhor organização das tarefas, definição de prioridades e controle do progresso.
    """)

    st.image("imagens/trello.png",
             caption="Quadro do Trello utilizado para organização das tarefas do projeto, incluindo etapas de desenvolvimento, revisão e conclusão.",
             use_container_width=True)

    st.markdown("---")

    # 🔹 CÓDIGO
    st.subheader("💻 Estrutura e Desenvolvimento do Código")
    st.write("""
    O código foi estruturado de forma modular, buscando clareza, organização e facilidade de manutenção.
    Abaixo estão alguns trechos representando diferentes partes do desenvolvimento.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.image("imagens/codigo1.png",
                 caption="Estrutura inicial do projeto, incluindo importação de bibliotecas e configuração base.",
                 use_container_width=True)

        st.image("imagens/codigo2.png",
                 caption="Implementação da lógica principal do sistema, responsável pelo funcionamento das funcionalidades.",
                 use_container_width=True)

    with col2:
        st.image("imagens/codigo3.png",
                 caption="Organização das funções e separação de responsabilidades dentro do código.",
                 use_container_width=True)

        st.image("imagens/codigo4.png",
                 caption="Ajustes finais e melhorias aplicadas para otimização e padronização do sistema.",
                 use_container_width=True)

    st.markdown("---")

    # 🔹 PORTFÓLIO
    st.subheader("🌐 Desenvolvimento do Portfólio")
    st.write("""
    O portfólio foi desenvolvido com o objetivo de apresentar de forma clara e profissional
    as competências adquiridas, bem como os projetos realizados ao longo da formação.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.image("imagens/portfolio1.png",
                 caption="Tela inicial do portfólio, com apresentação geral e introdução.",
                 use_container_width=True)

        st.image("imagens/portfolio2.png",
                 caption="Seção dedicada à exibição de projetos desenvolvidos.",
                 use_container_width=True)

    with col2:
        st.image("imagens/portfolio3.png",
                 caption="Área de apresentação pessoal, destacando habilidades e objetivos profissionais.",
                 use_container_width=True)

    st.markdown("---")

    # 🔹 AULAS
    st.subheader("📚 Desenvolvimento em Aula")
    st.write("""
    O projeto também foi acompanhado e desenvolvido durante as aulas,
    com orientação do professor e aplicação prática dos conteúdos estudados.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.image("imagens/aula1.png",
                 caption="Momento de desenvolvimento prático durante as aulas.",
                 use_container_width=True)

        st.image("imagens/aula2.png",
                 caption="Explicação de conceitos importantes aplicados no projeto.",
                 use_container_width=True)

    with col2:
        st.image("imagens/aula3.png",
                 caption="Execução de atividades no ambiente de laboratório.",
                 use_container_width=True)

        st.image("imagens/aula4.png",
                 caption="Evolução do projeto ao longo das etapas de aprendizado.",
                 use_container_width=True)