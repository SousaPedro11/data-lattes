# data-lattes

[comment]: <> (<h4 style="text-align:center">Python and D3.js</h4>)
<p style="text-align:center">
    <img alt="Python" src="https://img.shields.io/badge/python-3.8-green" />
    <img alt="Miniconda" src="https://img.shields.io/badge/miniconda-3-brightgreen" />
    <img alt="D3.js" src="https://img.shields.io/badge/D3.js-v5-orange" />
</p>
Projeto da disciplina de Tópicos em Computação II do curso de Bacharelado em Sistemas de Informação da UFPA.

## Objetivos
* Coletar dados da plataforma Lattes
* Tratar e analisar os dados obtidos
* Mostrar os dados obtidos com gráficos em páginas web utilizando D3.js

## Equipe
* [Francielma Assunção](https://github.com/FrancielmaA)
* José Perdigão
* [Pedro Sousa](https://github.com/SousaPedro11)
* [Rafael Paixão](https://github.com/Rapaix)
* Raphael Campos
* Wellington Santos
* [Yuri Melo](https://github.com/yurimses)

## Tecnologias
* [Python 3](https://www.python.org/)
* [Pip](https://pip.pypa.io/en/stable/) ou [Pipenv](https://github.com/pypa/pipenv)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/),
  [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/),
  [Flask-Bootstrap](https://pythonhosted.org/Flask-Bootstrap/),
  [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* [Pytest](https://docs.pytest.org/en/stable/)
* [gunicorn](https://gunicorn.org/)
* [D3.js](https://d3js.org/)

## Ambiente de desenvolvimento
### Preparação
* Instalar o Python
* Clonar o projeto
    ```shell
    git clone https://github.com/SousaPedro11/data-lattes.git
    ```
* Mude para o diretório raiz do projeto
* Criar um ambiente virtual para isolar a instalação das dependências, utilizando pip ou pipenv
### Usando Pipenv
* Instalar o pipenv utilizando o pip

    No Linux seria: ```sudo pip install pipenv```
* Criar o abiente virtual
  * Verificar e se preciso alterar para 3.8 a versão do Python no arquivo [Pipfile](Pipfile)
  * Criar o ambiente com: ```pipenv --three```
* Instalar dependências
  * Entrar no shell do pipenv: ```pipenv shell```
  * Instalar dependencias com: ```pipenv install```

### Usando pip
* criar o abiente virtual
  ```shell
  python -m venv venv
  ```
* Ativar o ambiente virtual
  * No Linux
    ```shell
    source ./venv/bin/activate
    ```
  * No Windows
    ```
    source .\venv\Scripts\activate
    ```
* instalar dependências
  * instalar dependencias com: ```pip install -r requirements.txt```


## Como executar
* Padrão
```shell
flask run
```
* Gunicorn (standalone server - somente Linux)
```shell
gunicorn --workers=5 --bind=0.0.0.0:5000 --access-logfile - --error-logfile - 'run:app'
```
ou
```shell
gunicorn run:app
```

## Deploy (execução no Heroku)
O deploy é automatizado, atualmente, utilizando a branch flask_develop.

O link da produção: [https://data-lattes.herokuapp.com/](https://data-lattes.herokuapp.com/)
