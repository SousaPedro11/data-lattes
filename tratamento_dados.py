import pandas as pd
import re

# Opcional, utilizado para debug
pd.set_option("display.max_rows", None, "display.max_columns", None)

# Leitura inicial de dados
df_data = pd.read_csv('export_dataframe.csv', low_memory=False)

# Dataframe onde serao usados os dados
a = pd.DataFrame(data=df_data)

a1 = 1999
a2 = 2021
tabelaartsemdoi = []
tabelaartsemdoi2 = []
tabelaartcomdoi = []
tabelaartcomdoi2 = []
tabelaorientacoes = []
tabelaorientacoes2 = []

# Variável s separa os dados da quantidade e de artigos anuais.

a.drop_duplicates(subset=['Titulo'], keep='last', inplace=True)  # Remove artigos com nomes iguais
s = a['Tipo'] + a['Ano']
# Separa somente os artigos do dataframe das colunas Tipo e Ano, coloca em outro dataframe e soma [..]
# [...] quantos resultados obtiveram por ano em um loop, onde é iniciado sempre em 1999 e acaba em 2021.
while a1 < a2 + 1:
    # Primeira condição ser do tipo Artigos Publicados
    df = a[s.str.contains('tipo=ArtigosPublicadosAno={}'.format(a1), case=False)]
    index = df.index
    contagem_tmp = len(index)
    tabelaartsemdoi.append(contagem_tmp)
    tabelaartsemdoi2.append(a1)
    print("Em {} foram publicados: ".format(a1), contagem_tmp, " Artigos")
    a1 += 1

a1 = 1999
list_tmp = list(zip(tabelaartsemdoi2, tabelaartsemdoi))
df2 = pd.DataFrame(list_tmp, columns=['Ano', 'Quantidade'])

# Salva o dataframe contendo Anos e Quantidade para um arquivo que vai ser lido pelo D3.JS

df2.to_csv(r'~/Downloads/data-lattes-master/articles_dataframe.csv', index=False, header=True)

print('#######################################################################################')

# Separa os dados de artigos que possuem DOI.

s = a['Tipo'] + a['Ano'] + a['DOI']
# Separa somente os artigos do dataframe das colunas Tipo e Ano, coloca em outro dataframe e soma [..]
# [...] quantos resultados obtiveram por ano em um loop, onde é iniciado sempre em 1999 e acaba em 2021.
while a1 < a2 + 1:
    # Primeira condição ser do tipo Artigos Publicados e ter um doi que não esteja vazio.
    dftemp = a[s.str.contains('tipo=ArtigosPublicadosAno={}doi=10'.format(a1), case=False)]
    tmpindex = dftemp.index
    contagem_tmp = len(tmpindex)
    tabelaartcomdoi.append(contagem_tmp)
    tabelaartcomdoi2.append(a1)
    print("Em {} foram publicados com DOI: ".format(a1), contagem_tmp, " Artigos")
    a1 += 1

list_tmp = list(zip(tabelaartcomdoi2, tabelaartcomdoi))
df3 = pd.DataFrame(list_tmp, columns=['Ano', 'Quantidade'])

# Salva o dataframe contendo Anos e Quantidade para um arquivo que vai ser lido pelo D3.JS

df3.to_csv(r'~/Downloads/data-lattes-master/articles_doi_dataframe.csv', index=False, header=True)

# Separa os dados de orientacoes completadas.

s = a['Tipo'] + a['Ano']
a1 = 1999
print('#######################################################################################')
while a1 < a2 + 1:
    # Primeira condicao
    dftemp = a[s.str.contains('tipo=TRABALHO_DE_CONCLUSAO_DE_CURSO_GRADUACAOAno={}'.format(a1), case=False)]
    tmpindex = dftemp.index
    # Segunda condicao
    dftemp2 = a[s.str.contains('tipo=ORIENTACAO-DE-OUTRA-NATUREZAAno={}'.format(a1), case=False)]
    tmpindex2 = dftemp2.index
    # Terceira condicao
    dftemp3 = a[s.str.contains('tipo=Dissertação de mestradoAno={}'.format(a1), case=False)]
    tmpindex3 = dftemp3.index
    # Soma o resultado das condicoes
    contagem_tmp = len(tmpindex) + len(tmpindex2) + len(tmpindex3)
    tabelaorientacoes.append(contagem_tmp)
    tabelaorientacoes2.append(a1)
    print("Em {} houveram: ".format(a1), contagem_tmp, " Orientações")
    a1 += 1

list_tmp = list(zip(tabelaorientacoes2, tabelaorientacoes))
df4 = pd.DataFrame(list_tmp, columns=['Ano', 'Quantidade'])
df4.to_csv(r'~/Downloads/data-lattes-master/orientacoes_dataframe.csv', index=False, header=True)

# Inicio da criação do diagrama de VENN (Incompleto)
# ||||||||||||||||||||||||||||||||||||||||
# Separa os dados de artigos por professor.
# s = a['Tipo'] + a['Ano'] + a['Docente']

# a1 = 1999

# print('#######################################################################################')
# while a1 < a2 + 1:
#     # TCC Graduação
#     dftemp = a[s.str.contains('tipo=TRABALHO_DE_CONCLUSAO_DE_CURSO_GRADUACAOAno={}'.format(a1), case=False)]
#     tmpindex = dftemp.index
#     # Segunda
#     dftemp2 = a[s.str.contains('tipo=ORIENTACAO-DE-OUTRA-NATUREZAAno={}'.format(a1), case=False)]
#     tmpindex2 = dftemp2.index
#     # Terceira
#     dftemp3 = a[s.str.contains('tipo=Dissertação de mestradoAno={}'.format(a1), case=False)]
#     tmpindex3 = dftemp3.index
#     # Quarta
#     dftemp4 = a[s.str.contains('tipo=Tese de doutoradoAno={}'.format(a1), case=False)]
#     tmpindex4 = dftemp4.index
#     # Quinta
#     dftemp5 = a[s.str.contains('tipo=Supervisão de pós-doutoradoAno={}'.format(a1), case=False)]
#     tmpindex5 = dftemp5.index

#     contagem_tmp = len(tmpindex) + len(tmpindex2) + len(tmpindex3) + len(tmpindex4) + len(tmpindex5)

#     tabelaorientacoes.append(contagem_tmp)
#     tabelaorientacoes2.append(a1)
#     print("Em {} houveram: ".format(a1), contagem_tmp, " Orientações")
#     a1 += 1

# list_tmp = list(zip(tabelaorientacoes2, tabelaorientacoes))
# df4 = pd.DataFrame(list_tmp, columns=['Ano', 'Quantidade'])
# df4.to_csv(r'~/Downloads/data-lattes-master/orientacoes_dataframe.csv', index=False, header=True)
print('#######################################################################################')
print('Aplicação finalizada, os arquivos .csv já se encontram na página inicial com os seguintes nomes:')
print('orientacoes_dataframe.csv, articles_doi_dataframe.csv e articles_dataframe.csv')
