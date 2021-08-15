from django.shortcuts import render

from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect


from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone

from .models import Post
from .forms import PostForm

from django.urls import reverse_lazy,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,
								DetailView,CreateView,
								UpdateView,DeleteView)



# from .forms import RegisterForm

# Create your views here.
# def base(request):
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = RegisterForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#                 # Create the user:
#                 user = User.objects.create_user(
#                     form.cleaned_data['username'],
#                     form.cleaned_data['password']
#                 )
#                 user.save()
#                 # Login the user
#                 login(request, user)
#                 # redirect to accounts page:
#    # No post data availabe, let's just show the page.
#     # else:
#     #     form = RegisterForm()

#     return render(request,'my_app/base.html')

class CreatePostView(CreateView):
	# login_url = '/login/'
	# redirect_field_name='blog/post_detail.html'

	form_class=PostForm
	model = Post
