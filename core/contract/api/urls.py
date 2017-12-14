from django.conf.urls import url 
from django.contrib import admin 

from contract.api.views import ContractViewSet


urlpatterns = [
    url(r'^contract/$', ContractViewSet.as_view({'get':'list'}), name='list')
]
