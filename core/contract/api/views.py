from rest_framework import viewsets

from contract.models import Contract
from contract.api.serializers import ContractSerializer

class ContractViewSet(viewsets.ModelViewSet):

    serializer_class = ContractSerializer
    queryset = Contract.objects.all()

    