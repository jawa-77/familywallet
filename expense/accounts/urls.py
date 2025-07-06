from django.contrib import admin
from django.urls import path
from .views import SignUpView,LoginView , VerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignUpView.as_view(),name="signup"),
    path('login/', LoginView.as_view(),name="login"),
    path('check_verification/', VerifyView.as_view(),name="check_verification"),
]
