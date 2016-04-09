from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model): #nasza klasa dziedziczy 'modles' z biblioteki 'Models'
#rozszerzamy już instniejącą klasę. Poniżej informacje, jak zapisać daną klasę w bazie danych. Jak utworzyć odpowiednią tebelą
    author = models.ForeignKey("auth.User") #klucz z innej tabeli, podpinamy się pod inną tabelę, auth.User
    title = models.CharField(max_length=200) #CharField, to ciąg znaków (a maksymalnej długości)
    text = models.TextField() #pole z tekstem,bez ograniczania ilości znaków
    crated_date = models.DateTimeField(default=timezone.now) #domyślnie uzupełniamy bazę danych w kwestii czasu
    published_date = models.DateTimeField(blank=True, null=True) #jak nic nie wpisujemy, tzn blank=True, to by default wpisujemy 'null'

    def publish(self):
        self.published_date = timezone.now()
        self.save() #self odnosi się do konkretnego obiektu, w tym przypadku do 'Post' (to funkcja wewnątrz klasy, parameterm będzie zawsze self)

    def __str__(self):#jak chę zobaczyć obiekt na konsoli (tutaj: Post) ta funkcja nam powi co nam się wyświetli
        return self.title #tutaj wyświetli nam się tylko tytuł posta (w konsoli)
        
