# criar menu
import readline
import subprocess
import createDataFrame
import tratamento_dados
import webbrowser
readline.parse_and_bind("tab: complete")

print("Welcome to the LattesPlan Script Menu")
print("")
path = input("insira o endereço de diretorio: ")

createDataFrame.Main(path)
print("Criação do dataframe finalizada")
tratamento_dados.Main()
print("Tratamento de dados finalizado")
print("Abrindo visualização...")
webbrowser.open("https://data-lattes.herokuapp.com/home/", new=1)
