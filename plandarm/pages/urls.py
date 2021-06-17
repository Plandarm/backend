from django.urls import path
from . import views


urlpatterns = [
    path('page/create/', views.createPage, name='create_page'),
    path('page/<str:page_id>/', views.page, name='page'),
    path('page/<str:page_id>/save/', views.savePage, name='save_page'),
    path('page/<str:page_id>/delete/', views.deletePage, name='delete_page'),
    path('page/<str:page_id>/error:<str:err>/', views.denyAccess, name='error')
]
