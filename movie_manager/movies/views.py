from django.shortcuts import render
from .models import MovieInfo
from .forms import MovieInfoForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login/')
def movie_list(request):
    print(request.COOKIES)
    visits = request.COOKIES.get('visits', 0)
    visits = int(visits) + 1
    movie_data = MovieInfo.objects.all()
    #print(movie_data)

    response = render(request,'list.html',{'movies': movie_data, 'visits': visits} )
    response.set_cookie('visits', visits)
    return response

@login_required(login_url='login/')
def movie_create(request):

    
    if request.POST or request.FILES:
        # Process form data and create a new movie
        # print(request.POST)
        frm = MovieInfoForm(request.POST, request.FILES)
        #print(frm.is_valid())
        if frm.is_valid():
            frm.save()
    else:
        frm = MovieInfoForm()
            

    return render(request,'create.html', {'frm': frm})

@login_required(login_url='login/')
def movie_edit(request, pk):
    edit_movie = MovieInfo.objects.get(pk = pk)

    if request.POST:
        frm = MovieInfoForm(request.POST, instance=edit_movie)
        if frm.is_valid():
            edit_movie.save()
    else:   
        frm = MovieInfoForm(instance=edit_movie)

    return render(request,'create.html', {'frm': frm})

def movie_delete(request, pk):
    delete_movie = MovieInfo.objects.get(pk=pk)
    delete_movie.delete()
    movie_data = MovieInfo.objects.all()
    #print(movie_data)
    return render(request,'list.html',{'movies': movie_data} )
   