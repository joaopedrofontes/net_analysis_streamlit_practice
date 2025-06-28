import pandas as pd
import networkx as nx
from pyvis.network import Network


def carregar_dados(caminho_csv):
    return pd.read_csv(caminho_csv, sep=";")

def construir_grafo(df):
    G = nx.DiGraph()
    for _, row in df.iterrows():
        origem = row["Descrição Aeroporto Origem"]
        destino = row["Descrição Aeroporto Destino"]
        G.add_edge(origem, destino)
    return G

def gerar_visualizacao_pyvis(G, physics=True):
    net = Network(height='600px', width='100%', directed=True)
    net.from_nx(G)
    if physics:
        net.show_buttons(filter_=['physics'])
    net.save_graph("html/rede_voos.html")

def calcular_metricas(G):
    densidade = nx.density(G)
    assort = nx.degree_assortativity_coefficient(G)
    clustering = nx.average_clustering(G.to_undirected())

    componentes_fortemente_conectados = list(nx.strongly_connected_components(G))
    componentes_fracamente_conectados = list(nx.weakly_connected_components(G))

    return {
        "densidade": densidade,
        "assortatividade": assort,
        "clustering": clustering,
        "componentes_fortes": componentes_fortemente_conectados,
        "componentes_fracos": componentes_fracamente_conectados
    }

def distribuicao_grau(G):
    grau_entrada = dict(G.in_degree())
    grau_saida = dict(G.out_degree())
    return grau_entrada, grau_saida

def centralidades(G):
    return {
        "Eigenvector": nx.eigenvector_centrality(G, max_iter=1000),
        "Degree": nx.degree_centrality(G),
        "Closeness": nx.closeness_centrality(G),
        "Betweenness": nx.betweenness_centrality(G)
    }
