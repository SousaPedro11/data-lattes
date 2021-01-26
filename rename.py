# -*- coding: utf-8 -*-
"""
Script renomeia os curriculos para o nomes
"""

import os
import glob
import xml.etree.ElementTree as ET


cont = 0
curriculos = []
for f in glob.glob('CurriculosXML/*'):    #Lista os arquivos xml da pasta
    curriculos.append(f)
    cont = cont+1 

novos_nomes = []

print('\nCurrículos importados: '+str(cont)) #Imprime os currículos que serão importados
for m in range(0, len(curriculos)):
    tree = ET.parse(curriculos[m])
    root = tree.getroot()
    for t in root.iter('DADOS-GERAIS'):   
        nome_professor = str(t.attrib['NOME-COMPLETO']).upper()
        novos_nomes.append(nome_professor)
        print(curriculos[m],nome_professor)
        os.rename(os.path.join(curriculos[m]), os.path.join("CurriculosXML/"+nome_professor+".xml"))