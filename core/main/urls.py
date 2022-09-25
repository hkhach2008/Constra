from django.urls import path
from . import views

urlpatterns = [
        path('', views.HomeListView.as_view(), name='home'),
        path('<int:id>', views.HomeValueSubCatDetailView.as_view(), name='home'),
        path('<int:id>', views.HomeProjectCategorySubCatDetailView.as_view(), name='home'),
        path('about/',  views.AboutListView.as_view(), name='about'),
        path('team/', views.TeamListView.as_view(), name='team')
]    