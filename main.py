import tkinter as tk
from tkinter import ttk

from funções import *
from sample import *

# CONFIGURAÇÕES DA JANELA
janela = tk.Tk()
janela.title("Formulario de cadastro socioeconome")

centralizarGrid(janela)

# Input labels e campos
## Nome
varNome = tk.StringVar()
tk.Label(janela, text="Nome").grid(row=0, column=0, sticky="e")
inputNome = tk.Entry(janela, width=30, textvariable=varNome)
inputNome.grid(row=0, column=1, padx=10, pady=5)

## Idade
varIdade = tk.StringVar()
tk.Label(janela, text="Idade").grid(row=0, column=2, padx=10, pady=5, sticky="e")
inputIdade = tk.Entry(janela, textvariable=varIdade, width=30)
inputIdade.grid(row=0, column=3, padx=10, pady=5)

## Estado Civil
tk.Label(janela, text="Estado Civil").grid(row=1, column=0, padx=10, pady=5, sticky="e")
varEstadoCivil = tk.StringVar()
estadoCivil = ttk.Combobox(janela, width=27, textvariable=varEstadoCivil)
estadoCivil['values'] = ('Casado (a)', 'Solteiro (a)')
estadoCivil.grid(column=1, row=1, padx=10, pady=5)
estadoCivil.current()

## Número de Filhos
varNumFilhos = tk.StringVar()
tk.Label(janela, text="Número de Filhos").grid(row=1, column=2, padx=10, pady=5, sticky="e")
inputNumFilhos = tk.Entry(janela, textvariable=varNumFilhos, width=30)
inputNumFilhos.grid(row=1, column=3, padx=10, pady=5)

## Sexo
tk.Label(janela, text="Sexo").grid(row=2, column=0, padx=10, pady=5, sticky="e")
varSexo = tk.StringVar()
inputSexo = ttk.Combobox(janela, width=27, textvariable=varSexo)
inputSexo['values'] = ('Masculino', 'Feminino')
inputSexo.grid(column=1, row=2, padx=10, pady=5)
inputSexo.current()

## Você está empregado?
tk.Label(janela, text="Você está empregado").grid(row=2, column=2, padx=10, pady=5, sticky="e")
varEmpregado = tk.StringVar()
inputEmpregado = ttk.Combobox(janela, width=27, textvariable=varEmpregado)
inputEmpregado['values'] = ('Sim', 'Não')
inputEmpregado.grid(column=3, row=2, padx=10, pady=5)
inputEmpregado.current()

## Qual refeição você não pode consumir
tk.Label(janela, text="Qual refeição você não pode consumir").grid(row=3, column=0, padx=10, pady=5, sticky="e")
varRefeicaoNaoConsumir = tk.StringVar()
inputRefeicaoNaoConsumir = ttk.Combobox(janela, width=27, textvariable=varRefeicaoNaoConsumir)
inputRefeicaoNaoConsumir['values'] = (
    'Cuscuz com carne moída', 'Cuscuz com fígado', 'Cuscuz com leite', 'Manguzá',
    'Macarrão com carne moída', 'Sopa', 'Arroz com Strogonoff', 'Arroz com carne moída', 'NENHUMA'
)
inputRefeicaoNaoConsumir.grid(column=1, row=3, padx=10, pady=5)
inputRefeicaoNaoConsumir.current()

## Classificação da merenda
tk.Label(janela, text="Classificação da merenda").grid(row=3, column=2, padx=10, pady=5, sticky="e")
varClassMerenda = tk.StringVar()
inputClassMerenda = ttk.Combobox(janela, width=27, textvariable=varClassMerenda)
inputClassMerenda['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
inputClassMerenda.grid(column=3, row=3, padx=10, pady=5)
inputClassMerenda.current()

## Qual refeição você mais gosta
tk.Label(janela, text="Qual refeição você mais gosta").grid(row=4, column=0, padx=10, pady=5, sticky="e")
varRefeicaoMaisGosta = tk.StringVar()
inputRefeicaoMaisGosta = ttk.Combobox(janela, width=27, textvariable=varRefeicaoMaisGosta)
inputRefeicaoMaisGosta['values'] = (
    'Cuscuz com carne moída', 'Cuscuz com fígado', 'Cuscuz com leite', 'Manguzá',
    'Macarrão com carne', 'Arroz com Strogonoff', 'Arroz com carne moída', 'NENHUMA', 'Sopa'
)
inputRefeicaoMaisGosta.grid(column=1, row=4, padx=10, pady=5)
inputRefeicaoMaisGosta.current()

## Qual refeição você menos gosta
tk.Label(janela, text="Qual refeição você menos gosta").grid(row=4, column=2, padx=10, pady=5, sticky="e")
varRefeicaoMenosGosta = tk.StringVar()
inputRefeicaoMenosGosta = ttk.Combobox(janela, width=27, textvariable=varRefeicaoMenosGosta)
inputRefeicaoMenosGosta['values'] = (
    'Cuscuz com carne moída', 'Cuscuz com fígado', 'Cuscuz com leite', 'Manguzá',
    'Macarrão com carne moída', 'Sopa', 'Arroz com Strogonoff', 'Arroz com carne moída', 'NENHUMA'
)
inputRefeicaoMenosGosta.grid(column=3, row=4, padx=10, pady=5)
inputRefeicaoMenosGosta.current()





## Output DeDados
# Frame para o Treeview
frameTreeview = tk.Frame(janela)
frameTreeview.grid(row=5, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

# Dados das colunas para o Treeview
dadosColunas = ("nome", "idade", "estadoCivil", "numeroFilhos", "sexo", "empregado",
                 "naoConsome", "class", "maisGosta", "menGosta")

# Criação do Treeview
treeMedidas = ttk.Treeview(frameTreeview, columns=dadosColunas, show='headings', selectmode='browse')

# Configuração das barras de rolagem
verScrlbar = ttk.Scrollbar(frameTreeview, orient="vertical", command=treeMedidas.yview)
verScrlbar.pack(side='right', fill='y')
horScrlbar = ttk.Scrollbar(frameTreeview, orient="horizontal", command=treeMedidas.xview)
horScrlbar.pack(side='bottom', fill='x')

# Configuração do Treeview para usar as barras de rolagem
treeMedidas.configure(yscrollcommand=verScrlbar.set, xscrollcommand=horScrlbar.set)

# Configuração dos headings (cabeçalhos)
treeMedidas.heading("nome", text="Nome")
treeMedidas.heading("idade", text="Idade")
treeMedidas.heading("estadoCivil", text="Estado Civil")
treeMedidas.heading("numeroFilhos", text="Números de Filhos")
treeMedidas.heading("sexo", text="Sexo")
treeMedidas.heading("empregado", text="Você está empregado")
treeMedidas.heading("naoConsome", text="Qual refeição você não pode consumir")
treeMedidas.heading("class", text="Classificação da merenda")
treeMedidas.heading("maisGosta", text="Qual refeição você mais gosta?")
treeMedidas.heading("menGosta", text="Qual refeição você menos gosta?")

# Configuração das colunas
treeMedidas.column("nome", minwidth=0, width=100)
treeMedidas.column("idade", minwidth=0, width=40)
treeMedidas.column("estadoCivil", minwidth=0, width=100)
treeMedidas.column("numeroFilhos", minwidth=0, width=110)
treeMedidas.column("sexo", minwidth=0, width=70)
treeMedidas.column("empregado", minwidth=0, width=120)
treeMedidas.column("naoConsome", minwidth=0, width=180)
treeMedidas.column("class", minwidth=0, width=150)
treeMedidas.column("maisGosta", minwidth=0, width=180)
treeMedidas.column("menGosta", minwidth=0, width=200)

# Empacotamento do Treeview
treeMedidas.pack(padx=10, pady=10, fill='both', expand=True)




## Frame para os botões
frameBotoes = tk.Frame(janela)
frameBotoes.grid(row=10, column=0, columnspan=5, pady=20, sticky="ew")



# Botões
tk.Button(frameBotoes, text='Sair', command=janela.quit).pack(side='left',padx=5)
(tk.Button(frameBotoes, text='Inserir Dados', command=lambda:inserirDados(varNome, varIdade, varEstadoCivil, varNumFilhos,
                                                                 varEmpregado, varRefeicaoNaoConsumir, varClassMerenda,
                                                                 varRefeicaoMaisGosta,
                                                                 varRefeicaoMenosGosta,treeMedidas))
 .pack(side='left',padx=5))

(tk.Button(frameBotoes, text='Excluir Linha', command=lambda:deletarLinha(treeMedidas))
 .pack(side='left',padx=5))


#MockDeDados
#mockInserirDados(treeMedidas)

##Dados
pegarDadosDaPlanilha(treeMedidas)


janela.mainloop()
