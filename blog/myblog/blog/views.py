from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import EditForm
from .models import Post


class BlogHome(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "blog_home"


class BlogCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/create.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogDetail(DetailView):
    model = Post
    template_name = "blog/detail.html"
    context_object_name = "detail"


class BlogEdit(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = EditForm
    template_name = "blog/edit.html"
    context_object_name = "edit"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def handle_no_permission(self):
        messages.error(self.request, "You don't have permission to edit this post.")
        return redirect("home")


class BlogDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/delete.html"
    context_object_name = 'delete'
    success_url = reverse_lazy("home")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def handle_no_permission(self):
        messages.error(self.request, "You don't have permission to delete this post.")
        return redirect("home")
