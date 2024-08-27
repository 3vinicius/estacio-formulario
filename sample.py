#!/usr/bin/env python
# coding: utf-8

# # manipulção de dados
# 
# Apesar do projeto está em jupyter, o projeto está sendo compilado para .py usando o before script `jupyter nbconvert --to script sample.ipynb`

# 

# In[159]:


import pandas as ds

result = ds.read_excel('dados.xlsx')
result.describe()


# In[160]:


colunas = result.columns
result.columns


# ## Funções para a mainupalação da planilha

# In[ ]:


def dadosDaPlanilha():
    listaDeDados = []
    for i,row in result.iterrows():
        values=("Aluno " + str(i), row['Idade'], row['Estado civil'],row['Número de filhos'], row['Sexo'], row['Qual a sua profissão ?'],
                row['Qual refeição você não pode consumir'],row['Entre 0 - 10 qual a classificação da merenda escolar ?'], row['Qual refeição você mais gosta ?\n'], row['Qual refeição você menos gosta ?'])
        listaDeDados.append(values)
    return listaDeDados


# In[164]:


def inserirNaPlanilha(listaDeDados):
    myColunas = ['Sexo', 'Idade', 'Estado civil', 'Número de filhos',
                       'Qual refeição você mais gosta ?\n', 'Qual refeição você menos gosta ?',
                       'Qual refeição você não pode consumir',
                       'Entre 0 - 10 qual a classificação da merenda escolar ?',
                       'Qual a sua profissão ?']
    novaLinha = dict(zip(myColunas, listaDeDados))
    result.loc[len(result)] = novaLinha
    result.to_excel("saidas.xlsx", index=False)
    


# In[165]:


lista = ("Masculino", 18, "Casado",
 5, "cuscuz com leite" ,"Cuscuz com fígado","NENHUMA",5 ,"test")

inserirNaPlanilha(lista)


# In[ ]:





# In[ ]:




