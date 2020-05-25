from django.urls import include, path
from . import views

app_name = 'indexpage'

urlpatterns = [
  path('', views.IndexPageView.as_view(), )
  # classic view
  # path('', views.indexpage, name='indexpage')
]
