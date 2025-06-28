import os
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit.components.v1 as components
from rede_voos import *

st.set_page_config(layout="wide")
st.title("Rede de Voos no Brasil em dezembro de 2024")

st.sidebar.header("Opções")
physics = st.sidebar.checkbox("Habilitar interações físicas (Pyvis)", value=True)
top_k = st.sidebar.slider("Top-K nós por centralidade", 5, 30, 10)


CSV_PATH = "VRA_2024_12.csv"

if not os.path.exists(CSV_PATH):
    st.error(f"O arquivo '{CSV_PATH}' não foi encontrado.")
else:
    df = carregar_dados(CSV_PATH)
    G = construir_grafo(df)
    gerar_visualizacao_pyvis(G, physics=physics)

    st.subheader("Visualização Interativa da Rede de Voos")
    HtmlFile = open("html/rede_voos.html", 'r', encoding='utf-8')
    components.html(HtmlFile.read(), height=700)

    st.subheader("Métricas Estruturais da Rede")
    metricas = calcular_metricas(G)
    st.markdown(f"- **Densidade**: {metricas['densidade']:.4f}")
    st.markdown(f"- **Assortatividade**: {metricas['assortatividade']:.4f}")
    st.markdown(f"- **Coeficiente de Clustering Global**: {metricas['clustering']:.4f}")
    st.markdown(f"- **Componentes Fortemente Conectados**: {len(metricas['componentes_fortes'])}")
    st.markdown(f"- **Componentes Fracamente Conectados**: {len(metricas['componentes_fracos'])}")

    st.subheader("Distribuição de Grau (Entrada e Saída)")
    grau_entrada, grau_saida = distribuicao_grau(G)

    fig, axs = plt.subplots(1, 2, figsize=(14, 5))
    sns.histplot(list(grau_entrada.values()), kde=False, ax=axs[0])
    axs[0].set_title("In-degree")
    sns.histplot(list(grau_saida.values()), kde=False, ax=axs[1])
    axs[1].set_title("Out-degree")
    st.pyplot(fig)

    st.subheader("Centralidades dos Nós")
    central = centralidades(G)
    for tipo, valores in central.items():
        st.markdown(f"### {tipo} Centrality")
        top_nos = sorted(valores.items(), key=lambda x: x[1], reverse=True)[:top_k]
        st.table(pd.DataFrame(top_nos, columns=["Aeroporto", "Centralidade"]))
