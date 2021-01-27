from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .form import formUser

# Create your views here.
class Login(LoginView):
	template_name = 'User/login.html'
	success_url = reverse_lazy('home')
	extra_context = {
		'title':'LOGIN'
	}
	query_string = True


	def get(self, request, *args, **kwargs):
		if self.request.user.is_authenticated:
			return redirect('home')
		else:
			 self.extra_context = {
							'title':'LOGIN',
							'next':self.request.GET.get('next', "")
						}
		return self.render_to_response(self.get_context_data())

	def get_success_url(self):
		url = self.request.GET.get('next', False)
		if url is False:
			return self.success_url
		else:
			self.success_url = self.request.GET['next']
			return self.success_url

class Logout(LogoutView):
	next_page = reverse_lazy('home')

class createUser(CreateView):
	model = User
	form_class = formUser
	template_name='User/createUser.html'
	extra_context = {
		'title':'REGISTER USER',
	}
	success_url = reverse_lazy('home')

	def post(self, request):
		form = self.get_form()
		if form.is_valid():
			grup = Group.objects.get(name="User")
			user = form.save()
			user.is_activate = True
			user.save()
			user.groups.add(grup)
			return redirect('home')
		else:
			return super().post(request)




