# Acesse esse material diretamente pelo Notion!

```python
https://grizzly-amaranthus-f6a.notion.site/Aula-1-PSW-6-0-f358927b96914721aea51412a400714f
```

### Conceitos

![Cliente servidor.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c6076cc0-2d69-4c17-9b9f-f2a51d2ddb24/Cliente_servidor.png)

Fluxo de dados no Django:

![diagrama fluxo.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/58b0d368-2402-481a-9bca-2101f71cf6b4/diagrama_fluxo.png)

### O projeto

Link do FIGMA:

[https://www.figma.com/file/NYEOiXmkj8vTQuH9P02oCf/Untitled?node-id=0%3A1&t=vrinTU7MlRjoCuXJ-1](https://www.figma.com/file/NYEOiXmkj8vTQuH9P02oCf/Untitled?node-id=0%3A1&t=vrinTU7MlRjoCuXJ-1)

### Configurações iniciais

Primeiro devemos criar o ambiente virtual:

```python
# Criar
	# Linux
		python3 -m venv venv
	# Windows
		python -m venv venv
```

Após a criação do venv vamos ativa-lo:

```python
#Ativar
	# Linux
		source venv/bin/activate
	# Windows
		venv\Scripts\Activate

# Caso algum comando retorne um erro de permissão execute o código e tente novamente:

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Agora vamos fazer a instalação do Django e as demais bibliotecas:

```python
pip install django
pip install pillow
```

Vamos criar o nosso projeto Django:

```jsx
django-admin startproject type_event .
```

Crie o app usuarios:

## Instale o APP!

```jsx
python3 manage.py startapp usuarios
```

Crie uma URL para o APP usuarios:

```jsx
path('usuarios/', include('usuarios.urls')),
```

### Cadastro

Crie uma URL para o cadastro de usuários:

```jsx
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
]
```

Agora crie a view cadastro para exibir a interface de cadastro:

```python
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
```

Configure onde o Django irá procurar por HTML:

```python
os.path.join(BASE_DIR, 'templates')
```

Crie um HTML base em templates/bases/base.html:

```python
{% load static %}
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>{% block 'title' %}{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    {% block 'head' %}{% endblock %}
  
  </head>
  <body>
    {% block 'body' %}{% endblock %}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>
```

Crie o cadastro.html

```python
{% extends 'bases/base.html' %}
{% load static %}
{% block 'head' %}
    
{% endblock %}

{% block 'body' %}

    <div class="container-fluid bg-inscricao">
        
        <div class="row">
            <div class="col-md">
                <h3 class="logo">Type.Event</h3>

                

                <img src="{% static 'geral/img/logo_evento.png' %}" class="logo-evento">

            </div>

            <div class="col-md bg-img">
            
            </div>
        
        </div>
    </div>

{% endblock %}
```

Configure os arquivos estáticos:

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'templates/static'),)
STATIC_ROOT = os.path.join('static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

Crie o base.css em geral/css/base.css:

```python
body{
    color: white !important;
}

:root{
     
    --main-color: #201F1F;
    --dark-color: #1C1A1A;
    --contrast-color: #BE375F;
    --differential-color: #ED8554;

}
```

Importe o CSS base:

```python
<link href="{% static 'geral/css/base.css' %}" rel="stylesheet">
```

Crie o usuarios.css:

```python
.bg-inscricao{

    height: 100vh;
    background-color: var(--dark-color);
    padding-left: 1%;
}

.bg-img{
    background-image: url('/static/usuarios/img/bg.png');
    height: 100vh;
    background-size: cover;
    color: #14e9e9
}

.logo{
    font-family: Arial, Helvetica, sans-serif;
    margin-top: 40px;
}

.box-form{
    width: 70%;
    background-color: var(--main-color);
    margin: auto;
    padding: 40px;
    margin-top: 4%;
    border-radius: 20px;
    box-shadow: 1px 1px 5px 1px #0e0e0e;
    height: 65vh;
}

.link{
    color: var(--differential-color);
    text-decoration: none;
}

.btn-principal{
    
    background-color: transparent;
    border: 1px solid var(--contrast-color);
    color: white;
    padding: 10px;
    border-radius: 10px;
    font-weight: bold;
}

.logo-evento{

    position: fixed;
    bottom: 20px;

}
```

importe o CSS em cadastro:

```python
<link href="{% static 'usuarios/css/usuarios.css' %}" rel="stylesheet">
```

Adicione a logo do evento!

Adicione a imagem de fundo!

Crie o partial para o formulário de cadastro em templates/partials/usuarios/cadastro.html:

```python
<div class="box-form">
    <h3>CADASTRO</h3>
    <hr style="border-color: #7E7B7C">

    <form action="#" method="POST">
        <label>Username:</label> 
        <input type="text" class="form-control" placeholder="Username..." name="username">
        <br>
        <label>E-mail:</label>
        <input type="email" class="form-control" placeholder="E-mail..." name="email">
        <br>
        <div class="row">
            <div class="col-md">
                <label>Senha:</label>
                <input type="password" class="form-control" placeholder="Senha..." name="senha">
            </div>

            <div class="col-md">
                <label>Confirmar senha:</label>
                <input type="password" class="form-control" placeholder="Confirmar senha..." name="confirmar_senha">
            </div>
        </div>
        <a href="#" class="link">Já possuo uma conta</a>
        <br>
        <br>
        <input type="submit" value="CADASTRAR" class="btn-principal">
    </form>
</div>
```

Inclua o arquivo o partial de cadastro no HTML principal:

```python
{% include "partials/usuarios/cadastro.html" %}
```

Envie os dados do formulário para URL:

```python
<form action="{% url 'cadastro' %}" method="POST">
```

Execute as migrações

Adicione o cadastro de usuários na view cadastro:

```python
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not (senha == confirmar_senha):    
            return redirect(reverse('cadastro'))
        
        user = User.objects.filter(username=username)

        if user.exists():
            return redirect(reverse('cadastro'))   
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        return redirect(reverse('login'))
```

Configure as mensagens:

```python
from django.contrib.messages import constants
MESSAGE_TAGS = {
    constants.DEBUG: 'alert-primary',
    constants.ERROR: 'alert-danger',
    constants.WARNING: 'alert-warning',
    constants.SUCCESS: 'alert-success',
    constants.INFO: 'alert-info ',
}
```

Adicione as mensagens na view cadastro:

```python
from django.contrib import messages
from django.contrib.messages import constants

messages.add_message(request, constants.ERROR, 'Mensagem')
```

Exiba as mensagens no HTML:

```python
{% if messages %}
    {% for message in messages %}
        <div class="alert {{ message.tags }}">{{ message }}</div>
    {% endfor %}
{% endif %}
```

### Login

Crie a URL para login:

```python
path('login/', views.login, name='login'),
```

Crie a view para o login:

```python
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
```

Crie o HTML para login:

```python
{% extends 'bases/base.html' %}
{% load static %}
{% block 'head' %}
    <link href="{% static 'usuarios/css/usuarios.css' %}" rel="stylesheet">
{% endblock %}

{% block 'body' %}

    <div class="container-fluid bg-inscricao">
        
        <div class="row">
            <div class="col-md">
                <h3 class="logo">Type.Event</h3>

               

                <img src="{% static 'geral/img/logo_evento.png' %}" class="logo-evento">

            </div>

            <div class="col-md bg-img">
            
            </div>
        
        </div>
    </div>

{% endblock %}
```

Crie o partial do form de login:

```python
<div class="box-form">
    <h3>LOGIN</h3>
    {% if messages %}
        {% for message in messages %}
            <div class="alert {{ message.tags }}">{{ message }}</div>
        {% endfor %}
    {% endif %}
    <hr style="border-color: #7E7B7C">

    <form action="{% url 'login' %}" method="POST">{% csrf_token %}
        <label>Username:</label>
        <input type="text" class="form-control" placeholder="Username..." name="username">
        <br>    
        <label>Senha</label>
        <input type="password" class="form-control" placeholder="Senha..." name="senha">
            
        <a href="{% url 'cadastro' %}" class="link">Cadastre-se</a>
        <br>
        <br>
        <input type="submit" value="LOGAR" class="btn-principal">
    </form>
</div>
```

Adicione o partial em login.html:

```python
{% include "partials/usuarios/login.html" %}
```

Crie a view para efetuar o login do usuário:

```python
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=username, password=senha)

        if not user:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
            return redirect(reverse('login'))
        
        auth.login(request, user)
        return redirect('/eventos/novo_evento/')
```

### Novo evento

Crie um novo app chamado eventos:

```python
python3 manage.py startapp eventos
```

Instale o APP!

Crie uma URL para eventos:

```python
path('eventos/', include('eventos.urls')),
```

Crie uma URL para NOVO EVENTO:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('novo_evento/', views.novo_evento, name="novo_evento"),
]
```

Crie o HTML base de evento o base_evento.html:

```python
{% extends 'bases/base.html' %}
{% load static %}

{% block 'head' %}

    {% block 'importacoes' %}{% endblock %}
    <link href="{% static 'evento/css/evento.css' %}" rel="stylesheet">
    <link href="{% static 'usuarios/css/usuarios.css' %}" rel="stylesheet">

{% endblock %}

{% block 'body' %}
    <nav class="navbar navbar-expand-lg bg-body-tertiary navbar-color" data-bs-theme="dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Type.Event</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavDropdown">
            <ul class="navbar-nav">
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Empresa
                    </a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="">Criar novo evento</a></li>
                        <li><a class="dropdown-item" href="">Gerenciar eventos</a></li>
                    </ul>
                </li>
                
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Cliente
                    </a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="">Meus eventos</a></li>
                        <li><a class="dropdown-item" href="">Meus certificados</a></li>
                    </ul>
                </li>
            </ul>
            </div>
        </div>
    </nav>

    <div style="min-height: 60vh">
        {% block 'conteudo' %}

        {% endblock %}
    </div>

    <div class="fundo-pagina">
        
    </div>
{% endblock %}
```

Crie o CSS de evento:

```python
.navbar-color{
    background-color: #201F1F !important;
}

body{
    background-color: #1C1A1A;
}

.fundo-pagina{
    background-image: url('/static/evento/img/fundo_pagina.png');
    height: 300px;
    background-size: cover;
    
}
```

Adicione a imagem de fundo!

Crie o HTML de novo_evento:

```python
{% extends "bases/base_evento.html" %}

{% block 'conteudo' %}
    <div class="container">
        <div class="row">
            <div class="col-md-7">
                <br>
                {% if messages %}
                    {% for message in messages %}
                        <div class="alert {{ message.tags }}">{{ message }}</div>
                    {% endfor %}
                {% endif %}
                <br>
                <h3>Novo evento</h3>
                <form action="{% url 'novo_evento' %}" method="POST" enctype="multipart/form-data">{% csrf_token %}
                    <label>Nome evento</label>
                    <input type="text" name="nome" class="form-control" placeholder="Nome...">
                    <br>
                    <label>Descrição</label>
                    <textarea name="descricao" class="form-control" placeholder="Descrição..."></textarea>
                    <br>
                    <div class="row">
                        <div class="col-md">
                            <label>Data início</label>
                            <input type="date" name="data_inicio" class="form-control">
                        </div>
                        <div class="col-md">
                            <label>Data término</label>
                            <input type="date" name="data_termino" class="form-control">
                        </div>
                    </div>
                    <br>
                    <label>Carga horária (em horas)</label>
                    <input type="number" name="carga_horaria" class="form-control" placeholder="X horas">
                    <br>
                    <label>Logo do evento</label>
                    <input type="file" name="logo" class="form-control">
                
            </div>

            <div style="z-index: 99999" class="col-md">
                <br>
                <br>
                <h3>Paleta de cores</h3>
                <br>
                <input type="color" name="cor_principal" value="#15773b"> <span>Cor principal</span>
                <br>
                <input type="color" name="cor_secundaria" value="#14e9e9"> <span>Cor secundária</span>
                <br>
                <input type="color" name="cor_fundo" value="#020202"> <span>Cor de fundo</span>
                <br>
                <br>
                <input type="submit" class="btn-principal" value="Criar evento">
                </form>
            </div>
            <form>
        </div>
    </div>

{% endblock %}
```

Permita que apenas usuários logados acessa a página:

```python
from django.contrib.auth.decorators import login_required

@login_required
```

Crie o banco de dados para o Evento:

```python
from django.contrib.auth.models import User

class Evento(models.Model):
    criador = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_termino = models.DateField()
    carga_horaria = models.IntegerField()
    logo = models.FileField(upload_to="logos")

    #paleta de cores
    cor_principal = models.CharField(max_length=7)
    cor_secundaria = models.CharField(max_length=7)
    cor_fundo = models.CharField(max_length=7)
    

    def __str__(self):
        return self.nome
```

Execute as migrações!

Crie a views para salvar o evento:

```python
@login_required
def novo_evento(request):
    if request.method == "GET":
        return render(request, 'novo_evento.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        data_inicio = request.POST.get('data_inicio')
        data_termino = request.POST.get('data_termino')
        carga_horaria = request.POST.get('carga_horaria')

        cor_principal = request.POST.get('cor_principal')
        cor_secundaria = request.POST.get('cor_secundaria')
        cor_fundo = request.POST.get('cor_fundo')
        
        logo = request.FILES.get('logo')
        
        evento = Evento(
            criador=request.user,
            nome=nome,
            descricao=descricao,
            data_inicio=data_inicio,
            data_termino=data_termino,
            carga_horaria=carga_horaria,
            cor_principal=cor_principal,
            cor_secundaria=cor_secundaria,
            cor_fundo=cor_fundo,
            logo=logo,
        )
    
        evento.save()
        
        messages.add_message(request, constants.SUCCESS, 'Evento cadastrado com sucesso')
        return redirect(reverse('novo_evento'))
```