from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogutView.as_view()),
    path('home/', MaqolalarView.as_view()),
    path('maqola/<int:pk>/', MaqolaView.as_view()),
]
