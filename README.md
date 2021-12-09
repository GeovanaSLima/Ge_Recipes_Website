<h1 align="center">Alura Receita Website</h1>

<!-- <p align="center"><img src="https://img.shields.io/static/v1?label=&message=Live Demo&color=FC5C65&style=for-the-badge&logo=heroku" style="align-items:center"/></p> -->

<p align="center"><img src="https://github.com/GeovanaSLima/Ge_Recipes_Website/blob/main/django-gereceitas.gif"  alt="Expanding Cards"/></p>


</br>

Projeto de desenvolvimento Back-end utilizando o framework Django. A ideia do site foi proposta na Formação Django da Plataforma Alura, onde criamos um site completo de receitas. Dentro do projeto, trabalhamos com a construção de banco de dados, integração das páginas HTML com o Back-end, utilização de ferramentas de Formulários do Django, e muito mais.

</br>

# 🏁 Tabela de Conteúdo

- [🏁 Tabela de Conteúdo](#-tabela-de-conteúdo)
- [💻 Como Usar](#-como-usar)
  - [⚠️ Pré-requisitos](#️-pré-requisitos)
  - [🔨 Instalação e Configuração do Virtualenv](#-instalação-e-configuração-do-virtualenv)
  - [📄 Alteração de arquivos](#-alteração-de-arquivos)
  - [🚩 Rodando o Projeto](#-rodando-o-projeto)
  - [📝 Estrutura do Projeto](#-estrutura-do-projeto)
- [🚀 Features](#-features)
- [🏭 Banco de Dados](#-banco-de-dados)
- [🛠 Tecnologias](#-tecnologias)
- [✒️ Autora](#️-autora)


</br>

# 💻 Como Usar

## ⚠️ Pré-requisitos
Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:

* [Git](https://git-scm.com)
* [Python](https://www.python.org/)

Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/), ou o editor da sua preferência.

## 🔨 Instalação e Configuração do Virtualenv
</br>

```bash
# Clone este repositório
$ git clone https://github.com/GeovanaSLima/Front-End-Challenge.git
```


```python
## No terminal, Acesse a pasta do Projeto
$ cd C:/PastaProjeto

## Criando Ambiente Virtual
$ python -m venv ./venv       

## Ativando virtual env
$ ./venv/Scripts/activate    

## Instalar Django
$ pip install django          
```

## 📄 Alteração de arquivos 
</br> 

No arquivo ```settings.py```:
```python
## Importar bibliotecas
import os
```

```python
## Definir o local da pasta TEMPLATES
'DIRS': [os.path.join(BASE_DIR, 'templates')],
```

```python
## Alterar o Idioma e Fuso Horário
LANGUAGE_CODE = 'pt_br'
TIME_ZONE = 'America/Sao_Paulo'
```
* Criar a pasta ```templates```
* Na pasta ```./venv/Scripts``` criar o arquivo ```manage.bat```:

    ```
    @python "%VIRTUAL_ENV%\..\manage.py" % *
    ```
    _Torna possível a utilização do arquivo ```manage.py``` em qualquer local sem a necessidade de referenciar o caminho inteiro_

## 🚩 Rodando o Projeto
```python
## No terminal
$ python manage.py runserver 
```

Você deve ver a seguinte imagem depois de rodar o código:

<img src="https://raw.githubusercontent.com/GeovanaSLima/Ge_Alura_Receitas/main/runserver.PNG">


</br>

Clicando no link fornecido, você já consegue acessar o site em desenvolvimento e alterar como desejar.

</br>

## 📝 Estrutura do Projeto
   - aplicacao
      - alurareceita
        - static
      - apps
        - receitas
        - usuarios
      - media
      - templates
        - partials
        - receitas
        - usuarios
      - venv

</br>

# 🚀 Features

- [X] Cadastro de Usuários
- [X] Login de Usuários
- [X] Cadastro de Receitas
- [X] Editar Receitas
- [X] Deletar Receitas
- [X] Dashboard Específico de Usuário
- [X] Busca de Receitas
- [X] Página Admin
  
</br>

# 🏭 Banco de Dados


Foi criado um banco de dados utilizando o PostgreSQL para armazenar as informações de usuários e as receitas. Assim, foi possível criar o dashboard com as receitas do usuário.

</br>


# 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

</br>

<p align="center">
<a href="https://www.djangoproject.com/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-original.svg" alt="django" width="50" height="50"/> </a><a href="https://www.w3.org/html/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="50" height="50"/> </a><a href="https://www.w3schools.com/css/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="50" height="50"/> </a><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="50" height="50"/> </a><a href="https://www.postgresql.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="50" height="50"/> </a> <a href="https://heroku.com" target="_blank"> <img src="https://www.vectorlogo.zone/logos/heroku/heroku-icon.svg" alt="heroku" width="50" height="50"/> </a>

</p>

</br>

# ✒️ Autora

<a href="https://learningdata.dev/sobre">
 <img style="border-radius:50%" src="https://media-exp1.licdn.com/dms/image/C4D03AQEeTSxE08-_QQ/profile-displayphoto-shrink_800_800/0/1628591938780?e=1642636800&v=beta&t=go-NA-niXJWY74fvMdvf9pRq0yKL5rT7WcnreLd9VDE" width="100px;" alt="Geovana Sousa"/>
 <br />
 <sub style="font-size:15px"><b>Geovana Sousa 🚀</b></sub></a>


_A passionate Data Scientist and Developer ❤️_

Entre em contato! 👋🏽

[![LearningData Badge](https://img.shields.io/badge/-LearningData-%23FC5C65?style=&logo=ghost)](https://learningdata.dev)
[![Portfolio Badge](https://img.shields.io/badge/-Portfolio-%238390A2?style=&logo=adobe)](https://geovanasousa.com)
[![Linkedin Badge](https://img.shields.io/badge/-Geovana-blue?style=&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/geovana--sousa/)](https://www.linkedin.com/in/geovana--sousa/) 
[![UpWork Badge](https://img.shields.io/badge/-UpWork-%23008329?style=&logo=upwork)](https://www.upwork.com/freelancers/~011b2cff3928142907)
[![Gmail Badge](https://img.shields.io/badge/-geovanasslima-c14438?style=&logo=Gmail&logoColor=white&link=mailto:geovanasslima@gmail.com)](mailto:geovanasslima@gmail.com)
