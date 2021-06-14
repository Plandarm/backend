from django.urls import path
from . import views


urlpatterns = [
    path('page/<str:page_id>/', views.page, name='page'),
]