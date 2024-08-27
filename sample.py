#!/usr/bin/env python
# coding: utf-8

# # manipulção de dados
# 
# Apesar do projeto está em jupyter, o projeto está sendo compilado para .py usando o before script `jupyter nbconvert --to script sample.ipynb`

# 

# In[6]:


import pandas as ds
import matplotlib.pyplot as plt

result = ds.read_excel('dados.xlsx')
result.describe()


# In[ ]:





# In[ ]:


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


# In[ ]:


def inserirNaPlanilha(listaDeDados,result):
    myColunas = ['Sexo', 'Idade', 'Estado civil', 'Número de filhos',
                       'Qual refeição você mais gosta ?\n', 'Qual refeição você menos gosta ?',
                       'Qual refeição você não pode consumir',
                       'Entre 0 - 10 qual a classificação da merenda escolar ?',
                       'Qual a sua profissão ?']
    novaLinha = dict(zip(myColunas, listaDeDados))
    result.loc[len(result)] = novaLinha
    result.to_excel("saidas.xlsx", index=False)


lista = ("Masculino", 18, "Casado",
 5, "cuscuz com leite" ,"Cuscuz com fígado","NENHUMA",5 ,"test")
inserirNaPlanilha(lista,result)




# In[ ]:


result.plot(x='Idade', y='Número de filhos', kind='scatter')
result.plot(x='Idade', y='Qual refeição você mais gosta ?\n', kind='scatter')
result.plot(x='Idade', y='Qual refeição você menos gosta ?', kind='scatter')


# In[ ]:


result.plot.area()
result.plot.area(x='Idade', y='Número de filhos', stacked=False)


# In[ ]:


result.plot.barh()


# In[ ]:


result


# In[ ]:


result.plot.barh(stacked=True)


# In[ ]:


result.apply(ds.value_counts).plot(kind='bar', subplots=True)


# result.apply(ds.value_counts).plot(kind='bar', subplots=True)

# In[5]:


dfCopy = result[['Idade']].copy()
result.plot.kde()


# In[ ]:





# In[ ]:





# In[ ]:


result.plot(title='Dados')


# In[ ]:


dfRelation = result.loc[(result['Estado civil'] == "Solteiro") & (result['Sexo'] == "Mulher" )]
dfRelation.plot(x='Idade', y='Número de filhos', kind='scatter')
dfRelation.plot(x='Idade', y='Qual refeição você mais gosta ?\n', kind='scatter')
dfRelation.plot(x='Idade', y='Qual refeição você menos gosta ?', kind='scatter')


# In[ ]:


dfRelation


# In[ ]:


result.plot(x='Idade', y='Número de filhos', kind='')


# 

# ## Gráfico das preferências dos alunos
#  É possível observar as referencias dos alunos

# In[ ]:


fig, ax = plt.subplots()


result.plot(x='Idade', y='Qual refeição você não pode consumir', kind='scatter', color='red', label='Não pode consumir', ax=ax)
result.plot(x='Idade', y='Qual refeição você mais gosta ?\n', kind='scatter', color='blue', label='Mais gosta', ax=ax)
result.plot(x='Idade', y='Qual refeição você menos gosta ?', kind='scatter', color='green', label='Menos gosta', ax=ax)
plt.title('Distribuição das Preferências de Refeições por Idade')
plt.xlabel('Idade')
plt.ylabel('Refeições')
plt.legend()



# In[ ]:




