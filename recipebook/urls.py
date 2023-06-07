from . import views
from django.urls import path

urlpatterns = [
    path("", views.EntryList.as_view(), name="home"),
    path('contact/', views.contact, name='contact'),
    path('recipes/', views.Recipes.as_view(), name='recipes'),
    path('add_recipe/', views.AddRecipe.as_view(), name='add_recipe'),
    path('recipes/edit/<slug:slug>/', views.EditRecipe.as_view(), name='edit_recipe'),
    path('recipes/delete/<slug:slug>/', views.DeleteRecipe.as_view(), name='delete_recipe'),
    path('<slug:slug>/', views.EntryDetail.as_view(), name='entry_detail'),     
]