from django.urls import path
from . import views  # ✅ correct import

urlpatterns = [
    path('', views.signup, name='signup'),  
    path('loginn/', views.loginn, name='loginn'),
]
