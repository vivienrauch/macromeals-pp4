from . import views
from django.urls import path
from .views import Contact

urlpatterns = [
    path("", views.EntryList.as_view(), name="home"),
    path('<slug:slug>/', views.EntryDetail.as_view(), name='entry_detail'),
    path('contact/', views.Contact.as_view(), name='contact'),
]