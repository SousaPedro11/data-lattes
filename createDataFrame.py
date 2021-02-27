# -*- coding: utf-8 -*-
"""
    Autores: Francielma Assunção e Yuri Melo
"""

import xml.etree.ElementTree as ET
import pandas as pd
import os

path = '.\CurriculosXML'
lista_dados = []
cols = ['Tipo','Titulo','DOI', 'Ano', 'Docente']

for filename in os.listdir(path):
    if filename.endswith('.xml'):
        fullname = os.path.join(path, filename)
        tree = ET.parse(fullname)
        root = tree.getroot()
        #cols = ['Tipo','Titulo','DOI', 'Ano', 'Docente']

        lista_trab = [] #lista dos trabalhos em eventos
        lista_art = [] #lista dos artigos publicados
        lista_cap =[] #lista dos capitulos publicados
        lista_oout = [] #lista das outras orientações concluídas
        lista_om = [] #lista das orientações de mestrado concluídas
        lista_odr = [] #lista das orientações de doutorado concluídas
        lista_opdr = [] #lista das orientações de pós-doutorado concluídas
        lista_appt = [] #lista das apresentações trabalhos
        lista_sof = [] #lista dos registros de software 
        
        _tipo = ''
        _titulo = ''
        _doi = ''
        _ano = ''
        trabEventos = 'TrabalhoEventos'
        artPub = 'ArtigosPublicados'
        capPub = 'CapitulosPublicados'
        software = 'Software'
        docente = ''

        ##Cria um lista dos trabalhos em eventos com seus respectivos DOIs
        for i in root.iter('DADOS-BASICOS-DO-TRABALHO'):
            trabEventos = trabEventos
            _titulo = i.attrib['TITULO-DO-TRABALHO']
            _doi = i.attrib['DOI'] 
            _ano = i.attrib['ANO-DO-TRABALHO'] 
            lista_trab.append(['tipo='+ trabEventos,'titulo='+ _titulo,'doi='+ _doi, 'ano='+ _ano, 'docente='+ filename])

        ##Cria um lista dos artigos publicados com seus respectivos DOIs
        for i in root.iter('DADOS-BASICOS-DO-ARTIGO'):
            artPub = artPub
            _titulo = i.attrib['TITULO-DO-ARTIGO']
            _doi = i.attrib['DOI'] 
            _ano = i.attrib['ANO-DO-ARTIGO'] 
            lista_art.append(['tipo='+ artPub,'titulo='+ _titulo,'doi='+ _doi, 'ano='+ _ano,'docente='+ filename])
        
        lista_trab += lista_art

        ##Cria um lista dos capitulos publicados com seus respectivos DOIs
        for i in root.iter('DADOS-BASICOS-DO-CAPITULO'):
            capPub = capPub
            _titulo = i.attrib['TITULO-DO-CAPITULO-DO-LIVRO']
            _doi = i.attrib['DOI'] 
            _ano = i.attrib['ANO'] 
            lista_cap.append(['tipo='+ capPub,'titulo='+ _titulo,'doi='+ _doi, 'ano='+ _ano,'docente='+ filename])

        lista_trab += lista_cap

        ##Cria um lista das outras orientações concluídas com seus respectivos DOIs
        for i in root.iter('DADOS-BASICOS-DE-OUTRAS-ORIENTACOES-CONCLUIDAS'):
            _tipo = i.attrib['NATUREZA']
            _titulo = i.attrib['TITULO']
            _doi = i.attrib['DOI'] 
            _ano = i.attrib['ANO'] 
            lista_oout.append(['tipo='+ _tipo, 'titulo='+ _titulo,'doi='+ _doi, 'ano='+ _ano,'docente='+ filename])
        
        lista_trab += lista_oout
        
        ##Cria um lista das orientações de mestrado concluídas com seus respectivos DOIs
        for i in root.iter('DADOS-BASICOS-DE-ORIENTACOES-CONCLUIDAS-PARA-MESTRADO'):
            #print(i.attrib)
            _tipo = i.attrib['NATUREZA']
            _titulo = i.attrib['TITULO']
            _doi = i.attrib['DOI'] 
            _ano = i.attrib['ANO'] 
            lista_om.append(['tipo='+ _tipo, 'titulo='+ _titulo,'doi='+ _doi, 'ano='+ _ano,'docente='+ filename])

        lista_trab += lista_om
        
        ##Cria um lista das orientações de doutorado concluídas com seus respectivos DOIs
        for i in root.iter('DADOS-BASICOS-DE-ORIENTACOES-CONCLUIDAS-PARA-DOUTORADO'):
            _tipo = i.attrib['NATUREZA']
            _titulo = i.attrib['TITULO']
            _doi = i.attrib['DOI'] 
            _ano = i.attrib['ANO'] 
            lista_odr.append(['tipo='+ _tipo, 'titulo='+ _titulo,'doi='+ _doi, 'ano='+ _ano,'docente='+ filename])
        
        lista_trab += lista_odr

        ##Cria um lista das orientações de pós-doutorado concluídas com seus respectivos DOIs
        for i in root.iter('DADOS-BASICOS-DE-ORIENTACOES-CONCLUIDAS-PARA-POS-DOUTORADO'):
            _tipo = i.attrib['NATUREZA']
            _titulo = i.attrib['TITULO']
            _doi = i.attrib['DOI'] 
            _ano = i.attrib['ANO'] 
            lista_opdr.append(['tipo='+ _tipo, 'titulo='+ _titulo,'doi='+ _doi, 'ano='+ _ano,'docente='+ filename])

        lista_trab += lista_opdr

        ##Cria um lista das apresentações trabalhos com seus respectivos DOIs
        for i in root.iter('DADOS-BASICOS-DA-APRESENTACAO-DE-TRABALHO'):
            _tipo = i.attrib['NATUREZA']
            _titulo = i.attrib['TITULO']
            _doi = i.attrib['DOI'] 
            _ano = i.attrib['ANO'] 
            lista_appt.append(['tipo='+ _tipo, 'titulo='+ _titulo,'doi='+ _doi, 'ano='+ _ano,'docente='+ filename])

        lista_trab += lista_appt

        ##Cria um lista dos registros de software com seus respectivos DOIs
        for i in root.iter('DADOS-BASICOS-DO-SOFTWARE'):
            software = software
            _titulo = i.attrib['TITULO-DO-SOFTWARE']
            _doi = i.attrib['DOI'] 
            _ano = i.attrib['ANO'] 
            lista_sof.append(['tipo='+ software, 'titulo='+ _titulo,'doi='+ _doi, 'ano='+ _ano,'docente='+ filename])
        
        lista_trab += lista_sof
        lista_dados += lista_trab

#cria o dataframe       
df = pd.DataFrame(lista_dados,columns=cols)
#gera o arquivo CSV do dataframe no destino desejado
df.to_csv(r'C:\Users\assun\Documents\data-lattes\data-lattes\export_dataframe.csv',index= False, header = True)
 


  
            