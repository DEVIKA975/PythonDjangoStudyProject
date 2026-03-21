from django.forms import ModelForm
from .models import MovieInfo

class MovieInfoForm(ModelForm):
    class Meta:
        model = MovieInfo
        fields = '__all__' #we can represent in list as well like fields = ['title', 'summary', 'year', 'success', 'img_name']