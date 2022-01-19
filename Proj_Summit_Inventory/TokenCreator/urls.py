from rest_framework.authtoken import views
from django.urls import path
from . import views



# This service should have 4 endpoint(s) to generate a JWT token using a Secret Key
# Endpoint A - token with read_product permission
# Endpoint B - token with manage_product permission
# Endpoint C - token with both: read_product and manage_product permission
# Endpoint D - token with admin permission
# Token should be valid for 10 mins only  #####Trying as model method.
# The token should be stored in the DB  Cache
# Only one token should be valid at any point of time

#appName =


#python manage.py createsuperuser --username Annias --email a@b.com
#python manage.py drf_create_token Annias

#token    3c32af34607b9f02a0871ac222e16fd70d5947c9

urlpatterns = [

    #login
    #logout
    #reset_pass
    path('read_product/', views.ReadProductView.as_view(), name='read'), #ListView
    path('create/', views.CreateAndManageProduct.as_view(), name='create'),
    path('manage_product/<int:pk>/', views.ReadAndManageProduct.as_view(), name='mang'),
    path('rest_admin/', views.AdminManageProduct.as_view(), name='rest_adm'),




]