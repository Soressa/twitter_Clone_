from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import twitter
from .forms import TwitterForm, UpdateForm
from .models import update


def index(request):
    # if the method is TWITTER
    if request.method == 'POST':
        form = TwitterForm(request.POST, request.FILES)
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()
            # Redirect to home
            return HttpResponseRedirect('/')

        else:
            # No, Show Error
            return HttpResponseRedirect(form.errors.as_json())
    # Get all twitters  
    twitters = twitter.objects.all()

    # show
    return render(request, 'twitter.html', {'twitters': twitters})

def delete(request, twitter_id):
    # find  twitter
    tw = twitter.objects.get(id = twitter_id)
    tw.delete()
    return HttpResponseRedirect('/')

def update(request, twitter_id):
    tw = twitter.objects.get(id = twitter_id)
    form = TwitterForm(instance=tw)
    # if the method is post
    if request.method == 'POST':
        form = TwitterForm(request.POST, request.FILES, instance=tw)
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()
            # Redirect to home
            return redirect('/')

        else:
            # No, Show Error
            return HttpResponseRedirect(form.errors.as_json())

    # show
    return render(request, 'update.html', {'form': form})
