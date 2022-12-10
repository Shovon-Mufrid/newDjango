from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician, Album
from templates.second_app import forms 
from django.db.models import Avg, Max, Min


# Create your views here.
# view name is index
# parameter is request / or anything, its varible type

def index(request):
   # msuician form
   musician_list = Musician.objects.order_by('first_name')
   # album_list = Album.objects.order_by('first_name')

   dictionary = {'title':"Home Page", 'musician_list': musician_list}
   return render(request, 'second_app/index.html', context = dictionary)

def album_list(request, artist_id):
   musician_info = Musician.objects.get(pk=artist_id)
   album_list = Album.objects.filter(artist=artist_id).order_by("name","release_date")
   artist_rating = Album.objects.filter(artist=artist_id).aggregate(Avg('num_starts'))

   dictionary = {'title':"List of album", 'musician_info': musician_info, 'album_list': album_list, 'artist_rating': artist_rating}
   return render(request, 'second_app/album_list.html', context=dictionary)

def musician_form(request):
   form = forms.MusicianForm()

   if request.method == 'POST':
      form = forms.MusicianForm(request.POST)

      if form.is_valid():
         form.save(commit=True)
         return index(request) #if submit successful, it will take me to index page

   dictionary = {'title' :'Add Musician', 'musician_form': form}
   return render(request, 'second_app/musician_form.html', context=dictionary)

def album_form(request):
   form = forms.AlbumForm()

   if request.method == 'POST':
      form = forms.AlbumForm(request.POST)

      if form.is_valid():
         form.save(commit=True)
         return index(request) 

   dictionary = {'title' :'Add Album', 'album_form': form}
   return render(request, 'second_app/album_form.html', context=dictionary)
















# remv for vid 8.2
# templates
# def index(request):
#    musician_list = Musician.objects.order_by('first_name')
#    dictionary = { 'text_1' : 'List of Musicians' , 'musician' : musician_list }
#    return render(request, 'first_app/index.html', context=dictionary)

# rmv vid 8.2
# def form(request):
#    # sumitting form in DATABASE
#    newForm = forms.Musician_form()

#    if request.method == 'POST':
#       newForm = forms.Musician_form(request.POST)

#       if newForm.is_valid():
#          newForm.save(commit=True) #save info in databse
#          return index(request) #call data to index.html page
      
   # 3.7 videos
   # newForm = forms.user_form  # form.py>>> form is for form.py, user_form is class name
   # dictionary = {'newForm' : newForm}

   # if request.method == 'POST':
   #    newForm = forms.user_form(request.POST)
   #    dictionary.update({'newForm':newForm})

   #    if newForm.is_valid():
         # user_name = newForm.cleaned_data['user_name']
         # user_dob = newForm.cleaned_data['user_dob']
         # user_email = newForm.cleaned_data['user_email']
         # user_pass = newForm.cleaned_data['user_pass']
         # nationality = newForm.cleaned_data['nationality']
         # born = newForm.cleaned_data['born']
         # fav_num = newForm.cleaned_data['fav_num']
         # # cat_name = newForm.cleaned_data['cat_name']

         # dictionary.update({'user_name': user_name})
         # dictionary.update({'user_dob': user_dob})
         # dictionary.update({'user_email': user_email})
         # dictionary.update({'user_pass': user_pass})
         # dictionary.update({'nationality': nationality})
         # dictionary.update({'born': born})
         # dictionary.update({'fav_num': fav_num})
         # # dictionary.update({'cat_name': newForm.cleaned_data['cat_name']})
   
         # # boolean 
         # dictionary.update({'boolean': newForm.cleaned_data['boolean_field'] })


         # dictionary.update({'field': 'field matched' })
         # dictionary.update({'form_submitted': 'Yes'})

# rmv vid 8.2
#    dictionary = {'newForm': newForm}
#    return render(request, 'first_app/form.html', context=dictionary)


# def contact(request):
#    dictionary = {'text_1': Album.objects.get(pk=2), 'text_2': 'Sample text: '}
#    return render(request, 'first_app/contact.html', context=dictionary)









# def index(request):
#     return HttpResponse("<h1>HELLO WORLD!</h2> <a href='/first_app/contact/'> Contact </a> <a href='/first_app/about/'>About</a>")

# def about(request):
#     return HttpResponse("<h1>This Is About page</h1> <a href='/first_app/home/'> Home </a>  <a href='/first_app/contact/'> Contact </a> ")

# def contact(request):
#     return HttpResponse("<h1>This is contact page</h1> <a href='/first_app/home/'> Home</a> <a href='/first_app/about/'> About </a>") 