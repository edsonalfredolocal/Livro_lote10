#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 13:33:03 2026

@author: edsonalfredo
"""

#%% 1 - Importar bibliotecas
import streamlit as st
from PIL import Image
import pandas as pd
from datetime import datetime
import os
from io import BytesIO


#%% 2 - Configuração da página
st.set_page_config(
    page_title="Livro do Lote 10",
    page_icon="🏢",
    layout="centered"
)


#%% 3 - Código de acesso do administrador
CODIGO_ADMIN = "L10_2026_Admin_Oficial"


#%% 4 - Nome do ficheiro Excel
FICHEIRO_EXCEL = "respostas_lote10.xlsx"


#%% 5 - Carregar imagens
imagem1 = Image.open("IMG_2537.jpeg")
imagem2 = Image.open("IMG_2538.jpeg")


#%% 6 - Estilo visual da aplicação
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f4f7f1;
    }

    h1, h2, h3 {
        color: #1f4d2e;
    }

    .stButton>button {
        background-color: #2e7d32;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
    }

    .stButton>button:hover {
        background-color: #1b5e20;
        color: white;
    }

    section[data-testid="stSidebar"] {
        background-color: #dfe8d8;
    }
    </style>
    """,
    unsafe_allow_html=True
)


#%% 7 - Função para guardar resposta no Excel
def guardar_resposta(dados):

    nova_linha = pd.DataFrame([dados])

    if os.path.exists(FICHEIRO_EXCEL):

        dados_antigos = pd.read_excel(FICHEIRO_EXCEL)

        dados_atualizados = pd.concat(
            [dados_antigos, nova_linha],
            ignore_index=True
        )

    else:

        dados_atualizados = nova_linha

    dados_atualizados.to_excel(
        FICHEIRO_EXCEL,
        index=False
    )


#%% 8 - Função para carregar respostas
def carregar_respostas():

    if os.path.exists(FICHEIRO_EXCEL):

        return pd.read_excel(FICHEIRO_EXCEL)

    else:

        return pd.DataFrame()


#%% 9 - Menu lateral
st.sidebar.title("🏢 LIVRO DO LOTE 10")

pagina = st.sidebar.radio(
    "Escolha a área:",
    [
        "Formulário Público",
        "Área Administrativa"
    ]
)


#%% 10 - Página pública
if pagina == "Formulário Público":

    st.title("🏢 LIVRO DO LOTE 10")

    st.subheader(
        "Sistema de recolha de histórias e memórias"
    )

    st.write("""
    Este espaço foi criado para recolher memórias,
    histórias, acontecimentos e experiências
    dos moradores e ex-moradores do Lote 10.
    """)

    st.divider()

    st.header("📋 Pré-Inquérito")

    nome = st.text_input("Nome")

    apelido = st.text_input(
        "Apelido pelo qual era conhecido"
    )

    tipo_pessoa = st.selectbox(
        "Qual a sua ligação ao Lote 10?",
        [
            "Morador",
            "Ex-morador",
            "Familiar",
            "Amigo",
            "Outro"
        ]
    )

    periodo = st.text_input(
        "Em que período frequentou ou viveu no prédio?"
    )

    memoria = st.text_area(
        "Qual a memória mais marcante que tem do Lote 10?"
    )

    pessoas = st.text_area(
        "Que pessoas marcaram a história do prédio?"
    )

    pais_maes = st.text_area(
        "Que pais, mães ou encarregados marcaram "
        "a sua infância e juventude no Lote 10?"
    )

    jogos = st.text_area(
        "Que jogos, brincadeiras ou momentos "
        "comunitários marcaram o prédio?"
    )

    espaco_livre = st.text_area(
        "Espaço livre para outras histórias "
        "e lembranças."
    )

    autorizacao = st.checkbox(
        "Autorizo o uso destas informações "
        "no Livro do Lote 10"
    )

    if st.button("Enviar Resposta"):

        if nome == "":

            st.error("Por favor, preencha o nome.")

        elif autorizacao == False:

            st.warning(
                "É necessário autorizar "
                "o uso das informações."
            )

        else:

            dados = {
                "Data_Hora": datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                "Nome": nome,
                "Apelido": apelido,
                "Ligacao_Lote10": tipo_pessoa,
                "Periodo": periodo,
                "Memoria_Marcante": memoria,
                "Pessoas_Marcantes": pessoas,
                "Pais_Maes_Marcantes": pais_maes,
                "Jogos_Momentos": jogos,
                "Espaco_Livre": espaco_livre,
                "Autorizacao": "Sim"
            }

            guardar_resposta(dados)

            st.success(
                "Resposta enviada e guardada com sucesso!"
            )

            st.divider()

            st.header("📄 Resumo da Resposta")

            st.write(f"**Nome:** {nome}")
            st.write(f"**Apelido:** {apelido}")
            st.write(f"**Ligação ao prédio:** {tipo_pessoa}")
            st.write(f"**Período:** {periodo}")

            st.write("### Memória Marcante")
            st.write(memoria)

            st.write("### Pessoas Marcantes")
            st.write(pessoas)

            st.write("### Pais e Mães que Marcaram")
            st.write(pais_maes)

            st.write("### Jogos e Momentos Comunitários")
            st.write(jogos)

            st.write("### Espaço Livre")
            st.write(espaco_livre)


#%% 11 - Área administrativa
elif pagina == "Área Administrativa":

    st.title("🔐 Área Administrativa")

    codigo_digitado = st.text_input(
        "Digite o código de acesso:",
        type="password"
    )

    if codigo_digitado == "":

        st.info(
            "Digite o código para aceder "
            "à administração."
        )

    elif codigo_digitado != CODIGO_ADMIN:

        st.error("Código incorreto.")

    else:

        st.success("Acesso autorizado.")

        respostas = carregar_respostas()

        st.divider()

        st.header("📊 Painel de Controlo")

        total_respostas = len(respostas)

        st.metric(
            "Total de respostas",
            total_respostas
        )

        st.metric(
            "Respostas validadas",
            0
        )

        st.metric(
            "Respostas por validar",
            total_respostas
        )

        st.divider()

        st.header("📋 Respostas Recebidas")

        if respostas.empty:

            st.warning(
                "Ainda não existem respostas guardadas."
            )

        else:

            st.dataframe(
                respostas,
                use_container_width=True
            )

            output = BytesIO()

            with pd.ExcelWriter(
                output,
                engine="openpyxl"
            ) as writer:

                respostas.to_excel(
                    writer,
                    index=False,
                    sheet_name="Respostas"
                )

            st.download_button(
                label="📥 Baixar respostas em Excel",
                data=output.getvalue(),
                file_name="respostas_lote10.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        st.divider()

        st.header("🗂️ Gestão do Projecto")

        st.write("""
        Nesta área administrativa poderás:

        - visualizar respostas recebidas
        - baixar Excel
        - controlar número de respostas
        - organizar histórias
        - preparar conteúdos para o livro
        """)


#%% 12 - Galeria inferior
st.divider()

st.header("📸 Memórias do Lote 10")

col1, col2 = st.columns(2)

with col1:

    st.image(
        imagem1,
        use_container_width=True
    )

with col2:

    st.image(
        imagem2,
        use_container_width=True
    )