from tkinter import messagebox
from sample import *

def centralizarGrid(janela):
    for i in range(6):
        janela.grid_columnconfigure(i, weight=1)
    for i in range(10):
        janela.grid_rowconfigure(i, weight=1)

def inserirDados(varNome, varIdade, varEstadoCivil, varNumFilhos, varEmpregado, varRefeicaoNaoConsumir, varClassMerenda,
                 varRefeicaoMaisGosta, varRefeicaoMenosGosta,treeMedidas):
    listData = (varNome.get(),
                varIdade.get(),
                varEstadoCivil.get(),
                varNumFilhos.get(),
                varEstadoCivil.get(),
                varEmpregado.get(),
                varRefeicaoNaoConsumir.get(),
                varClassMerenda.get(),
                varRefeicaoMaisGosta.get(),
                varRefeicaoMenosGosta.get())

    treeMedidas.insert(parent="", index="end",values=(varNome,)+listData)
    inserirNaPlanilha(listData)

def deletarLinha(tree):
    # Obter a linha selecionada
    selected_item = tree.focus()
    if selected_item:
        if messagebox.askyesno("Alerta", "Você realmente deseja excluir essa linha ?"):
            tree.delete(selected_item)
    else:
        messagebox.showinfo("Alerta", "Selecione a linha que deseja excluir")

def ValidacaoDeNumeros(inputIdade):
    user_input = inputIdade.get()
    if user_input.isdigit():
        messagebox.showinfo("Resultado", "A entrada contém apenas números.")
    else:
        messagebox.showwarning("Resultado", "A entrada contém caracteres não numéricos.")

def printCadastro(inputNome, inputIdade):
    print("nome= %s \nIdade= %d"% (inputNome.get(), inputIdade.get()))

def mockInserirDados(treeMedidas):
    for i in range(200):
        treeMedidas.insert('', 'end', values=("Aluno " + str(i), i + 18, "Casado" if i % 2 == 0 else "Solteiro",
                                             i, "Masculino" if i % 2 == 0 else "Feminino", "Sim" if i % 3 == 0 else "Não",
                                             "Cuscuz com fígado", i % 10, "Macarrão com carne", "Sopa"))

def pegarDadosDaPlanilha(treeMedidas):
    listaDeDados = dadosDaPlanilha()
    for row in listaDeDados:
        treeMedidas.insert('', 'end', values=row)
