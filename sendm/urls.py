from django.urls import path
from sendm.views import ListMail, CreateMail

app_name = 'sendm'
urlpatterns = [
    path('', CreateMail.as_view(), name='index'),
    path('list/', ListMail.as_view(), name='list_mail'),
]
