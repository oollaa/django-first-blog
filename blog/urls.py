from django.conf.urls import url #importujemy funkcję 'url', listę adresów,
#na którą jesteśmy w stanie odpowiedzieć
from . import views #'.' to lokalny katalog

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),#przychodzi zapytanie do serwera,
    #r=wyrażenie regularne
    #daszek = ma się zaczynać od tego, co następne
    #$ ma sie kończyć
    #czyli ma być pyste, (zaczyna się od końca, jednocześnie zaczyn się i kończy)
]
