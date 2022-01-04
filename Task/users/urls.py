from django.urls import path
from .views import CreateDate

urlpatterns = [
    path('api/schedule/', CreateDate.as_view())
]