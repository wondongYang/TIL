## PJT05 CODES

- templates/base.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
  </head>
  <body>
  <div class="container">
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link" href="{% url 'movies:index' %}">영화목록</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{% url 'movies:create' %}">영화작성</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  </div>
    <div class="container">
    {% block content %}
    
    {% endblock content %}
    </div>
  
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>
  </body>
  </html>
  ```

  

- pjt05/urls.py

  ```python
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('movies/', include('movies.urls')),
  ]
  ```

  

- movies/urls.py

  ```python
  from django.urls import path
  from . import views
  
  app_name = 'movies'
  urlpatterns = [
      path('', views.index, name='index'),
      path('create/', views.create, name='create'),
      path('<int:pk>/', views.detail, name='detail'),
      path('<int:pk>/update/', views.update, name='update'),
      path('<int:pk>/delete/', views.delete, name='delete'),
  ]
  ```

  

- movies/views.py

  ```python
  from django.shortcuts import redirect, render
  from .models import Movie
  from .forms import MovieForm
  
  # Create your views here.
  def index(request):
      movies = Movie.objects.order_by('-pk')
      context = {
          'movies': movies
      }
      return render(request, 'movies/index.html', context)
  
  def create(request):
      if request.method == "POST":
          form = MovieForm(request.POST)
          if form.is_valid():
              movie = form.save()
              return redirect('movies:detail', movie.pk)
      else:
          form = MovieForm()
      
      context = {
          'form': form
      }
      return render(request, 'movies/create.html', context)
  
  def detail(request, pk):
      movie = Movie.objects.get(pk=pk)
      context = {
          'movie': movie
      }
      return render(request, 'movies/detail.html', context)
  
  def update(request, pk):
      movie = Movie.objects.get(pk=pk)
      if request.method == "POST":
          form = MovieForm(request.POST, instance=movie)
          if form.is_valid():
              form.save()
              return redirect('movies:detail', movie.pk)
      else:
          form = MovieForm(instance=movie)
      
      context = {
          'movie': movie,
          'form': form,
      }
      return render(request, 'movies/update.html', context)
  
  def delete(request, pk):
      movie = Movie.objects.get(pk=pk)
      movie.delete()
      return redirect('movies:index')
  ```

  

- movies/models.py

  ```python
  from django.db import models
  
  # Create your models here.
  class Movie(models.Model):
      title = models.CharField(max_length=100)
      overview = models.TextField()
      poster_path = models.CharField(max_length=500)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  
      def __str__(self):
          return self.title
  ```

  

- movies/forms.py

  ```python
  from django import forms
  from .models import Movie
  
  class MovieForm(forms.ModelForm):
  
      class Meta:
          model = Movie
          fields = '__all__'
  ```

  

- movies/admin.py

  ```python
  import movies
  from django.contrib import admin
  from .models import Movie
  
  # Register your models here.
  admin.site.register(Movie)
  ```

  

- movies/templates/movies/index.html

  ```html
  {% extends 'base.html' %}
  
  {% block content %}
  <h1>영화목록</h1>
  <hr>
      {% for movie in movies %}
          <li>
          <a href="{% url 'movies:detail' movie.pk%}">{{ movie.title }}</a>
          <hr>
          </li>
      {% endfor %}
  {% endblock content %}
  ```

  

- movies/templates/movies/create.html

  ```html
  {% extends 'base.html' %}
  
  {% block content %}
  <h1>영화작성</h1>
  <form action="{% url 'movies:create' %}" method="POST">
      {% csrf_token %}
      {{ form.as_p }}
      <input type="submit" value="제출">
  </form>
  <a href="{% url 'movies:index' %}">[BACK]</a>
  {% endblock content %}
  ```

  

- movies/templates/movies/detail.html

  ```html
  {% extends 'base.html' %}
  
  {% block content %}
  <h1>영화상세</h1>
  <p>영화 제목: {{ movie.title }}</p>
  <p>줄거리: {{ movie.overview }}</p>
  <img src="{{ movie.poster_path }}" alt="movie_image">
  
  <hr>
  <a href="{% url 'movies:update' movie.pk %}">[EDIT]</a>
  <br>
  <a href="{% url 'movies:delete' movie.pk %}">[DELETE]</a>
  <br>
  <a href="{% url 'movies:index' %}">[BACK]</a>
  {% endblock content %}
  ```

  

- movies/templates/movies/update.html

  ```html
  {% extends 'base.html' %}
  
  {% block content %}
  <h1>영화수정</h1>
  <form action="{% url 'movies:create' %}" method="POST">
      {% csrf_token %}
      {{ form.as_p }}
      <input type="submit" value="제출">
  </form>
  <a href="{% url 'movies:index' %}">[BACK]</a>
  {% endblock content %}
  ```

  