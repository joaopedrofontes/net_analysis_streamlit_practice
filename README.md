# Rede de Voos no Brasil – Dezembro de 2024

Este projeto utiliza **Streamlit**, **NetworkX** e **Pyvis** para construir e visualizar a rede de voos comerciais no Brasil, com base nos dados abertos da ANAC. Cada aeroporto é representado como um nó, e cada voo como uma aresta dirigida na rede.

## Dados utilizados

Os dados utilizados são públicos e estão disponíveis no site da ANAC:

[https://siros.anac.gov.br/siros/registros/diversos/vra/2024/VRA_2024_12.csv](https://siros.anac.gov.br/siros/registros/diversos/vra/2024/VRA_2024_12.csv)

## Como executar o projeto

1. Clone este repositório:
```bash
git clone https://github.com/joaopedrofontes/net_analysis_streamlit_practice.git
cd net_analysis_streamlit_practice
```

2. Crie um ambiente virtual e ative:
```bash
python -m venv .venv
source .venv/bin/activate       # Linux/macOS
.venv\Scripts\activate          # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Rode a aplicação:
```bash
streamlit run app.py
```
