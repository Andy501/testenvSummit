from django.core.cache import cache
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from Inventory_API.models import Product # Should this be Inventory_API
from Inventory_API.serializers import ProductSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response



# This service should have 4 endpoint(s) to generate a JWT token using a Secret Key

# Endpoint B - token with manage_product permission
# Endpoint D - token with admin permission
# Token should be valid for 10 mins only
# The token should be stored in the DB / Cache
# Only one token should be valid at any point of time


# Endpoint A - token with read_product permission

#build the service inside of the endpoints.


###TODO: Hide instock field from non admins

class ReadProductView(generics.ListAPIView):

    permission_classes = [IsAuthenticated]

    queryset = Product.objects.filter(delete_now =False)

    serializer_class = ProductSerializer #should token be a table or a field added to users table.



    #token call


# Endpoint B - token with manage_product permission ####create only
class CreateAndManageProduct(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



# Endpoint C - token with both: read_product and manage_product permission
class ReadAndManageProduct(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    queryset = Product.objects.filter(delete_now=False) #functioning as soft delete.
    serializer_class = ProductSerializer



#
class AdminManageProduct(generics.RetrieveUpdateDestroyAPIView):
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAdmin] ####not sure name

    queryset = Product.objects.all() #admin can hard delete
    serializer_class = ProductSerializer






   # """Backend has cache expiring in 10 mins"""
   #  keys = cache.get_or_set('my_new_key', 'my new value')
   #  #if token less than 10 mins share it
   #  #if negatve or greater create new token
   #  #in 10 minutes call self and .save to tokenfield and update time stamp
   #  pass
