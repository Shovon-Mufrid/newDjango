from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician, Album
from templates.first_app import forms 

# Create your views here.
# view name is index
# parameter is request / or anything, its varible type

# templates
def index(request):
   musician_list = Musician.objects.order_by('first_name')
   dictionary = { 'text_1' : 'List of Musicians' , 'musician' : musician_list }
   return render(request, 'first_app/index.html', context=dictionary)


def form(request):
   # sumitting form in DATABASE
   newForm = forms.Musician_form()

   if request.method == 'POST':
      newForm = forms.Musician_form(request.POST)

      if newForm.is_valid():
         newForm.save(commit=True) #save info in databse
         return index(request) #call data to index.html page
      
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

   dictionary = {'newForm': newForm}
   return render(request, 'first_app/form.html', context=dictionary)



# def index(request):
#     return HttpResponse("<h1>HELLO WORLD!</h2> <a href='/first_app/contact/'> Contact </a> <a href='/first_app/about/'>About</a>")

# def about(request):
#     return HttpResponse("<h1>This Is About page</h1> <a href='/first_app/home/'> Home </a>  <a href='/first_app/contact/'> Contact </a> ")

# def contact(request):
#     return HttpResponse("<h1>This is contact page</h1> <a href='/first_app/home/'> Home</a> <a href='/first_app/about/'> About </a>") 