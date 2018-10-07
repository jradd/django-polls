from django.views.generic import TemplateView
from django.urls import path, include
from django.contrib import admin

from . import views

app_name = 'polls'
urlpatterns = [
#    path('', TemplateView.as_view(template_name="index.html")),
    path('admin/', admin.site.urls),
    #path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
