# AULA 2 | PSW 6.0
## Gerenciar evento
## Inscrever evento
## Lista de participantes


# Gerenciar evento
## Crie uma nova url:

    path('gerenciar_evento/', views.gerenciar_evento, name="gerenciar_evento"),

## Crie uma nova url:

    def gerenciar_evento(request):
        if request.method == "GET":
            return render(request, 'gerenciar_evento.html')

## Crie o HTML de gerenciar evento:

    {% extends "bases/base_evento.html" %}
    {% load static %}

    {% block 'importacoes' %}
        <link href="{% static 'evento/css/gerenciar_evento.css' %}" rel="stylesheet">
    {% endblock %}

    {% block 'conteudo' %}
        <div class="container">
            <br>
            <div class="row">
                <div class="col-md">
                    <form action="" method="titulo">
                    <label>Título:</label>
                    <input type="text" placeholder="Título..." class="form-control" name="nome">
                </div>

                <div class="col-md">
                    <br>
                    <input type="submit" class="btn-principal" value="filtrar">
                    </form>
                </div>

            </div>
            <table>
                <tr>
                    <th>Logo</th>
                    <th>Título</th>
                    <th>Descrição</th>
                    <th>Início</th>
                    <th>Término</th>
                    <th>Link de inscrição</th>
                </tr>
                
                <tr class="{% cycle 'linha' 'linha2' %}">
                    <td width="10%"><a href="#"><img width="100%" src="#"></a></td>
                    <td>Nome</td>
                    <td>Descrição</td>
                    <td>Data de Início</td>
                    <td>Data de término</td>
                    <td>Link de inscrição</td>
                </tr>
                    
            </table>

        </div>

    {% endblock %}


## Crie o CSS de gerenciar evento:

    table{
        width: 100%;
        padding: 20px;
    }

    .linha{
        height: 40px;
        background-color: var(--main-color);
        padding: 20px;
    }


    td, th{
        padding: 20px;
    }

## Agora vamos exibir dinamicamente os eventos do usuário:

    def gerenciar_evento(request):
        if request.method == "GET":
            eventos = Evento.objects.filter(criador=request.user)
            return render(request, 'gerenciar_evento.html', {'eventos': eventos})

## Exiba dinamicamente nos templates:

    {% for evento in eventos %}
        <tr class="{% cycle 'linha' 'linha2' %}">
            <td width="10%"><a href="#"><img width="100%" src="/media/{{evento.logo}}"></a></td>
            <td>{{evento.nome}}</td>
            <td>{{evento.descricao}}</td>
            <td>{{evento.data_inicio}}</td>
            <td>{{evento.data_termino}}</td>
            <td>Link</td>
        </tr>
    {% endfor %}


## Configure a URL para os arquivos de media:

    from django.contrib import admin
    from django.urls import path, include
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('usuarios/', include('usuarios.urls')),
        path('eventos/', include('eventos.urls')),
        
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


## Adicione o action do form para filtrar os eventos:

    {% url 'gerenciar_evento' %}


## Receba nas views e faça o filtro:

    def gerenciar_evento(request):
        if request.method == "GET":
            nome = request.GET.get('nome')
            eventos = Evento.objects.filter(criador=request.user)
            if nome:
                eventos = eventos.filter(nome__contains=nome)

            return render(request, 'gerenciar_evento.html', {'eventos': eventos})


# Inscrever evento

## Crie a URL para outras pessoas se inscreverem no evento:

    path('inscrever_evento/<int:id>/', views.inscrever_evento, name="inscrever_evento"),
    
## Crie a view inscrever_evento:

    def inscrever_evento(request, id):
		# Validar login
        evento = get_object_or_404(Evento, id=id)
        if request.method == "GET":
            return render(request, 'inscrever_evento.html', {'evento': evento})

## Crie o HTML de inscrição no evento:

    {% extends 'bases/base_evento.html' %}


    {% block 'conteudo' %}
        <br>
        <br>
        <div class="container">
            <div class="row">
                <div class="col-md-3">
                
                    <img width="100%" src="{{evento.logo.url}}">
                    <br>
                    <br>
                    <h3>{{evento.nome}}</h3>
                </div>
                <hr>

                <div class="col-md-6">
                    <h5>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s</h5>
                    <br>
                    <p>{{evento.data_inicio}} a {{evento.data_termino}}</p>

                    <a style="text-decoration: none;" class="btn-principal" href="#">QUERO PARTICIPAR</a>
                
                </div>
            </div>
        </div>
    {% endblock %}

## Adicione o campo para participantes na tabela do banco:

    participantes = models.ManyToManyField(User, related_name="evento_participante", null=True, blank=True)

## Execute as migrações!

## Faça a inscrição na view:

    def inscrever_evento(request, id):
        evento = get_object_or_404(Evento, id=id)
        if request.method == "GET":
            return render(request, 'inscrever_evento.html', {'evento': evento})
        elif request.method == "POST":
            # Validar se o usuário já é um participante
            evento.participantes.add(request.user)
            evento.save()

            messages.add_message(request, constants.SUCCESS, 'Inscrição com sucesso.')
            return redirect(reverse('inscrever_evento', kwargs={'id': id}))


## Exiba um botão diferente se o usuário já estiver inscrito:

    {% if request.user in evento.participantes.all %}
        <input style="border-color: green;" type="submit" class="btn-principal" value="JÁ ESTÁ PARTICIPANDO" disabled>
    {% else%}
        <form action="{% url 'inscrever_evento' evento.id %}" method="POST">{% csrf_token %}
            <input type="submit" class="btn-principal" value="QUERO PARTICIPAR">
        </form>
    {% endif %}

## Exiba o link na tabela:

    http://127.0.0.1:8000/eventos/inscrever_evento/2/


# Lista de participantes

## Crie a URL para exibir a página:

    path('participantes_evento/<int:id>/', views.participantes_evento, name="participantes_evento"),

## Crie a view para exibir a página dos participantes:

    def participantes_evento(request, id):
        evento = get_object_or_404(Evento, id=id)
        if request.method == "GET":
            participantes = evento.participantes.all()[::3]
            return render(request, 'participantes_evento.html', {'evento': evento, 'participantes': participantes})

## Crie o HTML participantes_evento:

    {% extends "bases/base_evento.html" %}
    {% load static %}

    {% block 'importacoes' %}
        <link href="{% static 'evento/css/gerenciar_evento.css' %}" rel="stylesheet">
    {% endblock %}

    {% block 'conteudo' %}
        <div class="container">
            <br>
            {% if messages %}
                {% for message in messages %}
                    <div class="alert {{ message.tags }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
            <br>
            <div class="row">
                <div class="col-md-2">
                    <img width="100%" src="/media/{{evento.logo}}">
                    <br>
                    <br>
                    <h3>{{evento.nome}}</h3>
                    
                </div>

                <div class="col-md">
                    <div class="row">
                        <div class="col-md-2">
                            <span class="badge rounded-pill text-bg-danger"><a class="link" href="{% url 'participantes_evento' evento.id %}">Participantes</a></span>
                        </div>
                        <div class="col-md-2">
                            <span class="badge rounded-pill text-bg-danger"><a class="link" href="">Certificados</a></span>
                        </div>
                    </div>
                </div>
            </div>
            <hr>

            <div class="row">
                <h5>{{evento.participantes.all.count}} Participantes</h5>
                
                <div class="col-md-4">
                    <table>
                        <tr>
                            <th>Nome</th>
                            <th>E-mail</th>
                        </tr>
                        {% for participante in participantes %}
                            <tr class="{% cycle 'linha' 'linha2' %}">
                                <td>{{participante.username}}</td>
                                <td>{{participante.email}}</td>
                            </tr>
                        {% endfor %}       
                    </table>
                    <br>
                    <div class="row">
                        <div class="col-md text-center">
                            <p>X de Z</p>
                        </div>

                        <div class="col-md ">
                            <a href="#" class="btn-principal" style="text-decoration: none;">Exportar CSV</a>
                        </div>
                    </div>
                </div>
            
            </div>
            
            
        </div>

    {% endblock %}

## Valide se o evento é realmente do criador:

    if not evento.criador == request.user:
        raise Http404('Esse evento não é seu')

## Vamos criar uma URL para gerar o arquivo de participantes:

    path('gerar_csv/<int:id>/', views.gerar_csv, name="gerar_csv"),

## Crie a URL gerar CSV:

    def gerar_csv(request, id):
        evento = get_object_or_404(Evento, id=id)
        if not evento.criador == request.user:
            raise Http404('Esse evento não é seu')
        participantes = evento.participantes.all()
        
        token = f'{token_urlsafe(6)}.csv'
        path = os.path.join(settings.MEDIA_ROOT, token)

        with open(path, 'w') as arq:
            writer = csv.writer(arq, delimiter=",")
            for participante in participantes:
                x = (participante.username, participante.email)
                writer.writerow(x)

        return redirect(f'/media/{token}')

## Crie a URL gerar CSV:

    {% url 'gerar_csv' evento.id %}
