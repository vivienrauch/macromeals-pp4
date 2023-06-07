from . import views
from django.urls import path

urlpatterns = [
    path("", views.EntryList.as_view(), name="home"),
    path('contact/', views.contact, name='contact'),
    path('recipes/', views.Recipes.as_view(), name='recipes'),
    path('add_recipe/', views.AddRecipe.as_view(), name='add_recipe'),
    path('<slug:slug>/edit', views.EditRecipe.as_view(), name='edit_recipe'),
    path('<slug:slug>/', views.EntryDetail.as_view(), name='entry_detail'), 
]