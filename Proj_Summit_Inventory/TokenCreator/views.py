from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from TokenCreator.models import Product
from TokenCreator.serializers import ProductSerializer, No_Delete_ProductSerilizer



#Endpoint A - token with read_product permission
class ReadProductView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Product.objects.filter(delete_now =False)
    serializer_class = No_Delete_ProductSerilizer #should token be a table or a field added to users table.




# Endpoint B - token with manage_product permission ####create only
class CreateProduct(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = No_Delete_ProductSerilizer



# Endpoint C - token with both: read_product and manage_product permission
class UpdateProduct(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Product.objects.filter(delete_now=False) #functioning as soft delete.
    serializer_class = ProductSerializer



#Endpoint D List view with Create - token with admin permission
class CreateReadAdmin(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Product.objects.all() #admin view items soft deleted.
    serializer_class = ProductSerializer

#Endpoint E... Delete view token with admin permission
class DeleteProductAdmin(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]

    queryset = Product.objects.all()  # admin can hard delete
    serializer_class = ProductSerializer

