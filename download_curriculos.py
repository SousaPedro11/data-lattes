# -*- coding: utf-8 -*-
"""
O script faz o download dos curricuos dos professores

total de professores: 31
"""
import webbrowser

link_xml = 'http://buscatextual.cnpq.br/buscatextual/download.do?metodo=apresentar&idcnpq='
link_lattes = 'http://lattes.cnpq.br/'

# lista de professores listados no site da FACOMP UFPA Belém:
    
identificadores = [
    '2949449810540513', #André Figueira Riker  
    '5376253015721742', #Antonio Jorge Gomes Abelém  
    '7709951222407913', #Benedito de Jesus Pinheiro Ferreira
    '3032638002357978', #Bianchi Serique Meiguins
    '1614538302774823', #Carla Alessandra Lima Reis
    '2948406243474342', #Carlos Gustavo Resque dos Santos
    '9626971450974065', #Cassia Maria Carneiro Kahwage
    '4742268936279649', #Claudomiro De Souza De Sales Junior
    '6490014244112888', #Cleidson Ronald Botelho De Souza
    '8273198217435163', #Denis Lima do Rosário
    '4423219093583221', #Dionne Cavalcante Monteiro
    '1497269209026542', #Eloi Luiz Favero
    '7676631005873564', #Fabiola Pantoja Oliveira Araújo
    '5883877669437870', #Filipe de Oliveira Saraiva	
    '1631238943341152', #Gustavo Henrique Lima Pinto
    '1468872219964148', #Helder May Nunes da Silva Oliveira
    '5219735119295290', #Jefferson Magalhães De Morais
    '8158963767870649', #Josivaldo de Souza Araújo
    '0970111009687779', #Lídio Mauro Lima de Campos
    '2130563131041136', #Marcelle Pereira Mota
    '6655468164115415', #Marianne Kogut Eliasquevici	
    '9756167788721062', #Nelson Cruz Sampaio Neto
    '3286528998900137', #Raimundo Viégas Junior
    '1572121571522063', #Regiane Silva Kawasaki Frances
    '9157422386900321', #Reginaldo Cordeiro dos Santos Filho
    '7469949213441010', #Renato Hidaka Torres
    '6894507054383644', #Roberto Samarone Dos Santos Araujo
    '9839778710074372', #Rodrigo Quites Reis
    '2080791630485427', #Sandro Ronaldo Bezerra Oliveira
    '2484200467965399', #Vinicius Augusto Carvalho de Abreu
    '8798424081680540', #Victor Hugo Santiago Costa Pinto
]

decisao = input('''PARA ABRIR OS CURRÍCULOS LATTES, DIGITE 1. 
PARA ABRIR OS ARQUIVOS XMLs, DIGITE 2.
''')

cont = 0

if decisao == 1:
    for item in identificadores:
        cont = cont + 1
        webbrowser.open_new(link_lattes+item)
else:
    for item in identificadores:
        cont = cont + 1
        webbrowser.open_new(link_xml+item)
    
print('Total de páginas abertas: '+str(cont))
