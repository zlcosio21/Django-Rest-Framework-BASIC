from rest_framework import viewsets
from .models import Programmer, Product
from .serializer import ProgrammerSerializer, ProductSerializer

# Create your views here.
class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer