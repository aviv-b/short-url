from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import UrlForm
from .models import Url
from shorturl.settings import SERVER_ID_COUNTER , SERVER_BASE_URL
from helpers import base62


def main(request):
    """ Redirect to create page """ 
    return redirect('create')


def create(request): 
    form = UrlForm()
    short = None 
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            long_url = form.cleaned_data.get('long_url')
            
            """ Check if url exists in db """
            url = Url.objects.filter(long_url = long_url).first()
            if url is None:
                """ Check if not Initial. Then inital id with SERVER_ID_COUNTER """   
                if Url.objects.count() == 0:
                    url = form.save(commit=False)
                    url.id = SERVER_ID_COUNTER
                else:
                    url = form.save() 
                url.short_url = base62.encode(url.id)
                url.save()
                messages.success(request,"Success")
            """ Set short url format: """      
            short =  f'{SERVER_BASE_URL}/s/{url.short_url}'
        else:
            messages.error(request,"Invalid url")
    context = {
        'form':form ,
        'short': short
    }
    return render(request,template_name='create.html',context=context)






def short_url(request,short_url):
    """ Check if url exists """
    try:
        url = Url.objects.get(short_url = short_url)
    except Exception as e:
        messages.error(request,e)
        context = {
            'form': UrlForm(),
        }        
        return redirect('create')
    
    """ Http Redirect to long url """
    return HttpResponseRedirect(url.long_url)
