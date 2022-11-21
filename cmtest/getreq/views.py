from rest_framework.viewsets import ModelViewSet
from .models import Getreq
from .serializer import GetReqSerializer


class GetreqViewSet(ModelViewSet):
    serializer_class = GetReqSerializer
    queryset = Getreq.objects.all()
