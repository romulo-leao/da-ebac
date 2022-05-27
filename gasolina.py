# código de geração do gráfico 

import pandas as pd
import seaborn as sns

data = pd.read_csv("gasolina.csv")

line_plot = sns.lineplot(data=data, x="dia", y="venda")

fig = line_plot.get_figure()
fig.savefig("gasolina.png")