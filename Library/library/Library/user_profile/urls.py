from django.urls import path
from . import views
from Library import settings
from django.conf.urls.static import static


urlpatterns = [
    path('user_profile/', views.user_profile, name='user_profile'),
]