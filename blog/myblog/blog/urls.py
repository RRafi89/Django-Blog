from django.urls import path
from .views import BlogHome, BlogCreate, BlogDetail, BlogEdit, BlogDelete

urlpatterns = [
    path("", BlogHome.as_view(), name="home"),
    path("create/", BlogCreate.as_view(), name="create"),
    path("post/<int:pk>/", BlogDetail.as_view(), name="detail"),
    path("post/<int:pk>/edit/", BlogEdit.as_view(), name="edit"),
    path("post/<int:pk>/delete/", BlogDelete.as_view(), name="delete"),
]
