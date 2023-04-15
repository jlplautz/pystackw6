# AULA 3 | PSW 6.0

## Arquivos

[template_certificado.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ddb0e03a-f8c6-45e7-9ca1-3921a4c0a6c5/template_certificado.png)

[arimo.ttf](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fa7d3d84-71ce-4cf7-b8bf-cf668fd62ec9/arimo.ttf)

## Certificados

### Crie a models para salvar os certificados:

```python
class Certificado(models.Model):
    certificado = models.ImageField(upload_to="certificados")
    participante = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    evento = models.ForeignKey(Evento, on_delete=models.DO_NOTHING)
```

### Crie a URL para certificados:

```python
path('certificados_evento/<int:id>/', views.certificados_evento, name="certificados_evento"),
```

### Execute as migrações!

### Crie a view certificados_evento:

```python
def certificados_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if not evento.criador == request.user:
        raise Http404('Esse evento não é seu')
    if request.method == "GET":
        qtd_certificados = evento.participantes.all().count() - Certificado.objects.filter(evento=evento).count()
        return render(request, 'certificados_evento.html', {'evento': evento, 'qtd_certificados': qtd_certificados})
```

### Crie o HTML certificados_evento:

```python
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
                        <span class="badge rounded-pill text-bg-danger"><a class="link" href="{% url 'certificados_evento' evento.id %}">Certificados</a></span>
                    </div>
                </div>
            </div>
        </div>
        <hr>

        <div class="row">
            <h5>{{qtd_certificados}} Certificados para serem gerados</h5>            
                <a href="#" class="btn-principal link" style="width: 40%">GERAR TODOS OS CERTIFICADOS</a>
        </div>
        <hr>

        <div class="row">
            <h5>Procurar certificado</h5>
            <br>
            <form action="" method="">
                <input type="email" class="form-control" placeholder="Digite o e-mail" name="email">{% csrf_token %}
                <br>
                <input type="submit" value="BUSCAR" class="btn btn-primary">
            </form>
        </div>
        
        
    </div>

{% endblock %}
```

### Verifique se existe certificados para exibir o botão:

```python
{% if qtd_certificados > 0 %}
    <a href="#" class="btn-principal link" style="width: 40%">GERAR TODOS OS CERTIFICADOS</a>
{% endif %}
```

### Crie a URL para a view gerar_certificado:

```python
path('gerar_certificado/<int:id>/', views.gerar_certificado, name="gerar_certificado"),
```

### Crie a VIEW gerar_certificado:

```python
from io import BytesIO  
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image, ImageDraw, ImageFont
import sys

def gerar_certificado(request, id):
    evento = get_object_or_404(Evento, id=id)
    if not evento.criador == request.user:
        raise Http404('Esse evento não é seu')

    path_template = os.path.join(settings.BASE_DIR, 'templates/static/evento/img/template_certificado.png')
    path_fonte = os.path.join(settings.BASE_DIR, 'templates/static/fontes/arimo.ttf')
    for participante in evento.participantes.all():
        # TODO: Validar se já existe certificado desse participante para esse evento
        img = Image.open(path_template)
        path_template = os.path.join(settings.BASE_DIR, 'templates/static/evento/img/template_certificado.png')
        draw = ImageDraw.Draw(img)
        fonte_nome = ImageFont.truetype(path_fonte, 60)
        fonte_info = ImageFont.truetype(path_fonte, 30)
        draw.text((230, 651), f"{participante.username}", font=fonte_nome, fill=(0, 0, 0))
        draw.text((761, 782), f"{evento.nome}", font=fonte_info, fill=(0, 0, 0))
        draw.text((816, 849), f"{evento.carga_horaria} horas", font=fonte_info, fill=(0, 0, 0))
        output = BytesIO()
        img.save(output, format="PNG", quality=100)
        output.seek(0)
        img_final = InMemoryUploadedFile(output,
                                        'ImageField',
                                        f'{token_urlsafe(8)}.png',
                                        'image/jpeg',
                                        sys.getsizeof(output),
                                        None)
        certificado_gerado = Certificado(
            certificado=img_final,
            participante=participante,
            evento=evento,
        )
        certificado_gerado.save()
    
    messages.add_message(request, constants.SUCCESS, 'Certificados gerados')
    return redirect(reverse('certificados_evento', kwargs={'id': evento.id}))
```

### Crie o arquivos!

Redirecione o botão para URL:

```python
{% url 'gerar_certificado' evento.id %}
```

## Procurar certificados

### Crie uma URL para procurar e exibir um certificado:

```python
path('procurar_certificado/<int:id>/', views.procurar_certificado, name="procurar_certificado")
```

### Crie a VIEW para procurar um certificado:

```python
def procurar_certificado(request, id):
    evento = get_object_or_404(Evento, id=id)
    if not evento.criador == request.user:
        raise Http404('Esse evento não é seu')
    email = request.POST.get('email')
    certificado = Certificado.objects.filter(evento=evento).filter(participante__email=email).first()
    if not certificado:
        messages.add_message(request, constants.WARNING, 'Certificado não encontrado')
        return redirect(reverse('certificados_evento', kwargs={'id': evento.id}))
    
    return redirect(certificado.certificado.url)
```

### Envie o form para a URL criada:

```python
<form action="{% url 'procurar_certificado' evento.id %}" method="POST">
    <input type="email" class="form-control" placeholder="Digite o e-mail" name="email">{% csrf_token %}
    <br>
    <input type="submit" value="BUSCAR" class="btn btn-primary">
</form>
```

## Clientes

### Crie um APP para clientes e faça a instalação!

### Crie uma URL para o APP:

```python
path('cliente/', include('cliente.urls'))
```

### Crie uma URL para certificados:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('meus_certificados/', views.meus_certificados, name="meus_certificados"),
]
```

### Crie a VIEW para exibir os certificados:

```python
def meus_certificados(request):
    certificados = Certificado.objects.filter(participante=request.user)
    return render(request, 'meus_certificados.html', {'certificados': certificados})
```

### Agora crie o HTML:

```python
{% extends "bases/base_evento.html" %}
{% load static %}

{% block 'conteudo' %}

<div class="container">
    <br>
    <br>
    <div class="row">
        {% for certificado in certificados %}
            <div class="col-md-4">
                <img src="{{certificado.certificado.url}}" width="100%">

                
            </div>
        {% endfor %}
    </div>
</div>

{% endblock %}
```