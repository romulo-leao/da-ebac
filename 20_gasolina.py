with sns.axes_style('whitegrid'):

  line_plot = sns.lineplot(data=data, x="dia", y="venda", palette="pastel")
  line_plot.set(title='Venda de Gasolina por Dia em SP', xlabel='Dia', ylabel='Qtd Vendida')

fig = line_plot.get_figure()
fig.savefig("gasolina.png")
