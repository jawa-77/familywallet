from django.contrib import admin
from django.urls import path
from .views import SignUpView,LoginView , VerifyView

 

path('check_verification/', VerifyView.as_view(),name="check_verification"),

User = get_user_model()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignUpView.as_view(),name="signup"),
 
]
