# ProyectoBaseDiseno
> python manage.py runserver

#Continuando con la customización de la página... hemos de poner todo lo que no habíamos puesto en nuestro HTML base.
De abajo (dese el footer) hacia arriba (hasta el showcase).

Hacer lo mismo con "about.html" (desde el navbar hasta el footer). 

Seguimos definimos la imagen estàtica que se encontrarà en "about.html". Mira los comentarios del doc. 
Ahora le daremos enlaces a los botones de los crumbreads. 
#Aqui redefinimos el link. 
            <a href="{% url 'index' %}">
Repetimos esto en _navbar.html. 
Donde vemos el documento comentado, tenemos vìnculos a las otras páginas. Ya podemos ir y venir con los botones y el logo. 
Tomar en cuenta que la referencia se hace desde urls.py.

Makign dynamic highlighting: 
<li
            {% if '/' == request.path %}
                class="nav-item active mr-3"{
            {% else %}
              class="nav-item mr-3"
            {% endif %}
          >
Aplica para todos los botones. 
<li
            {% if 'about' in request.path %}
                class="nav-item active mr-3"{
            {% else %}
              class="nav-item mr-3"
            {% endif %}
          >

CREATING LISTINGS AND REALTORS APPS
python manage.py startapp listings.
Crear ambas apps, y agregar html template files a templates > listings.
Crear en listings un documento llamado: urls.py y pegar lo que habia en pages > urls.py

Conectando con una db:

En BTRE > sTATIC > settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'btredb',
        'USER': 'postgres',
        'PASSWORD': 'chema03',
        'HOST': 'localhost'
    }
}

#Creando modelos:Listings > models.py
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    bedrooms = models.IntegerField()
    sqft = models.DecimalField(max_digits=5, decimal_places=1)
    lost_size = models.DecimalField(max_digits=5, decimal_places=1)
    #Formato de fecha para las imagenes
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title;


#Creando modelos: Realtors> models.py
class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_datte = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name

#Corriendo las migraciones: 
pip install Pillows #(para usar el ImageField)
python manage.py makemigrations

Ir a Listings > migrations > 0001_intial... para ver la migración del modelo a la bd
#Aquì se muestra el modelo. 
python manage.py sqlmigrate listings 0001


#Admin Area!!
python manage.py createsuperuser
user: chema
pass: chema03
email: isharedocsjmg@gmail.com

#Queremos añadir usuarios y listings. 
#listings > admin.py

from .models import Listing

admin.site.register(Listing)

#Ya puedes agregar datos con una interfaz predeterminada, lol.
#Para ver media files en el frontend:
+ static(settings.MEDIA_URL, document_root=settings.MEDIAROOT)

#Custom admin area
Templates > New Folder > admin > new base_site.html
{% extends 'admin/base.html' %}
{% load static %}
{% block branding %}

<h1 id="head">
    <img src="{% static 'img/logo.png' %}" alt="BT Real State" height="50"
         width="80" class="brand_img">   Admin Area
</h1>
{% endblock %}
{% block extrastyle %}
    <link rel="stylesheet" href="{% static 'css/admin.css' %}">
{% endblock %}

#CSS para darle el mismo tema de color 
#header{
    background: #10284e;
    height: 50px;
    color: #fff
}
#branding h1{
    color: #fff
}

a:link,
a:visited{
    color: #10284e;
}
div.breadcrumbs {
    background: #30caa0;
    color: #10284e;
}

div.breadcrumbs a{
    color: #333333;
}

#header{
    background: #10284e;
    height: 50px;
    color: #fff
}
#branding h1{
    color: #fff
}

a:link,
a:visited{
    color: #10284e;
}
div.breadcrumbs {
    background: #30caa0;
    color: #10284e;
}

div.breadcrumbs a{
    color: #333333;
}

Para los titulos de tablas de home
Esto se sacò de la herramienta de Chrome
.module h2, .module caption, .inline-group h2{
    background: #30caa0;
}
Falta darle color a los botones... revisar el ss. 
#Modificando la data del area de modificaci[on de los listings
> Listings > admin.py

#Esta clase me muestra los parámetros que le indiques. 
from django.contrib import admin

from .models import Listing

#Esta clase meuestra diferentes elementos para manejar la visualización de los datos de la sección admin de cada aplicación.  
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    #se puede aplicar para cualquier campo
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state',
                     'zipcode', 'price')
    list_per_page = 25
admin.site.register(Listing, ListingAdmin)

#Lo mismo aplica para Realtos > admin.py

from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_datte')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25
admin.site.register(Realtor, RealtorAdmin)	

#Llevar información del backend al front end:



#Si estas en vsCode instala pylint Django: pip install pylint-django, para esta modificacion en: listings > views.py

#Pasaremos datos del modelo desde un diccionario.
def index(request):
    #Trayendo "Listings" desde la DB:
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'listings/listings.html')


#Agregar lo siguiente a: 
> Templates >listings > admin.py
{% if listings %}
          {% for listing in listings %}

<!--Listing 1-->
          {% endfor %}
        {% else %}

          <div class="col-md-12">
              <p>No Listings Available</p>
          </div>
      {% endif %}
#Ahora hacemos un elemento "Listing" dinámico en HTML:



