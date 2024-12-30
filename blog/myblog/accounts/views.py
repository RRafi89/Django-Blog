from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views import View
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomLoginForm
from .models import CustomUser
from django.views.generic import CreateView, DeleteView, UpdateView

class CustomRegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        login(self.request, user)
        return response
    

class CustomLoginView(View):
    template_name = 'accounts/login.html'
    
    def get(self, request):
            form = CustomLoginForm()
            return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = CustomLoginForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        return render(request, self.template_name, {'form': form, 'error': 'Invalid Credentials'})

    

@method_decorator(login_required, name='dispatch')
class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
        
class CustomEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'accounts/edit.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Profile updated successfully!')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class CustomDeleteView(DeleteView):
    model = CustomUser
    template_name = 'accounts/delete.html'
    success_url = reverse_lazy('home')
    
    # def get(self, request):
    #     logout(request)
    #     return redirect('home')
    
    def get_object(self, queryset=None):
        return self.request.user
    