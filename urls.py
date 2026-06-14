from django.urls import path
from .views import chat_page, ask

urlpatterns = [
    path('', chat_page),
    path('ask/', ask),
]