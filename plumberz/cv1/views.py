from django.shortcuts import render

# Create your views here.


from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'index-one.html'


class AboutPageView(TemplateView):
    template_name = 'about-one.html'


class SongsPageView(TemplateView):
    template_name = 'songs-one.html'

    
class BlogPageView(TemplateView):
    template_name = 'blog-one.html'


class BlogSinglePageView(TemplateView):
    template_name = 'blog-single.html'


class ContactPageView(TemplateView):
    template_name = 'contact-one.html'

# views.py
from django.views.generic.edit import FormView
from .forms import ContactForm
from django.urls import reverse_lazy

class ContactFormView(FormView):
    template_name = 'index-one.html'  # Replace 'your_template.html' with your actual template name
    form_class = ContactForm
    success_url = reverse_lazy('home')  # Replace 'success_url' with the URL name where you want to redirect after successful form submission

    def form_valid(self, form):
        form.save()  # Save the form data to the database
        return super().form_valid(form)


from django.http import HttpResponse
from .models import Music
    
    
def index(request):
    musics = Music.objects.all()
    return render(request, 'songs-one.html', {'musics': musics})

    
def new(request):
    return HttpResponse('New Products')
