import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

df = pd.read_csv('data/dados.csv')
df.columns = df.columns.str.strip()
df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')

min_kvus = 0
max_kvus = 60

num_registros = len(df)
cmap = plt.get_cmap("tab10")
colors = [cmap(i / num_registros) for i in range(num_registros)]

gauge_steps = []
annotations = []

max_legendas_por_linha = 4
linha_atual = 0
espaco_vertical_por_linha = -0.1

for i in range(len(df)):
    kvus = df['Kvus'].iloc[i]
    data = df['Data'].iloc[i].strftime('%d/%m/%Y')

    if i == 0:
        start_val = min_kvus
    else:
        start_val = df['Kvus'].iloc[i-1]
    end_val = kvus

    gauge_steps.append({
        'range': [start_val, end_val],
        'color': f'rgba({colors[i][0]*255}, {colors[i][1]*255}, {colors[i][2]*255}, {colors[i][3]})'
    })

    posicao_horizontal = (i % max_legendas_por_linha) * (1 / max_legendas_por_linha) + (1 / (2 * max_legendas_por_linha))
    if i % max_legendas_por_linha == 0 and i != 0:
        linha_atual += 1

    annotations.append({
        'xref': 'paper',
        'yref': 'paper',
        'x': posicao_horizontal,
        'y': espaco_vertical_por_linha * (linha_atual + 1),
        'text': f"<b>{data}:</b> {kvus} KVus",
        'showarrow': False,
        'font': {'size': 12, 'color': f'rgba({colors[i][0]*255}, {colors[i][1]*255}, {colors[i][2]*255}, {colors[i][3]})'},
        'align': 'center'
    })

kvus_atual = df['Kvus'].iloc[-1]

altura_extra_legendas = max(1, (linha_atual + 1)) * 50

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=kvus_atual,
    title={'text': "Quantidade de KVus"},
    gauge={
        'axis': {'range': [min_kvus, max_kvus]},
        'bar': {'color': "darkblue"},
        'steps': gauge_steps
    }
))

for annotation in annotations:
    fig.add_annotation(annotation)

fig.update_layout(
    autosize=True,
    margin=dict(t=50, b=100 + altura_extra_legendas, l=50, r=50),
    height=500 + altura_extra_legendas,
    annotations=annotations
)

fig.show()
