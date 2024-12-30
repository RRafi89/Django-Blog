from django.urls import path
from .views import CustomRegisterView, CustomLoginView, CustomLogoutView, CustomEditView, CustomDeleteView


urlpatterns = [
    path("register/", CustomRegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("edit/", CustomEditView.as_view(), name='edit_profile'),
    path("delete/", CustomDeleteView.as_view(), name="account_delete"),
]
